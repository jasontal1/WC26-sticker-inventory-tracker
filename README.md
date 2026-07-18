# 2026 World Cup Sticker Inventory (live, multi-person)

Two pages, same 980-item Panini checklist:

- `index.html` — regular stickers
- `blue.html` — blue border cards

Both read/write the same Firebase Realtime Database (to different branches), so everyone who has the page open sees each other's entries appear within a second or two — no more "who has the spreadsheet open."

## 1. Create the Firebase project (~3 minutes)

1. Go to [console.firebase.google.com](https://console.firebase.google.com) and sign in with your Google account.
2. Click **Add project**, name it anything (e.g. `wc26-stickers`), skip Google Analytics (not needed).
3. In the left sidebar, click **Build > Realtime Database > Create Database**. Pick any region, and start in **test mode** (this makes it open read/write — fine for a private link shared with friends; see the security note below).
4. In the left sidebar, click the gear icon > **Project settings**. Under "Your apps," click the `</>` (Web) icon to register a new web app (any nickname is fine, no need for Firebase Hosting).
5. Firebase will show you a `firebaseConfig` object. Copy it.

## 2. Wire it into the tool

Open `firebase-config.js` in this folder and replace the placeholder object with the one you copied, e.g.:

```js
window.FIREBASE_CONFIG = {
  apiKey: "AIzaSy...",
  authDomain: "wc26-stickers.firebaseapp.com",
  databaseURL: "https://wc26-stickers-default-rtdb.firebaseio.com",
  projectId: "wc26-stickers",
  storageBucket: "wc26-stickers.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abcdef"
};
```

Save the file. That's the only code change needed — `index.html` and `blue.html` both pick it up automatically.

**Security note:** test-mode rules let anyone with your Firebase URL read/write the database. That's fine for a small group with a private link, but don't post the link publicly. If you want to lock it down later, go to Realtime Database > Rules and restrict write access (e.g. require Firebase Auth, or set an expiry date).

## 3. Put it on GitHub Pages (so everyone can just open a link)

From a terminal, inside this folder:

```bash
git init
git add .
git commit -m "WC26 sticker inventory tracker"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

(If you don't have a repo yet: go to [github.com/new](https://github.com/new), create an empty repo — don't initialize with a README — then use its URL above.)

Then turn on Pages: in the repo, **Settings > Pages > Build and deployment > Source: Deploy from a branch**, branch `main`, folder `/ (root)`, Save. GitHub gives you a URL like:

```
https://<your-username>.github.io/<your-repo>/
```

Share that link with whoever you want entering data — everyone typing into it at once will see the same live totals.

## Notes

- If `firebase-config.js` is still the placeholder, the page falls back to saving only in your own browser (same as before) so it still works standalone.
- **Backup** downloads a JSON snapshot of current quantities; **Restore** pushes a JSON file back up to Firebase for everyone.
- **Export CSV** gives you `team, code, number, name, type, quantity` — handy for building eBay listings once you know your duplicates.
