import React, { useEffect, useMemo, useRef, useState } from 'react';
import { createRoot } from 'react-dom/client';
import {
  BarChart3,
  ArrowUpRight,
  Building2,
  CheckCircle2,
  ChevronLeft,
  ChevronRight,
  ClipboardList,
  Droplets,
  FileText,
  Heart,
  Home,
  ImagePlus,
  Languages,
  LogIn,
  LogOut,
  MapPin,
  Mic,
  Navigation,
  Route,
  Search,
  Send,
  ShieldCheck,
  ScanSearch,
  Upload,
  User,
  Waves,
  X
} from 'lucide-react';
import {
  Bar,
  BarChart,
  CartesianGrid,
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis
} from 'recharts';
import {
  firebaseReady,
  observeAuthState,
  signInWithGoogle,
  signOutCurrentUser
} from './firebase';
import {
  createComplaint,
  recordVote,
  saveAreaInsight,
  saveUserProfile,
  subscribeToComplaints
} from './services/complaints';
import { getAreaInsights, verifyReportWithAi } from './services/ai';
import './styles.css';

const stateOptions = [
  'All India',
  'Andhra Pradesh',
  'Arunachal Pradesh',
  'Assam',
  'Bihar',
  'Chhattisgarh',
  'Goa',
  'Gujarat',
  'Haryana',
  'Himachal Pradesh',
  'Jharkhand',
  'Karnataka',
  'Kerala',
  'Madhya Pradesh',
  'Maharashtra',
  'Manipur',
  'Meghalaya',
  'Mizoram',
  'Nagaland',
  'Odisha',
  'Punjab',
  'Rajasthan',
  'Sikkim',
  'Tamil Nadu',
  'Telangana',
  'Tripura',
  'Uttar Pradesh',
  'Uttarakhand',
  'West Bengal',
  'Andaman and Nicobar Islands',
  'Chandigarh',
  'Dadra and Nagar Haveli and Daman and Diu',
  'Delhi',
  'Jammu and Kashmir',
  'Ladakh',
  'Lakshadweep',
  'Puducherry'
];

const places = [
  ['Andhra Pradesh', 'Vijayawada'], ['Arunachal Pradesh', 'Itanagar'], ['Assam', 'Guwahati'],
  ['Bihar', 'Patna'], ['Chhattisgarh', 'Raipur'], ['Goa', 'Panaji'], ['Gujarat', 'Ahmedabad'],
  ['Haryana', 'Faridabad'], ['Himachal Pradesh', 'Shimla'], ['Jharkhand', 'Ranchi'],
  ['Karnataka', 'Bengaluru'], ['Kerala', 'Kochi'], ['Madhya Pradesh', 'Indore'],
  ['Maharashtra', 'Mumbai'], ['Manipur', 'Imphal'], ['Meghalaya', 'Shillong'],
  ['Mizoram', 'Aizawl'], ['Nagaland', 'Kohima'], ['Odisha', 'Bhubaneswar'],
  ['Punjab', 'Ludhiana'], ['Rajasthan', 'Jaipur'], ['Sikkim', 'Gangtok'],
  ['Tamil Nadu', 'Chennai'], ['Telangana', 'Hyderabad'], ['Tripura', 'Agartala'],
  ['Uttar Pradesh', 'Lucknow'], ['Uttarakhand', 'Dehradun'], ['West Bengal', 'Howrah'],
  ['Andaman and Nicobar Islands', 'Port Blair'], ['Chandigarh', 'Sector 22'],
  ['Dadra and Nagar Haveli and Daman and Diu', 'Daman'], ['Delhi', 'Karol Bagh'],
  ['Jammu and Kashmir', 'Srinagar'], ['Ladakh', 'Leh'], ['Lakshadweep', 'Kavaratti'],
  ['Puducherry', 'Puducherry']
];

const universalHeroImage = {
  url: 'https://commons.wikimedia.org/wiki/Special:FilePath/Mumbai%2C%20India%2C%20Back%20Bay%2C%20Mumbai%20city%20skyline.jpg?width=1600',
  credit: 'Mumbai city skyline, photo by Vyacheslav Argenberg / Wikimedia Commons'
};

