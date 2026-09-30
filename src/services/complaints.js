import {
  addDoc,
  collection,
  doc,
  increment,
  limit,
  onSnapshot,
  orderBy,
  query,
  runTransaction,
  serverTimestamp,
  setDoc
} from 'firebase/firestore';
import { getDownloadURL, ref, uploadBytes } from 'firebase/storage';
import { db, storage } from '../firebase';

const complaintsCollection = () => {
  if (!db) throw new Error('Firestore is not configured. Check your Firebase environment values.');
  return collection(db, 'complaints');
};

export const subscribeToComplaints = (onData, onError) => {
  if (!db) return () => {};
  return onSnapshot(
    query(complaintsCollection(), orderBy('createdAt', 'desc'), limit(300)),
    (result) => onData(result.docs.map((item) => ({ id: item.id, ...item.data(), live: true }))),
    onError
  );
};

export const uploadComplaintPhoto = async (file, uid, complaintId) => {
  if (!file || !storage) return null;
  const safeName = file.name.replace(/[^a-zA-Z0-9._-]/g, '-');
  const photoRef = ref(storage, `complaint-images/${uid}/${complaintId}/${safeName}`);
  await uploadBytes(photoRef, file, { contentType: file.type || 'image/jpeg' });
  return getDownloadURL(photoRef);
};

export const createComplaint = async ({ user, data, photoFile }) => {
  const complaintRef = doc(complaintsCollection());
  const photoUrl = await uploadComplaintPhoto(photoFile, user.uid, complaintRef.id);
  await setDoc(complaintRef, {
    ...data,
    photoUrl: photoUrl || null,
    userId: user.uid,
    userName: user.displayName || 'JanSetu citizen',
    userPhotoUrl: user.photoURL || null,
    status: 'Routed',
    reports: 1,
    votes: 0,
    source: 'citizen',
    createdAt: serverTimestamp(),
    updatedAt: serverTimestamp()
  });
  return { id: complaintRef.id, photoUrl };
};

export const saveAreaInsight = async ({ user, area, coordinates, insight }) => {
  if (!db || !user || !insight) return;
  const insightRef = doc(collection(db, 'areaInsights'));
  await setDoc(insightRef, {
    userId: user.uid,
    area: area || 'All India',
    coordinates: coordinates || null,
    insight,
    createdAt: serverTimestamp()
  });
};

export const recordVote = async ({ complaintId, uid }) => {
  if (!db) throw new Error('Firestore is not configured.');
  const complaintRef = doc(db, 'complaints', complaintId);
  const voteRef = doc(db, 'complaints', complaintId, 'votes', uid);
  return runTransaction(db, async (transaction) => {
    const [complaintSnapshot, voteSnapshot] = await Promise.all([
      transaction.get(complaintRef),
      transaction.get(voteRef)
    ]);
    if (!complaintSnapshot.exists()) throw new Error('This problem is no longer available.');
    if (voteSnapshot.exists()) return { alreadyVoted: true };
    transaction.set(voteRef, { uid, createdAt: serverTimestamp() });
    transaction.update(complaintRef, { votes: increment(1), updatedAt: serverTimestamp() });
    return { alreadyVoted: false };
  });
};

export const saveUserProfile = async (user) => {
  if (!db || !user) return;
  await setDoc(doc(db, 'users', user.uid), {
    uid: user.uid,
    displayName: user.displayName || 'JanSetu citizen',
    email: user.email || null,
    photoURL: user.photoURL || null,
    lastSeenAt: serverTimestamp()
  }, { merge: true });
};
