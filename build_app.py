import json

with open('checklist.json', encoding='utf-8') as f:
    data = json.load(f)

# Sanity
print(len(data))

data_json = json.dumps(data, ensure_ascii=False).replace('</script>', '<\\/script>')

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>2026 World Cup Sticker Inventory</title>
<style>
  :root{
    --bg:#0f1115; --panel:#171a21; --panel2:#1e222b; --border:#2a2f3a;
    --text:#e9ebef; --muted:#8b93a3; --accent:#3ea6ff; --green:#3ecf8e;
    --amber:#f5b642; --red:#ef5b5b;
  }
  *{box-sizing:border-box;}
  body{margin:0;background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;}
  header{position:sticky;top:0;z-index:20;background:rgba(15,17,21,0.97);backdrop-filter:blur(6px);border-bottom:1px solid var(--border);padding:14px 16px;}
  h1{font-size:17px;margin:0 0 10px 0;font-weight:650;}
  .stats{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:10px;}
  .stat{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:8px 12px;min-width:88px;}
  .stat .num{font-size:18px;font-weight:700;line-height:1.1;}
  .stat .lbl{font-size:11px;color:var(--muted);margin-top:2px;}
  .controls{display:flex;gap:8px;flex-wrap:wrap;align-items:center;}
  input[type=text], select{background:var(--panel2);border:1px solid var(--border);color:var(--text);border-radius:8px;padding:9px 10px;font-size:14px;}
  #search{flex:1;min-width:160px;}
  button{background:var(--panel2);border:1px solid var(--border);color:var(--text);border-radius:8px;padding:9px 12px;font-size:13px;cursor:pointer;}
  button:hover{border-color:var(--accent);}
  button.primary{background:var(--accent);border-color:var(--accent);color:#04121f;font-weight:600;}
  button.danger:hover{border-color:var(--red);}
  main{max-width:820px;margin:0 auto;padding:12px 12px 60px;}
  details.team{background:var(--panel);border:1px solid var(--border);border-radius:12px;margin-bottom:10px;overflow:hidden;}
  summary{list-style:none;cursor:pointer;padding:12px 14px;display:flex;align-items:center;justify-content:space-between;gap:10px;}
  summary::-webkit-details-marker{display:none;}
  summary .tname{font-weight:650;font-size:15px;}
  summary .tcount{font-size:12px;color:var(--muted);}
  summary .badge{font-size:11px;padding:3px 8px;border-radius:999px;background:var(--panel2);border:1px solid var(--border);color:var(--muted);}
  summary .badge.complete{background:rgba(62,207,142,0.15);border-color:var(--green);color:var(--green);}
  .rows{border-top:1px solid var(--border);}
  .row{display:flex;align-items:center;gap:10px;padding:9px 14px;border-bottom:1px solid var(--border);cursor:pointer;}
  .row:last-child{border-bottom:none;}
  .row:hover{background:var(--panel2);}
  .row.owned{background:rgba(62,207,142,0.06);}
  .num{width:28px;flex:none;font-size:12px;color:var(--muted);text-align:right;}
  .name{flex:1;min-width:0;font-size:14px;}
  .name .type{display:block;font-size:11px;color:var(--muted);margin-top:1px;}
  .qty{display:flex;align-items:center;gap:6px;flex:none;}
  .qty button{width:28px;height:28px;padding:0;font-size:16px;line-height:1;display:flex;align-items:center;justify-content:center;}
  .qty input{width:44px;text-align:center;background:var(--panel2);border:1px solid var(--border);color:var(--text);border-radius:6px;padding:5px 2px;font-size:14px;}
  .hidden{display:none !important;}
  footer{max-width:820px;margin:0 auto;padding:0 12px 40px;color:var(--muted);font-size:12px;line-height:1.6;}
  footer a{color:var(--accent);}
  #toast{position:fixed;bottom:16px;left:50%;transform:translateX(-50%);background:var(--panel2);border:1px solid var(--border);padding:8px 14px;border-radius:8px;font-size:13px;opacity:0;pointer-events:none;transition:opacity .2s;}
  #toast.show{opacity:1;}
  .row-actions{display:flex;gap:8px;}
  .fileimport{display:none;}
</style>
</head>
<body>

<header>
  <h1>2026 FIFA World Cup &mdash; Panini Sticker Inventory</h1>
  <div class="stats">
    <div class="stat"><div class="num" id="statTotal">0</div><div class="lbl">total stickers</div></div>
    <div class="stat"><div class="num" id="statUnique">0 / 980</div><div class="lbl">unique owned</div></div>
    <div class="stat"><div class="num" id="statDupes">0</div><div class="lbl">extras (sellable)</div></div>
    <div class="stat"><div class="num" id="statTeams">0 / 50</div><div class="lbl">sets complete</div></div>
  </div>
  <div class="controls">
    <input type="text" id="search" placeholder="Search player or team...">
    <select id="filter">
      <option value="all">Show all</option>
      <option value="owned">Owned only</option>
      <option value="missing">Missing only</option>
      <option value="dupes">Duplicates only</option>
    </select>
    <button id="expandAll">Expand all</button>
    <button id="collapseAll">Collapse all</button>
    <button id="exportBtn">Export CSV</button>
    <button id="backupBtn">Backup</button>
    <button id="restoreBtn">Restore</button>
    <input type="file" id="restoreFile" class="fileimport" accept="application/json">
    <button id="resetBtn" class="danger">Reset</button>
  </div>
</header>

<main id="app"></main>

<footer>
  Data auto-saves to this browser as you type &mdash; keep this file in the same place to keep your data.
  Use <strong>Backup</strong> occasionally to save a copy you can restore from later or on another device.
  Checklist sourced from the official 980-sticker 2026 Panini FIFA World Cup album structure.
</footer>

<div id="toast"></div>

<script>
const DATA = __DATA_JSON__;
const STORAGE_KEY = 'wc26_sticker_inventory_v1';

let qty = {};
try { qty = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}'); } catch(e) { qty = {}; }

function key(item){ return item.code + '-' + item.num; }
function getQty(item){ return qty[key(item)] || 0; }
function setQty(item, v){
  v = Math.max(0, Math.min(999, Math.floor(v) || 0));
  if(v === 0){ delete qty[key(item)]; } else { qty[key(item)] = v; }
  save();
}
function save(){
  localStorage.setItem(STORAGE_KEY, JSON.stringify(qty));
  updateStats();
}

// group by team, preserving original order
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
      input.value = v;
      row.classList.toggle('owned', v > 0);
    }

    row.addEventListener('click', (e) => {
      if(e.target === dec || e.target === inc) return;
      input.focus();
      input.select();
    });
    dec.addEventListener('click', (e) => { e.stopPropagation(); setQty(item, getQty(item) - 1); refreshRow(); refreshTeamBadge(det, team); applyFilter(); });
    inc.addEventListener('click', (e) => { e.stopPropagation(); setQty(item, getQty(item) + 1); refreshRow(); refreshTeamBadge(det, team); applyFilter(); });
    input.addEventListener('click', (e) => e.stopPropagation());
    input.addEventListener('input', () => {
      const v = parseInt(input.value.replace(/[^0-9]/g,''), 10);
      setQty(item, isNaN(v) ? 0 : v);
      row.classList.toggle('owned', getQty(item) > 0);
      refreshTeamBadge(det, team);
    });
    input.addEventListener('blur', () => { refreshRow(); applyFilter(); });

    row._item = item;
    row._refresh = refreshRow;
    rowsWrap.appendChild(row);
  });

  det.appendChild(rowsWrap);
  app.appendChild(det);
  refreshTeamBadge(det, team);
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
updateStats();

