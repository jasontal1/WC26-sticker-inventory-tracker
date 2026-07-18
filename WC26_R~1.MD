# 2026 World Cup Sticker Inventory (live, multi-person)

Two pages, same 980-item Panini checklist:

- `wc26_index.html` — regular stickers
- `wc26_blue.html` — blue border cards

Both read/write the same Firebase Realtime Database (`wc26-stickers` project, to two separate branches), so everyone who has the page open sees each other's entries appear within a second or two.

Files: `wc26_index.html`, `wc26_blue.html`, `wc26_app.js`, `wc26_data.js`, `wc26_styles.css`, `wc26_firebase_config.js`. Keep them all in the same folder — they reference each other by relative filename.

## Firebase config: already wired in

`wc26_firebase_config.js` already has your real `wc26-stickers` project config in it, so opening `wc26_index.html` should show a green "Live — synced with everyone" dot right away.

**One thing to check in the Firebase console:** Realtime Database > Rules. If the database is still in test mode, those rules expire 30 days after creation and the app will silently stop syncing for everyone. Go to Build > Realtime Database > Rules and set something durable, e.g.:

```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```

That's still fully open (anyone with your project URL can read/write — fine for a private link shared with friends, since Firebase project URLs aren't guessable), but it won't expire. Don't post the GitHub Pages link publicly if you go this route.

## Put it on GitHub Pages (so everyone can just open a link)

Put all six files above into one local folder, then from a terminal inside it:

```bash
git init
git add .
git commit -m "WC26 sticker inventory tracker"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

(No repo yet? Go to [github.com/new](https://github.com/new), create an empty one — don't initialize with a README — then use its URL above.)

Then turn on Pages: repo **Settings > Pages > Build and deployment > Source: Deploy from a branch**, branch `main`, folder `/ (root)`, Save. GitHub gives you a URL like:

```
https://<your-username>.github.io/<your-repo>/wc26_index.html
```

Share that link with whoever you want entering data.

## Notes

- If `wc26_firebase_config.js` ever gets reset to placeholder values, the page falls back to saving only in your own browser.
- **Backup** downloads a JSON snapshot of current quantities; **Restore** pushes a JSON file back up to Firebase for everyone.
- **Export CSV** gives you `team, code, number, name, type, quantity` — handy for building eBay listings once you know your duplicates.