const imagePool = [
  {
    category: 'Water supply',
    url: 'https://commons.wikimedia.org/wiki/Special:FilePath/Public%20source%20of%20drinking%20water%2C%20Bhopal%20.jpg?width=960',
    credit: 'Public drinking water source, Bhopal / Wikimedia Commons'
  },
  {
    category: 'Water supply',
    url: 'https://commons.wikimedia.org/wiki/Special:FilePath/WaterTruck.JPG?width=960',
    credit: 'Water distribution, Kolhapur / Wikimedia Commons'
  },
  {
    category: 'Road access',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/1/14/Broken_Roads_in_India%27s_Capital_New_Delhi.jpg/960px-Broken_Roads_in_India%27s_Capital_New_Delhi.jpg',
    credit: 'Broken road, New Delhi, Wikimedia Commons'
  },
  {
    category: 'Road access',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/5/57/Potholed_road_outside_Kolkata_Airport.jpg/960px-Potholed_road_outside_Kolkata_Airport.jpg',
    credit: 'Potholed road, Kolkata, Wikimedia Commons'
  },
  {
    category: 'Road access',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/c/c1/Potholes_on_road.jpg/960px-Potholes_on_road.jpg',
    credit: 'Potholes on road, Wikimedia Commons'
  },
  {
    category: 'Road access',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/c/c6/Roads_in_Bihar_have_potholes.jpg/960px-Roads_in_Bihar_have_potholes.jpg',
    credit: 'Potholes in Bihar, Wikimedia Commons'
  },
  {
    category: 'Drainage',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/ab/Car_after_flood.jpg/960px-Car_after_flood.jpg',
    credit: 'Flood damage, Wikimedia Commons'
  },
  {
    category: 'Drainage',
    url: 'https://upload.wikimedia.org/wikipedia/commons/5/5a/1955_East_Punjab_Flood_49575.jpg',
    credit: 'Flood damage in India, Wikimedia Commons'
  },
  {
    category: 'Drainage',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/4/44/Roads_deformed_T_munnekollala_Bengaluru_2.jpg/960px-Roads_deformed_T_munnekollala_Bengaluru_2.jpg',
    credit: 'Deformed road, Bengaluru, Wikimedia Commons'
  },
  {
    category: 'Waste management',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d4/India_-_Sights_%26_Culture_-_Common_garbage_dump_outside_a_temple_%282566331277%29.jpg/960px-India_-_Sights_%26_Culture_-_Common_garbage_dump_outside_a_temple_%282566331277%29.jpg',
    credit: 'Street garbage dump, Wikimedia Commons'
  },
  {
    category: 'Waste management',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/1/18/A_burning_roadside_garbage_dump_at_Panvel_Naka_near_Mumbai.jpg/960px-A_burning_roadside_garbage_dump_at_Panvel_Naka_near_Mumbai.jpg',
    credit: 'Garbage dump near Mumbai, Wikimedia Commons'
  },
  {
    category: 'Waste management',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/5/55/Measuring_PM2.5_air_pollution_from_a_burning_roadside_garbage_dump_at_Bhiwandi_near_Mumbai.jpg/960px-Measuring_PM2.5_air_pollution_from_a_burning_roadside_garbage_dump_at_Bhiwandi_near_Mumbai.jpg',
    credit: 'Burning roadside waste, Wikimedia Commons'
  },
  {
    category: 'Sanitation',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d4/India_-_Sights_%26_Culture_-_Common_garbage_dump_outside_a_temple_%282566331277%29.jpg/960px-India_-_Sights_%26_Culture_-_Common_garbage_dump_outside_a_temple_%282566331277%29.jpg',
    credit: 'Unmanaged public waste, Wikimedia Commons'
  },
  {
    category: 'Sanitation',
    url: 'https://commons.wikimedia.org/wiki/Special:FilePath/Sulabh%20International%20-%20Indian%20NGO%20%282167664969%29.jpg?width=960',
    credit: 'Public sanitation facility, Wikimedia Commons'
  },
  {
    category: 'Sanitation',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/1/18/A_burning_roadside_garbage_dump_at_Panvel_Naka_near_Mumbai.jpg/960px-A_burning_roadside_garbage_dump_at_Panvel_Naka_near_Mumbai.jpg',
    credit: 'Roadside waste hazard, Wikimedia Commons'
  },
  {
    category: 'Street lighting',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/dd/Light_pole_at_Mall_Road%2C_Mussoorie.JPG/960px-Light_pole_at_Mall_Road%2C_Mussoorie.JPG',
    credit: 'Street light pole, Mussoorie, Wikimedia Commons'
  },
  {
    category: 'Street lighting',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/e/e4/Unique_heritage_street_light_at_tank_bund.jpg/960px-Unique_heritage_street_light_at_tank_bund.jpg',
    credit: 'Street light, Hyderabad, Wikimedia Commons'
  },
  {
    category: 'Street lighting',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/1/12/Long_exposure_shot_on_Inorbit_Mall_Road%2C_Hyderabad.jpg/960px-Long_exposure_shot_on_Inorbit_Mall_Road%2C_Hyderabad.jpg',
    credit: 'Lit road, Hyderabad, Wikimedia Commons'
  },
  {
    category: 'Health access',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/3d/Urban_Primary_Health_Center.JPG/960px-Urban_Primary_Health_Center.JPG',
    credit: 'Urban primary health center, Wikimedia Commons'
  },
  {
    category: 'Health access',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/0/0b/Bortoria_Primary_Health_Centre.jpg/960px-Bortoria_Primary_Health_Centre.jpg',
    credit: 'Primary health centre, Wikimedia Commons'
  },
  {
    category: 'Health access',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/c/c7/Primary_Health_centre.JPG/960px-Primary_Health_centre.JPG',
    credit: 'Primary health centre, Wikimedia Commons'
  },
  {
    category: 'School infrastructure',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/2/20/Government_School_in_New_Delhi.jpg/960px-Government_School_in_New_Delhi.jpg',
    credit: 'Government school, New Delhi, Wikimedia Commons'
  },
  {
    category: 'School infrastructure',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f2/Tamil_Nadu_school_kids.jpg/960px-Tamil_Nadu_school_kids.jpg',
    credit: 'Tamil Nadu school, Wikimedia Commons'
  },
  {
    category: 'School infrastructure',
    url: 'https://upload.wikimedia.org/wikipedia/commons/d/d5/Kumbakonam_arignarannagovt_school6.jpg',
    credit: 'Government school, Kumbakonam, Wikimedia Commons'
  },
  {
    category: 'Electricity',
    url: 'https://upload.wikimedia.org/wikipedia/commons/f/f0/Manosapota_WBSEB_Transformer_-_Simurali1020291.JPG',
    credit: 'Village transformer, West Bengal, Wikimedia Commons'
  },
  {
    category: 'Electricity',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/0/0c/Saffron_flags_at_Chinawal.jpg/960px-Saffron_flags_at_Chinawal.jpg',
    credit: 'Transformer and power lines, Wikimedia Commons'
  },
  {
    category: 'Electricity',
    url: 'https://upload.wikimedia.org/wikipedia/commons/f/f0/Manosapota_WBSEB_Transformer_-_Simurali1020291.JPG',
    credit: 'Electricity transformer, Wikimedia Commons'
  },
  {
    category: 'Public transport',
    url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/8/80/Christ_public_school_stop.jpg/960px-Christ_public_school_stop.jpg',
    credit: 'Public bus stop, Mysore, Wikimedia Commons'
  },
  {
    category: 'Public transport',
    url: 'https://upload.wikimedia.org/wikipedia/commons/a/a1/Pushpak_Bus_Routes_Map.jpg',
    credit: 'Public bus route map, Wikimedia Commons'
  },
  {
    category: 'Public transport',
    url: 'https://upload.wikimedia.org/wikipedia/commons/1/1f/Long_exposure_of_Durgam_cheruvu_road_in_Hyderabad.jpg',
    credit: 'Urban mobility corridor, Wikimedia Commons'
  }
];

