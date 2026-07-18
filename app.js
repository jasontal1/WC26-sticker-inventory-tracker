// Expects window.STICKER_DATA, window.FIREBASE_CONFIG, and window.COLLECTION_KEY
// (COLLECTION_KEY set inline in index.html / blue.html so both pages share this file
// but write to separate branches of the same Firebase database: /inventory/regular vs /inventory/blue)

const DATA = window.STICKER_DATA;
const COLLECTION_KEY = window.COLLECTION_KEY || 'regular';

let qty = {};
let dbRef = null;
let firebaseReady = false;

function key(item){ return item.code + '-' + item.num; }
function getQty(item){ return qty[key(item)] || 0; }

function setQty(item, v){
  v = Math.max(0, Math.min(999, Math.floor(v) || 0));
  const k = key(item);
  if(firebaseReady){
    // write straight to Firebase; the live listener below updates qty + UI for everyone,
    // including this tab, once the write round-trips.
    if(v === 0) dbRef.child(k).remove();
    else dbRef.child(k).set(v);
  } else {
    // offline fallback so the tool still works if Firebase isn't configured yet
    if(v === 0) delete qty[k]; else qty[k] = v;
    localStorage.setItem('wc26_local_' + COLLECTION_KEY, JSON.stringify(qty));
    refreshEverything();
  }
}

// ---------- Firebase wiring ----------
function initFirebase(){
  const cfg = window.FIREBASE_CONFIG;
  const looksConfigured = cfg && cfg.databaseURL && !String(cfg.databaseURL).includes('YOUR_PROJECT');
  if(!looksConfigured || typeof firebase === 'undefined'){
    setSyncStatus(false, 'Not connected — edit firebase-config.js to enable live sync');
    // fall back to any local cache so the page isn't empty
    try { qty = JSON.parse(localStorage.getItem('wc26_local_' + COLLECTION_KEY) || '{}'); } catch(e){ qty = {}; }
    return;
  }
  try {
    firebase.initializeApp(cfg);
    const db = firebase.database();
    dbRef = db.ref('inventory/' + COLLECTION_KEY);

    db.ref('.info/connected').on('value', snap => {
      setSyncStatus(!!snap.val(), snap.val() ? 'Live — synced with everyone' : 'Reconnecting…');
    });

    dbRef.on('value', snapshot => {
      qty = snapshot.val() || {};
      firebaseReady = true;
      refreshEverything();
    });
  } catch(e){
    setSyncStatus(false, 'Firebase error — check firebase-config.js');
    console.error(e);
  }
}

function setSyncStatus(on, label){
  const dot = document.getElementById('syncDot');
  const txt = document.getElementById('syncText');
  if(dot) dot.classList.toggle('on', on);
  if(txt) txt.textContent = label;
}

// ---------- build UI ----------
const teams = [];
const teamMap = {};
DATA.forEach(item => {
  if(!teamMap[item.team]){
    teamMap[item.team] = { name: item.team, items: [] };
    teams.push(teamMap[item.team]);
  }
  teamMap[item.team].items.push(item);
});

const app = document.getElementById('app');

function typeLabel(t){
  if(/logo/i.test(t)) return 'LOGO';
  if(/photo/i.test(t)) return 'TEAM PHOTO';
  if(/foil/i.test(t)) return 'FOIL';
  return '';
}

teams.forEach(team => {
  const det = document.createElement('details');
  det.className = 'team';
  det.dataset.team = team.name;
  det.open = false;

  const sum = document.createElement('summary');
  sum.innerHTML = `<span class="tname">${team.name}</span><span class="row-actions"><span class="tcount" data-tcount></span><span class="badge" data-tbadge></span></span>`;
  det.appendChild(sum);

  const rowsWrap = document.createElement('div');
  rowsWrap.className = 'rows';

  team.items.forEach(item => {
    const row = document.createElement('div');
    row.className = 'row';
    row.dataset.name = (item.name + ' ' + team.name).toLowerCase();

    const label = typeLabel(item.type);
    row.innerHTML = `
      <div class="num">${item.num}</div>
      <div class="name">${item.name}${label ? `<span class="type">${label}</span>` : ''}</div>
      <div class="qty">
        <button data-act="dec" aria-label="decrease">&minus;</button>
        <input type="text" inputmode="numeric" data-act="input" value="${getQty(item)}">
        <button data-act="inc" aria-label="increase">&plus;</button>
      </div>`;

    const input = row.querySelector('input');
    const dec = row.querySelector('[data-act=dec]');
    const inc = row.querySelector('[data-act=inc]');

    function refreshRow(){
      const v = getQty(item);
      if(document.activeElement !== input) input.value = v;
      row.classList.toggle('owned', v > 0);
    }

    row.addEventListener('click', (e) => {
      if(e.target === dec || e.target === inc) return;
      input.focus();
      input.select();
    });
    dec.addEventListener('click', (e) => { e.stopPropagation(); setQty(item, getQty(item) - 1); });
    inc.addEventListener('click', (e) => { e.stopPropagation(); setQty(item, getQty(item) + 1); });
    input.addEventListener('click', (e) => e.stopPropagation());
    input.addEventListener('input', () => {
      const v = parseInt(input.value.replace(/[^0-9]/g,''), 10);
      setQty(item, isNaN(v) ? 0 : v);
    });
    input.addEventListener('blur', () => { refreshRow(); applyFilter(); });

    row._item = item;
    row._refresh = refreshRow;
    rowsWrap.appendChild(row);
  });

  det.appendChild(rowsWrap);
  app.appendChild(det);
  det._team = team;
});

