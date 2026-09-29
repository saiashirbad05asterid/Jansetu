# Continuous deployment

Every push to `main` runs the production build, deploys the Cloud Run API, and releases Firebase Hosting, Firestore rules, and Storage rules.

Configure these GitHub repository secrets before enabling the workflow:

- `FIREBASE_ENV`: the complete contents of the production `.env.local` file.
- `GCP_SERVICE_ACCOUNT_JSON`: a Google Cloud service-account JSON key with Cloud Run Admin, Service Account User, Cloud Build Editor, Firebase Rules Admin, and Hosting Admin access.

The Firebase project is `playground-0505`, the Firebase Hosting site is `jansetu` (`jansetu.web.app`), the Cloud Run region is `asia-south1`, and the service is `jansetu-api`.

The one-time site creation command is:

```powershell
npx firebase-tools@15.32.0 hosting:sites:create jansetu --project playground-0505
```

## ADK agents

The two agent definitions live in `agents/`: `civic_integrity_agent` for report verification and `area_policy_agent` for local prioritisation. Only the policy agent has the Google Search tool, and it is instructed to search only for explicit current-policy or public-data context. Install `agents/requirements.txt` and run `adk web agents` for local testing. Report records, AI verification metadata, coordinates, votes, and saved area insights are stored in Firebase.