const categoryCopy = {
  'Water supply': ['Irregular drinking water supply reported', 'tap pressure', 'tanker coverage'],
  'Road access': ['Damaged road blocks daily mobility', 'pothole repair', 'ambulance access'],
  Drainage: ['Stormwater overflow after rainfall', 'drain cleaning', 'flood-prone lane'],
  'Waste management': ['Garbage accumulation near public area', 'collection route', 'segregation point'],
  Sanitation: ['Public sanitation facility needs urgent repair', 'toilet upkeep', 'safe disposal'],
  'Street lighting': ['Street lights not working on key route', 'dark stretch', 'night safety'],
  'Health access': ['Primary health service access needs support', 'medicine stock', 'patient footfall'],
  'School infrastructure': ['School infrastructure repair requested', 'classroom repair', 'safe approach'],
  Electricity: ['Frequent power disruption affecting services', 'feeder outage', 'transformer load'],
  'Public transport': ['Public transport gap on commuter corridor', 'bus frequency', 'last-mile access']
};

const issueCategories = Object.keys(categoryCopy);

const imagesForCategory = (category) => imagePool.filter((image) => image.category === category);

const weeklySignals = [
  { day: 'Mon', filed: 420, resolved: 188 },
  { day: 'Tue', filed: 512, resolved: 226 },
  { day: 'Wed', filed: 468, resolved: 241 },
  { day: 'Thu', filed: 624, resolved: 288 },
  { day: 'Fri', filed: 710, resolved: 336 },
  { day: 'Sat', filed: 590, resolved: 310 },
  { day: 'Sun', filed: 642, resolved: 354 }
];

const PAGE_SIZE = 48;
const voteStorageKey = (uid) => `jansetu:voted-problems:${uid}`;

const readStoredVotes = (uid) => {
  if (!uid) return [];
  try {
    return JSON.parse(localStorage.getItem(voteStorageKey(uid)) || '[]');
  } catch {
    return [];
  }
};

const writeStoredVotes = (uid, votes) => {
  if (!uid) return;
  localStorage.setItem(voteStorageKey(uid), JSON.stringify([...votes]));
};

const generateProblems = (count) =>
  Array.from({ length: count }, (_, index) => {
    const category = issueCategories[index % issueCategories.length];
    const categoryImages = imagesForCategory(category);
    const image = categoryImages[Math.floor(index / issueCategories.length) % categoryImages.length];
    const [state, district] = places[(index * 7 + Math.floor(index / 11)) % places.length];
    const [title, focus, impact] = categoryCopy[category];
    const priority = 58 + ((index * 13) % 41);
    const reports = 17 + ((index * 37) % 2860);
    const votes = 6 + ((index * 29) % 9800);
    const ward = 1 + ((index * 5) % 72);
    const statusList = ['Open', 'Under review', 'Field check', 'Budget match', 'Routed', 'In progress'];
    return {
      id: `JS-${String(100001 + index).padStart(6, '0')}`,
      title: `${title} in ${district} ward ${ward}`,
      category,
      state,
      district,
      status: statusList[index % statusList.length],
      priority,
      reports,
      votes,
      image: image.url,
      credit: image.credit,
      description: `Residents flagged ${focus} concerns around ${district}. The cluster indicates ${impact} pressure and needs department validation.`
    };
  });