function refreshTeamBadge(det, team){
  const total = team.items.length;
  const owned = team.items.filter(i => getQty(i) > 0).length;
  det.querySelector('[data-tcount]').textContent = owned + '/' + total;
  const badge = det.querySelector('[data-tbadge]');
  if(owned === total){ badge.textContent = 'COMPLETE'; badge.classList.add('complete'); }
  else { badge.textContent = owned === 0 ? 'empty' : 'in progress'; badge.classList.remove('complete'); }
}

function updateStats(){
  let total = 0, unique = 0, dupes = 0, teamsComplete = 0;
  teams.forEach(team => {
    let teamOwned = 0;
    team.items.forEach(i => {
      const v = getQty(i);
      total += v;
      if(v > 0){ unique++; teamOwned++; dupes += (v - 1); }
    });
    if(teamOwned === team.items.length) teamsComplete++;
  });
  document.getElementById('statTotal').textContent = total;
  document.getElementById('statUnique').textContent = unique + ' / ' + DATA.length;
  document.getElementById('statDupes').textContent = dupes;
  document.getElementById('statTeams').textContent = teamsComplete + ' / ' + teams.length;
}

function refreshEverything(){
  document.querySelectorAll('.row').forEach(row => row._refresh());
  document.querySelectorAll('details.team').forEach(det => refreshTeamBadge(det, det._team));
  updateStats();
  applyFilter();
}

// ---------- search + filter ----------
const searchEl = document.getElementById('search');
const filterEl = document.getElementById('filter');

function applyFilter(){
  const q = searchEl.value.trim().toLowerCase();
  const mode = filterEl.value;
  document.querySelectorAll('details.team').forEach(det => {
    let anyVisible = false;
    det.querySelectorAll('.row').forEach(row => {
      const item = row._item;
      const v = getQty(item);
      let show = true;
      if(q && !row.dataset.name.includes(q)) show = false;
      if(mode === 'owned' && v === 0) show = false;
      if(mode === 'missing' && v > 0) show = false;
      if(mode === 'dupes' && v <= 1) show = false;
      row.classList.toggle('hidden', !show);
      if(show) anyVisible = true;
    });
    det.classList.toggle('hidden', !anyVisible);
    if(anyVisible && (q || mode !== 'all')) det.open = true;
  });
}
searchEl.addEventListener('input', applyFilter);
filterEl.addEventListener('change', applyFilter);

document.getElementById('expandAll').addEventListener('click', () => {
  document.querySelectorAll('details.team').forEach(d => d.open = true);
});
document.getElementById('collapseAll').addEventListener('click', () => {
  document.querySelectorAll('details.team').forEach(d => d.open = false);
});

// ---------- export / backup / restore / reset ----------
document.getElementById('exportBtn').addEventListener('click', () => {
  let csv = 'team,code,number,name,type,quantity\n';
  DATA.forEach(item => {
    const v = getQty(item);
    const esc = s => '"' + String(s).replace(/"/g,'""') + '"';
    csv += [esc(item.team), esc(item.code), item.num, esc(item.name), esc(item.type), v].join(',') + '\n';
  });
  downloadBlob(csv, 'wc26_' + COLLECTION_KEY + '_inventory.csv', 'text/csv');
  toast('CSV exported');
});

document.getElementById('backupBtn').addEventListener('click', () => {
  downloadBlob(JSON.stringify(qty, null, 2), 'wc26_' + COLLECTION_KEY + '_backup.json', 'application/json');
  toast('Backup downloaded');
});

document.getElementById('restoreBtn').addEventListener('click', () => {
  document.getElementById('restoreFile').click();
});
document.getElementById('restoreFile').addEventListener('change', (e) => {
  const file = e.target.files[0];
  if(!file) return;
  const reader = new FileReader();
  reader.onload = () => {
    try {
      const restored = JSON.parse(reader.result) || {};
      if(firebaseReady){
        dbRef.set(restored); // pushes to everyone
      } else {
        qty = restored;
        localStorage.setItem('wc26_local_' + COLLECTION_KEY, JSON.stringify(qty));
        refreshEverything();
      }
      toast('Backup restored');
    } catch(err) { toast('Could not read that file'); }
  };
  reader.readAsText(file);
});

document.getElementById('resetBtn').addEventListener('click', () => {
  if(confirm('Clear all recorded quantities for everyone? This cannot be undone (unless you have a backup).')){
    if(firebaseReady){
      dbRef.remove();
    } else {
      qty = {};
      localStorage.setItem('wc26_local_' + COLLECTION_KEY, JSON.stringify(qty));
      refreshEverything();
    }
    toast('Inventory cleared');
  }
});

function downloadBlob(content, filename, mime){
  const blob = new Blob([content], {type: mime});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url; a.download = filename;
  document.body.appendChild(a); a.click(); document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

let toastTimer;
function toast(msg){
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove('show'), 1800);
}

// ---------- go ----------
refreshEverything();
initFirebase();