// search + filter
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

// export CSV
document.getElementById('exportBtn').addEventListener('click', () => {
  let csv = 'team,code,number,name,type,quantity\\n';
  DATA.forEach(item => {
    const v = getQty(item);
    const esc = s => '"' + String(s).replace(/"/g,'""') + '"';
    csv += [esc(item.team), esc(item.code), item.num, esc(item.name), esc(item.type), v].join(',') + '\\n';
  });
  downloadBlob(csv, 'wc26_sticker_inventory.csv', 'text/csv');
  toast('CSV exported');
});

document.getElementById('backupBtn').addEventListener('click', () => {
  downloadBlob(JSON.stringify(qty, null, 2), 'wc26_sticker_backup.json', 'application/json');
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
      const restored = JSON.parse(reader.result);
      qty = restored || {};
      save();
      document.querySelectorAll('.row').forEach(row => row._refresh());
      document.querySelectorAll('details.team').forEach((det, i) => refreshTeamBadge(det, teams[i]));
      toast('Backup restored');
    } catch(err) { toast('Could not read that file'); }
  };
  reader.readAsText(file);
});

document.getElementById('resetBtn').addEventListener('click', () => {
  if(confirm('Clear all recorded quantities? This cannot be undone (unless you have a backup).')){
    qty = {};
    save();
    document.querySelectorAll('.row').forEach(row => row._refresh());
    document.querySelectorAll('details.team').forEach((det, i) => refreshTeamBadge(det, teams[i]));
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
</script>
</body>
</html>
"""

html = html.replace('__DATA_JSON__', data_json)

with open('wc26_sticker_inventory.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('written', len(html), 'bytes')