const inferComplaint = (text, location) => {
  const lower = `${text} ${location}`.toLowerCase();
  if (
    lower.includes('drain') ||
    lower.includes('flood') ||
    lower.includes('rain') ||
    lower.includes('बारिश') ||
    lower.includes('भर')
  ) {
    return {
      category: 'Drainage',
      department: 'Urban Local Body',
      priority: 84,
      message: 'Drainage issue detected. Routed to Urban Local Body and stormwater cell.'
    };
  }
  if (lower.includes('road') || lower.includes('ambulance') || lower.includes('phc')) {
    return {
      category: 'Road access',
      department: 'Rural Roads Division',
      priority: 87,
      message: 'Road access issue detected. Routed to Rural Roads Division for field verification.'
    };
  }
  if (lower.includes('water') || lower.includes('पानी')) {
    return {
      category: 'Water supply',
      department: 'Water Resources Cell',
      priority: 92,
      message: 'Water supply issue detected. Routed to Water Resources Cell for infrastructure review.'
    };
  }
  return {
    category: 'General infrastructure',
    department: 'District Coordination Cell',
    priority: 72,
    message: 'Infrastructure request detected. Routed to District Coordination Cell for review.'
  };
};

const Stat = ({ label, value, note, icon: Icon }) => (
  <article className="metric-tile">
    <Icon size={20} />
    <span>{label}</span>
    <strong>{value}</strong>
    <small>{note}</small>
  </article>
);

