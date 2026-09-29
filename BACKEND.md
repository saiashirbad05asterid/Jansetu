# JanSetu backend

JanSetu uses Firebase Authentication, Cloud Firestore, and Cloud Storage for the production data path.

## Collections

- `users/{uid}` stores the signed-in citizen profile and last-seen timestamp.
- `complaints/{complaintId}` stores the report, location, category, triage priority, evidence URL, status, and vote count.
- `complaints/{complaintId}/votes/{uid}` is the unique vote record. A Firestore transaction creates this document and increments the parent vote count atomically.

## Deploy security rules

From this project directory, authenticate Firebase CLI once and deploy the checked-in rules:

```powershell
npx firebase-tools login
npx firebase-tools deploy --only firestore:rules,storage --project playground-0505
```

The application does not trust client-provided vote totals. Firestore rules require authentication for all civic data, restrict complaint creation to the signed-in owner, and restrict each vote path to its matching user ID. Storage limits evidence to authenticated image uploads below 10 MB.

## Environment

Copy `.env.example` to `.env.local` and fill the Firebase web-app values from the `playground-0505` project. Never commit `.env.local`.
