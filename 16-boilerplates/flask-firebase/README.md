# Flask + Firebase Hackathon Boilerplate

A quick-start template for hackathons using Flask and Firebase Authentication.

## Quick Start

```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment variables
cp .env.example .env
# Edit .env with your Firebase config

# 4. Run the app
python app.py
```

Open [http://localhost:5000](http://localhost:5000).

## Setup Steps

### 1. Create a Firebase Project

Go to [console.firebase.google.com](https://console.firebase.google.com) and create a project.

### 2. Enable Authentication

In Firebase Console:
- Go to **Authentication** → **Sign-in method**
- Enable **Email/Password** and/or **Google** provider
- Add your app's domain to **Authorized domains**

### 3. Get Firebase Config

- Go to **Project Settings** → **General** → **Your apps**
- Click the web icon (</>) to add a web app
- Copy the config object values into your `.env` file

### 4. Get Service Account Key (for server-side)

- Go to **Project Settings** → **Service accounts**
- Click **Generate new private key**
- Save as `serviceAccountKey.json` in the project root
- Add it to `.gitignore`!

### 5. Firebase Config for Client-side

Create `templates/firebase_config.js` with your Firebase config:

```javascript
const firebaseConfig = {
  apiKey: "your-api-key",
  authDomain: "your-project.firebaseapp.com",
  projectId: "your-project-id",
  storageBucket: "your-project.appspot.com",
  messagingSenderId: "123456789",
  appId: "your-app-id"
};
```

## Project Structure

```
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variable template
├── templates/
│   ├── index.html         # Landing page with login
│   └── dashboard.html     # Protected dashboard
└── README.md
```

## Tech Stack

- **Backend:** Flask (Python)
- **Auth:** Firebase Authentication
- **Database:** Firestore (add as needed)
- **Styling:** Tailwind CSS via CDN

## What's Included

- Firebase auth initialization
- Email/password sign-up and sign-in
- Google OAuth sign-in
- Protected routes with session management
- Basic responsive UI

## License

MIT — use this for any hackathon, no strings attached.