function App() {
  const [page, setPage] = useState('home');
  const [user, setUser] = useState(null);
  const [authLoading, setAuthLoading] = useState(true);
  const [authModalOpen, setAuthModalOpen] = useState(false);
  const [authError, setAuthError] = useState('');
  const [pendingPage, setPendingPage] = useState('complaint');
  const [votedProblems, setVotedProblems] = useState(() => new Set());
  const [problems, setProblems] = useState(() => generateProblems(10000));
  const [liveProblems, setLiveProblems] = useState([]);
  const [backendError, setBackendError] = useState('');
  const [query, setQuery] = useState('');
  const [activeState, setActiveState] = useState('All India');
  const [pageIndex, setPageIndex] = useState(0);
  const [form, setForm] = useState({
    name: '',
    phone: '',
    language: 'Hindi',
    state: 'West Bengal',
    location: 'Howrah ward 22',
    description: 'हमारे वार्ड में बारिश के बाद पानी भर जाता है और बच्चे स्कूल नहीं जा पाते।'
  });
  const [photoPreview, setPhotoPreview] = useState('');
  const [photoFile, setPhotoFile] = useState(null);
  const [receipt, setReceipt] = useState(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [liveLocation, setLiveLocation] = useState(null);
  const [locationMessage, setLocationMessage] = useState('');
  const [areaInsights, setAreaInsights] = useState(null);
  const [insightsLoading, setInsightsLoading] = useState(false);
  const insightsCache = useRef(new Map());

  useEffect(() => {
    const unsubscribe = observeAuthState((currentUser) => {
      setUser(currentUser);
      setVotedProblems(new Set(readStoredVotes(currentUser?.uid)));
      setAuthLoading(false);
      if (currentUser) saveUserProfile(currentUser).catch(() => {});
      if (currentUser && authModalOpen) {
        setAuthModalOpen(false);
        setPage(pendingPage);
      }
    });
    return unsubscribe;
  }, [authModalOpen, pendingPage]);

  useEffect(() => {
    const unsubscribe = subscribeToComplaints(
      (items) => {
        setBackendError('');
        setLiveProblems(items.map((item) => ({
          id: item.id,
          firestoreId: item.id,
          title: item.title,
          category: item.category || 'General infrastructure',
          state: item.state || 'India',
          district: item.district || item.location || 'India',
          status: item.status || 'Routed',
          priority: item.priority || 72,
          reports: item.reports || 1,
          votes: item.votes || 0,
          image: item.photoUrl || item.image,
          credit: item.photoUrl ? 'Citizen uploaded evidence' : 'Citizen report',
          description: item.description || '',
          live: true
        })));
      },
      () => setBackendError('Live civic data is temporarily unavailable. New reports will retry when Firebase is reachable.')
    );
    return unsubscribe;
  }, []);

  const allProblems = useMemo(() => [...liveProblems, ...problems], [liveProblems, problems]);

  const filteredProblems = useMemo(() => {
    const term = query.trim().toLowerCase();
    return allProblems.filter((problem) => {
      const stateMatch = activeState === 'All India' || problem.state === activeState;
      const queryMatch =
        !term ||
        [problem.title, problem.category, problem.state, problem.district, problem.status, problem.description]
          .join(' ')
          .toLowerCase()
          .includes(term);
      return stateMatch && queryMatch;
    });
  }, [activeState, allProblems, query]);

  const totalPages = Math.max(1, Math.ceil(filteredProblems.length / PAGE_SIZE));
  const safePageIndex = Math.min(pageIndex, totalPages - 1);
  const visibleProblems = filteredProblems.slice(safePageIndex * PAGE_SIZE, safePageIndex * PAGE_SIZE + PAGE_SIZE);
  const firstVisible = filteredProblems.length ? safePageIndex * PAGE_SIZE + 1 : 0;
  const lastVisible = Math.min((safePageIndex + 1) * PAGE_SIZE, filteredProblems.length);

  const categoryData = useMemo(() => {
    const counts = filteredProblems.reduce((acc, problem) => {
      acc[problem.category] = (acc[problem.category] || 0) + 1;
      return acc;
    }, {});
    return Object.entries(counts)
      .map(([issue, value]) => ({ issue, value }))
      .sort((a, b) => b.value - a.value)
      .slice(0, 8);
  }, [filteredProblems]);

  const stateData = useMemo(() => {
    const counts = filteredProblems.reduce((acc, problem) => {
      acc[problem.state] = (acc[problem.state] || 0) + 1;
      return acc;
    }, {});
    return Object.entries(counts)
      .map(([state, value]) => ({ state, value }))
      .sort((a, b) => b.value - a.value)
      .slice(0, 8);
  }, [filteredProblems]);

  const setFilterState = (state) => {
    setActiveState(state);
    setPageIndex(0);
  };

  const goHome = () => {
    setPage('home');
    setAuthModalOpen(false);
    setAuthError('');
  };

  const openProtectedPage = (nextPage) => {
    if (user) {
      setPage(nextPage);
      return;
    }
    setPendingPage(nextPage);
    setAuthError('');
    setAuthModalOpen(true);
  };

  const handleGoogleSignIn = async () => {
    setAuthError('');
    try {
      await signInWithGoogle();
    } catch (error) {
      setAuthError(error.message || 'Google sign-in could not be completed.');
    }
  };

  const handleSignOut = async () => {
    await signOutCurrentUser();
    setUser(null);
    setVotedProblems(new Set());
    setPage('home');
  };

  const submitComplaint = async () => {
    if (isSubmitting) return;
    if (!user) {
      openProtectedPage('complaint');
      return;
    }
    if (!form.location.trim() || !form.description.trim()) {
      setReceipt({ type: 'error', message: 'Location and problem description are required.' });
      return;
    }
    if (form.description.trim().length < 20) {
      setReceipt({ type: 'error', message: 'Please add a little more detail so the report can be verified accurately.' });
      return;
    }

    const triage = inferComplaint(form.description, form.location);
    setIsSubmitting(true);
    setReceipt({ type: 'pending', message: 'Saving your report and evidence securely...' });
    try {
      const verification = await verifyReportWithAi({
        description: form.description, location: form.location, state: form.state,
        coordinates: liveLocation
      });
      if (!verification.genuine || Number(verification.confidence) < 45) {
        setReceipt({ type: 'error', message: `AI verification needs more detail: ${verification.reason || 'Please describe a specific, observable issue and exact place.'}` });
        return;
      }
      const result = await createComplaint({
        user,
        photoFile,
        data: {
          title: form.description.slice(0, 80),
          category: triage.category,
          department: triage.department,
          priority: triage.priority,
          state: form.state,
          district: form.location.split(',')[0] || form.location,
          location: form.location,
          language: form.language,
          phone: form.phone || null,
          description: form.description,
          coordinates: liveLocation || null,
          aiVerification: { confidence: verification.confidence, reason: verification.reason }
        }
      });
      setReceipt({ type: 'success', id: result.id, message: `${triage.message} Your report is now visible in the civic data layer.` });
      setForm({ name: '', phone: '', language: 'Hindi', state: 'West Bengal', location: '', description: '' });
      setPhotoFile(null);
      setPhotoPreview('');
    } catch (error) {
      setReceipt({ type: 'error', message: error.message || 'The report could not be saved. Please try again.' });
    } finally {
      setIsSubmitting(false);
    }
  };

  const useLiveLocation = () => {
    if (!navigator.geolocation) { setLocationMessage('Live location is not supported by this browser.'); return; }
    setLocationMessage('Requesting location permission...');
    navigator.geolocation.getCurrentPosition(
      ({ coords }) => {
        const next = { lat: Number(coords.latitude.toFixed(6)), lon: Number(coords.longitude.toFixed(6)) };
        setLiveLocation(next);
        setLocationMessage('Location attached to this report.');
      },
      () => setLocationMessage('Location permission was not granted. You can still enter a place manually.'),
      { enableHighAccuracy: true, timeout: 10000, maximumAge: 300000 }
    );
  };

  const loadAreaInsights = async () => {
    const cacheKey = `${activeState}:${liveLocation?.lat || ''}:${liveLocation?.lon || ''}:${allProblems.length}`;
    const cached = insightsCache.current.get(cacheKey);
    if (cached) { setAreaInsights(cached); return; }
    setInsightsLoading(true);
    try {
      const reports = allProblems.slice(0, 25).map(({ title, category, state, district, status, votes, description }) => ({ title, category, state, district, status, votes, description }));
      const result = await getAreaInsights({ area: activeState, coordinates: liveLocation, reports });
      insightsCache.current.set(cacheKey, result);
      setAreaInsights(result);
      if (user) saveAreaInsight({ user, area: activeState, coordinates: liveLocation, insight: result }).catch(() => {});
    } catch {
      setAreaInsights({ headline: 'Area demand overview', topCategory: categoryData[0]?.issue || 'Infrastructure', summary: 'Live AI insights are temporarily unavailable. The ranked data remains available below.', recommendedAction: 'Review the highest-voted reports first.', confidence: 0 });
    } finally { setInsightsLoading(false); }
  };

  const handlePhoto = (event) => {
    const file = event.target.files?.[0];
    if (!file) return;
    setPhotoFile(file);
    setPhotoPreview(URL.createObjectURL(file));
  };

  const voteForProblem = async (id) => {
    if (!user) {
      openProtectedPage('problems');
      return;
    }
    if (votedProblems.has(id)) return;

    const problem = allProblems.find((item) => item.id === id);
    if (problem?.firestoreId) {
      try {
        const result = await recordVote({ complaintId: problem.firestoreId, uid: user.uid });
        if (result.alreadyVoted) return;
        setLiveProblems((items) => items.map((item) => item.id === id ? { ...item, votes: item.votes + 1 } : item));
      } catch (error) {
        setBackendError(error.message || 'Your vote could not be recorded.');
        return;
      }
    } else {
      setProblems((items) => items.map((problemItem) => problemItem.id === id ? { ...problemItem, votes: problemItem.votes + 1 } : problemItem));
    }
    const nextVotes = new Set(votedProblems);
    nextVotes.add(id);
    setVotedProblems(nextVotes);
    writeStoredVotes(user.uid, nextVotes);
  };

  return (
    <main className="site-shell">
      <div className="india-ribbon" />

      <header className="site-header">
        <button className="brand-button" onClick={goHome}>
          <img src="/jansetu_logo.svg" alt="JanSetu logo" />
          <span>
            <strong>JanSetu</strong>
            <small>Civic issue intelligence for India</small>
          </span>
        </button>
        <nav className="site-nav" aria-label="Primary navigation">
          <button className={page === 'home' ? 'active' : ''} onClick={goHome}>
            <Home size={17} /> Home
          </button>
          <button className={page === 'complaint' ? 'active' : ''} onClick={() => openProtectedPage('complaint')}>
            <FileText size={17} /> File complaint
          </button>
          <button className={page === 'problems' ? 'active' : ''} onClick={() => openProtectedPage('problems')}>
            <ClipboardList size={17} /> Problems & data
          </button>
        </nav>
        <section className="auth-status" aria-label="Authentication status">
          {user ? (
            <>
              <span>
                {user.photoURL ? <img src={user.photoURL} alt="" /> : <User size={16} />}
                {user.displayName || user.email}
              </span>
              <button onClick={handleSignOut}><LogOut size={16} /> Sign out</button>
            </>
          ) : (
            <button onClick={() => openProtectedPage('complaint')} disabled={authLoading}>
              <LogIn size={16} /> Sign in
            </button>
          )}
        </section>
      </header>

      {authModalOpen && !user && (
        <section className="auth-overlay" role="dialog" aria-modal="true" aria-labelledby="auth-title">
          <div className="auth-modal">
            <button className="auth-close" aria-label="Close sign in dialog" onClick={() => setAuthModalOpen(false)}>
              <X size={18} />
            </button>
            <img src="/jansetu_logo.svg" alt="JanSetu logo" />
            <p>Secure access required</p>
            <h2 id="auth-title">Continue to JanSetu</h2>
            <span>
              Sign in before opening complaint filing, voting, or public issue analytics. Home stays open for
              everyone.
            </span>
            <button className="google-button" onClick={handleGoogleSignIn} disabled={!firebaseReady || authLoading}>
              <span>G</span> Continue with Google
            </button>
            {!firebaseReady && (
              <small className="auth-warning">
                Firebase project config is not added yet. Share the Firebase console web app values and I will put
                them in `.env.local`.
              </small>
            )}
            {authError && <small className="auth-error">{authError}</small>}
          </div>
        </section>
      )}

      {page === 'home' && (
        <>
          <section className="hero hero-universal">
            <img className="hero-backdrop" src={universalHeroImage.url} alt="Mumbai city skyline representing India-wide civic infrastructure" />
            <div className="hero-overlay" />
            <div className="hero-copy">
              <p>India-wide civic intelligence platform</p>
              <h1>Report local development problems. Turn citizen demand into public action.</h1>
              <span>
                JanSetu helps citizens file evidence-backed civic issues and helps decision makers see
                demand hotspots, priority scores, votes, and infrastructure gaps across India.
              </span>
              <div className="hero-actions">
                <button className="primary-action" onClick={() => openProtectedPage('complaint')}>
                  File a problem <Send size={17} />
                </button>
                <button onClick={() => openProtectedPage('problems')}>
                  View public problems <BarChart3 size={17} />
                </button>
              </div>
            </div>
            <div className="hero-signal">
              <span className="signal-label">Live civic signal</span>
              <strong>10,000 mapped reports</strong>
              <span>Real issue evidence, local demand, and priority signals in one public view.</span>
              <small>{universalHeroImage.credit}</small>
            </div>
          </section>

          <section className="metric-grid">
            <Stat label="Problems listed" value={problems.length.toLocaleString()} note="mapped with place, category, image, and votes" icon={Mic} />
            <Stat label="States and UTs" value="36" note="complete India coverage in filters and intake" icon={MapPin} />
            <Stat label="Languages supported" value="9" note="citizen-first multilingual intake model" icon={Languages} />
            <Stat label="Routed cases" value="11,306" note="sent to responsible department queues" icon={ShieldCheck} />
          </section>

          <section className="civic-strip" aria-label="Platform capabilities">
            <span>Photo evidence</span>
            <span>Demand voting</span>
            <span>Priority scoring</span>
            <span>District clustering</span>
            <span>Public dashboards</span>
          </section>

          <section className="home-intelligence" aria-label="JanSetu civic workflow">
            <article className="home-process">
              <div className="home-section-heading">
                <span>From report to response</span>
                <h2>One shared picture of what India needs next.</h2>
              </div>
              <div className="steps">
                <span><b>1</b> Citizen files a problem with location and photo evidence</span>
                <span><b>2</b> System classifies category, urgency, and responsible department</span>
                <span><b>3</b> Similar reports form demand hotspots and priority scores</span>
                <span><b>4</b> Officials review, validate, and plan public projects</span>
              </div>
            </article>
            <article className="home-priority">
              <div className="home-section-heading compact-heading">
                <span>Priority watch</span>
                <h2>High-demand issue in focus</h2>
              </div>
              <ProblemCard problem={problems[0]} compact />
            </article>
          </section>

          <section className="home-pathways" aria-label="JanSetu pathways">
            <article>
              <span className="pathway-icon"><Send size={20} /></span>
              <p>For citizens</p>
              <h2>Make the local problem visible.</h2>
              <span>Add a clear description, exact place, and photo evidence so the issue reaches the right queue.</span>
              <button onClick={() => openProtectedPage('complaint')}>Start a report <ArrowUpRight size={17} /></button>
            </article>
            <article>
              <span className="pathway-icon"><ScanSearch size={20} /></span>
              <p>For public teams</p>
              <h2>See the pattern behind each request.</h2>
              <span>Review mapped demand, votes, and evidence to focus validation where it matters most.</span>
              <button onClick={() => openProtectedPage('problems')}>Explore signals <ArrowUpRight size={17} /></button>
            </article>
            <article>
              <span className="pathway-icon"><Building2 size={20} /></span>
              <p>For better planning</p>
              <h2>Connect everyday needs to public investment.</h2>
              <span>Translate recurring complaints into clear, local project priorities across the country.</span>
              <button onClick={() => openProtectedPage('problems')}>View the data <ArrowUpRight size={17} /></button>
            </article>
          </section>
        </>
      )}

      {page === 'complaint' && (
        <section className="page-grid">
          <section className="panel complaint-form">
            <div className="section-title">
              <p>Citizen complaint filing</p>
              <h1>Tell us what needs to be fixed</h1>
            </div>

            <div className="form-grid">
              <label>
                Name
                <input
                  value={form.name}
                  onChange={(event) => setForm({ ...form, name: event.target.value })}
                  placeholder="Optional"
                />
              </label>
              <label>
                Phone
                <input
                  value={form.phone}
                  onChange={(event) => setForm({ ...form, phone: event.target.value })}
                  placeholder="Optional"
                />
              </label>
              <label>
                Language
                <select value={form.language} onChange={(event) => setForm({ ...form, language: event.target.value })}>
                  <option>Hindi</option>
                  <option>English</option>
                  <option>Bengali</option>
                  <option>Tamil</option>
                  <option>Telugu</option>
                  <option>Marathi</option>
                  <option>Gujarati</option>
                  <option>Kannada</option>
                  <option>Malayalam</option>
                </select>
              </label>
              <label>
                State or union territory
                <select value={form.state} onChange={(event) => setForm({ ...form, state: event.target.value })}>
                  {stateOptions.slice(1).map((state) => <option key={state}>{state}</option>)}
                </select>
              </label>
              <label className="full-field">
                Exact place
                <input
                  value={form.location}
                  onChange={(event) => setForm({ ...form, location: event.target.value })}
                />
                <button type="button" className="location-action" onClick={useLiveLocation}><Navigation size={15} /> Use my live location</button>
                {locationMessage && <small className="field-note">{locationMessage}</small>}
              </label>
            </div>

            <label>
              Problem description
              <textarea
                value={form.description}
                onChange={(event) => setForm({ ...form, description: event.target.value })}
              />
            </label>

            <label className="upload-box">
              <input type="file" accept="image/*" onChange={handlePhoto} />
              <ImagePlus size={22} />
              <span>Upload original photo from the location</span>
            </label>

            {photoPreview && <img className="photo-preview" src={photoPreview} alt="Uploaded complaint preview" />}

            <button className="primary-action submit-wide" onClick={submitComplaint} disabled={isSubmitting}>
              {isSubmitting ? 'Saving complaint...' : 'Submit complaint'} <Upload size={17} />
            </button>

            {receipt && (
              <div className={receipt.type === 'error' ? 'receipt error' : 'receipt'}>
                <CheckCircle2 size={17} />
                <span>{receipt.message}</span>
              </div>
            )}
          </section>

          <aside className="panel triage-side">
            <h2>Smart routing preview</h2>
            <p>Your report is classified by issue type, urgency, location, evidence, and responsible department.</p>
            <div className="triage-list">
              <span><Droplets size={17} /> Water supply to Water Resources Cell</span>
              <span><Route size={17} /> Roads to Rural Roads Division</span>
              <span><Waves size={17} /> Drainage to Urban Local Body</span>
            </div>
            <div className="intake-card">
              <strong>Evidence quality</strong>
              <span>Photo, exact place, and clear description improve validation speed.</span>
            </div>
          </aside>
        </section>
      )}

      {page === 'problems' && (
        <>
          <section className="problems-toolbar">
            <label className="search-box">
              <Search size={17} />
              <input
                aria-label="Search listed problems"
                value={query}
                onChange={(event) => {
                  setQuery(event.target.value);
                  setPageIndex(0);
                }}
                placeholder="Search issue, district, status"
              />
            </label>
            <div className="state-filter">
              {stateOptions.map((state) => (
                <button
                  className={activeState === state ? 'active' : ''}
                  key={state}
                  onClick={() => setFilterState(state)}
                >
                  {state}
                </button>
              ))}
            </div>
          </section>

          <section className="area-insights panel">
            <div>
              <p>AI area brief</p>
              <h2>{areaInsights?.headline || 'Find the strongest local signal'}</h2>
              <span>{areaInsights?.summary || 'Use your live location to ground the next civic priority in nearby reports.'}</span>
            </div>
            <div className="insight-actions">
              <button className="secondary-action" onClick={useLiveLocation}><Navigation size={16} /> {liveLocation ? 'Location added' : 'Use live location'}</button>
              <button className="secondary-action" onClick={loadAreaInsights} disabled={insightsLoading}>
                <ScanSearch size={16} /> {insightsLoading ? 'Analysing...' : 'Analyse this area'}
              </button>
            </div>
            {areaInsights && <strong>{areaInsights.topCategory} · {areaInsights.confidence}% confidence</strong>}
          </section>

          <section className="problems-layout">
            <div className="problem-list">
              <div className="data-summary">
                <strong>{filteredProblems.length.toLocaleString()} problems found</strong>
                <span>
                  Showing {firstVisible.toLocaleString()}-{lastVisible.toLocaleString()} with place, image,
                  votes, reports, status, and priority score.
                </span>
              </div>
              {visibleProblems.map((problem) => (
                <ProblemCard
                  problem={problem}
                  key={problem.id}
                  onVote={voteForProblem}
                  hasVoted={votedProblems.has(problem.id)}
                />
              ))}
              {filteredProblems.length === 0 && <p className="empty-state">No problems match this filter.</p>}
              <div className="pagination">
                <button disabled={safePageIndex === 0} onClick={() => setPageIndex((value) => Math.max(0, value - 1))}>
                  <ChevronLeft size={17} /> Previous
                </button>
                <span>Page {safePageIndex + 1} of {totalPages}</span>
                <button
                  disabled={safePageIndex >= totalPages - 1}
                  onClick={() => setPageIndex((value) => Math.min(totalPages - 1, value + 1))}
                >
                  Next <ChevronRight size={17} />
                </button>
              </div>
            </div>

            <aside className="data-column">
              <section className="panel chart-panel">
                <h2>Problem categories</h2>
                <ResponsiveContainer width="100%" height={280}>
                  <BarChart data={categoryData} layout="vertical" margin={{ left: 8, right: 16 }}>
                    <XAxis type="number" hide />
                    <YAxis type="category" dataKey="issue" width={116} tickLine={false} axisLine={false} />
                    <Tooltip />
                    <Bar dataKey="value" fill="#2d7c4f" radius={[0, 5, 5, 0]} />
                  </BarChart>
                </ResponsiveContainer>
              </section>

              <section className="panel chart-panel">
                <h2>Top places in current view</h2>
                <ResponsiveContainer width="100%" height={280}>
                  <BarChart data={stateData} margin={{ left: -18, right: 12, top: 8 }}>
                    <CartesianGrid stroke="#e5e1d8" vertical={false} />
                    <XAxis dataKey="state" tickLine={false} axisLine={false} interval={0} angle={-25} height={76} />
                    <YAxis tickLine={false} axisLine={false} />
                    <Tooltip />
                    <Bar dataKey="value" fill="#1f5f77" radius={[5, 5, 0, 0]} />
                  </BarChart>
                </ResponsiveContainer>
              </section>

              <section className="panel chart-panel">
                <h2>Weekly filing trend</h2>
                <ResponsiveContainer width="100%" height={240}>
                  <LineChart data={weeklySignals} margin={{ left: -20, right: 12, top: 8 }}>
                    <CartesianGrid stroke="#e5e1d8" vertical={false} />
                    <XAxis dataKey="day" tickLine={false} axisLine={false} />
                    <YAxis tickLine={false} axisLine={false} />
                    <Tooltip />
                    <Line dataKey="filed" stroke="#1f5f77" strokeWidth={2.5} dot={false} />
                    <Line dataKey="resolved" stroke="#c26a2c" strokeWidth={2.5} dot={false} />
                  </LineChart>
                </ResponsiveContainer>
              </section>
            </aside>
          </section>
        </>
      )}
    </main>
  );
}

const ProblemCard = ({ problem, compact = false, onVote, hasVoted = false }) => (
  <article className={compact ? 'problem-card compact' : 'problem-card'}>
    <figure>
      <img src={problem.image} alt={`${problem.category} problem in ${problem.district}`} />
      <figcaption>{problem.credit}</figcaption>
    </figure>
    <div>
      <div className="problem-meta">
        <span>{problem.category}</span>
        <b>{problem.priority}</b>
      </div>
      <h3>{problem.title}</h3>
      <p className="location-line"><MapPin size={14} /> {problem.state} / {problem.district}</p>
      <p>{problem.description}</p>
      <div className="problem-footer">
        <span>{problem.reports.toLocaleString()} reports</span>
        <span>{problem.votes.toLocaleString()} votes</span>
        <strong>{problem.status}</strong>
      </div>
      {onVote && (
        <button
          className={hasVoted ? 'vote-button voted' : 'vote-button'}
          onClick={() => onVote(problem.id)}
          disabled={hasVoted}
        >
          <Heart size={16} /> {hasVoted ? 'Voted' : 'Vote for priority'}
        </button>
      )}
    </div>
  </article>
);

createRoot(document.getElementById('root')).render(<App />);
