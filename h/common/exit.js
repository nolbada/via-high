/* 내신 테스트(exit test): 선생님 앞에서 푸는 한 번 제출 시험.
   - 범위(과·구간)와 문항 수(5/7/10/15)를 고르고, 같은 학교 폴더의 기존 문제 데이터에서 섞어 낸다.
   - 정답·해설은 제출 전까지 나오지 않고, 제출하면 점수·합격 여부·틀린 문제만 보여 준다.
   - 기존 활동 페이지(find / eobeop-test / awkward-test / sunseo-* / blank)는 읽기만 한다. 고치지 않는다.
   필요: parts.js(PARTS), sx.js(G·GM·SX), window.EXIT_CFG = {school, title, sub} */
(function () {
  'use strict';
  var CFG = window.EXIT_CFG || {};
  var SCHOOL = CFG.school || 'x';
  var KN = { L2: '2과', L3: '3과', L4: '4과', mock: '모의고사' };
  var TYPE_NAME = { find: 'TF', eob: '어법선택', awk: '어색한 곳', abc: 'ABC 순서', mun: '문장삽입', blank: '빈칸추론' };
  var WEIGHT = { find: 3, eob: 3, abc: 3, mun: 2, awk: 2, blank: 2 };
  var SXAPP = { abc: 'abc', mun: 'mun', blank: 'blank' };
  var SXSUB = { abc: 'abc', mun: 'mi', blank: 'blank' };
  var CIRC = '①②③④⑤⑥⑦⑧⑨⑩';
  var COUNTS = [5, 7, 10, 15];
  var K_SET = 'vhex:set:' + SCHOOL, K_CUR = 'vhex:cur:' + SCHOOL, K_USED = 'vhex:used:' + SCHOOL;

  function E(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function lsGet(k) { try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  function lsDel(k) { try { localStorage.removeItem(k); } catch (e) {} }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function strip(h) { var d = document.createElement('div'); d.innerHTML = h; return (d.textContent || '').replace(/\s+/g, ' ').trim(); }
  var root = document.getElementById('ex');

  /* ---------- 범위 ---------- */
  function kinds() { return ['L2', 'L3', 'L4', 'mock'].filter(function (k) { return window.PARTS && PARTS[k]; }); }
  function partNums(k) { return Object.keys(PARTS[k]).map(Number).sort(function (a, b) { return a - b; }); }
  function partName(k, p) { var n = PARTS.names && PARTS.names[k] && PARTS.names[k][p]; return n || ('구간 ' + p); }
  function inP(k, pid, part) { var l = PARTS[k] && PARTS[k][part]; return !!l && l.map(String).indexOf(String(pid)) >= 0; }
  function inAny(k, pid, parts) { return parts.some(function (p) { return inP(k, pid, p); }); }
  function firstPart(k, pids, parts) { for (var i = 0; i < parts.length; i++) for (var j = 0; j < pids.length; j++) if (inP(k, pids[j], parts[i])) return parts[i]; return parts[0]; }

  /* ---------- 데이터 읽기 (기존 페이지는 읽기만) ---------- */
  function scanJSON(txt, marker) {
    var i = txt.indexOf(marker); if (i < 0) return null;
    i += marker.length; while (/\s/.test(txt.charAt(i))) i++;
    var open = txt.charAt(i), close = open === '{' ? '}' : open === '[' ? ']' : null; if (!close) return null;
    var d = 0, inS = false, esc = false, j = i;
    for (; j < txt.length; j++) {
      var c = txt.charAt(j);
      if (inS) { if (esc) esc = false; else if (c === '\\') esc = true; else if (c === '"') inS = false; continue; }
      if (c === '"') { inS = true; continue; }
      if (c === open) d++; else if (c === close) { d--; if (d === 0) { j++; break; } }
    }
    try { return JSON.parse(txt.slice(i, j)); } catch (e) { return null; }
  }
  var tcache = {}, ucache = {};
  function getText(url) {
    if (!tcache[url]) tcache[url] = fetch(url).then(function (r) { if (!r.ok) throw 0; return r.text(); }).catch(function () { return null; });
    return tcache[url];
  }
  function loadUnit(k) {
    if (ucache[k]) return ucache[k];
    var none = Promise.resolve(null), act = k !== 'mock'; /* 모의고사 폴더에는 TF·어법·어색한 곳 페이지가 없다 */
    return ucache[k] = Promise.all([act ? getText(k + '/find.html') : none, act ? getText(k + '/eobeop-test.html') : none, act ? getText(k + '/awkward-test.html') : none, getText(k + '/sx-data.js')]).then(function (r) {
      var u = { kind: k };
      /* 구간 표기가 두 가지: 고1은 지문 번호 목록(FZ·EZ·AWKZ), 고2는 구간 번호(FP·AWKP)와 제목 기호(_m) */
      if (r[0]) {
        var D = scanJSON(r[0], 'var D='), FZ = scanJSON(r[0], 'var FZ='), FP = scanJSON(r[0], 'var FP=');
        if (D && D.groups && (FZ || FP)) u.find = { D: D, FZ: FZ, FP: FP };
      }
      if (r[1]) {
        var doc = new DOMParser().parseFromString(r[1], 'text/html'), EZ = scanJSON(r[1], 'var EZ='), tq = [].slice.call(doc.querySelectorAll('.tq'));
        if (!EZ) { /* 제목(.secd)의 ❶~❼ 기호로 지문을 알아낸다 */
          var mm = /var _m=\{([^}]*)\}/.exec(r[1]), map = {};
          if (mm) mm[1].replace(/'([^']+)'\s*:\s*'([^']+)'/g, function (a, b, c) { map[b] = c; return a; });
          var cur = null, zs = [];
          [].forEach.call(doc.querySelectorAll('.secd,.tq'), function (e) {
            if (e.classList.contains('secd')) { var x = /[❶-❼]/.exec(e.textContent); cur = x && map[x[0]] ? map[x[0]] : null; }
            else zs.push(cur);
          });
          EZ = zs.length === tq.length && mm ? zs : null;
        }
        if (tq.length && EZ) u.eob = { tq: tq, EZ: EZ };
      }
      if (r[2]) {
        var Q = scanJSON(r[2], 'var Q='), Z = scanJSON(r[2], 'var AWKZ='), AP = null;
        if (!Z) { var am = /var AWKP=\{([^}]*)\}/.exec(r[2]); if (am) { AP = {}; am[1].replace(/(\w+)\s*:\s*(\d+)/g, function (a, b, c) { AP[b] = +c; return a; }); } }
        if (Q && (Z || AP)) u.awk = { Q: Q, Z: Z, P: AP };
      }
      if (r[3]) { try { var DATA = (new Function(r[3] + ';return DATA;'))(); if (DATA && DATA.passages) u.sx = DATA; } catch (e) {} }
      return u;
    });
  }

  /* ---------- 문제 후보 ---------- */
  function sxCfg(app) {
    if (!sxCfg.c) sxCfg.c = {};
    if (sxCfg.c[app]) return sxCfg.c[app];
    var og = GM.run, cap = null;
    GM.run = function (c) { cap = c; };
    try { SX.apps[app]({ set: 'x', title: '', lesson: false, passages: [] }, { set: 'x' }); } finally { GM.run = og; }
    return sxCfg.c[app] = cap;
  }
  function sxDeck(u, parts) {
    var ps = u.sx.passages.filter(function (p) { return inAny(u.kind, p.id, parts); });
    return { set: u.sx.set, title: u.sx.title, lesson: u.sx.lesson, passages: ps };
  }
  function sxAvail(u, parts, app) {
    if (!u.sx || typeof G === 'undefined') return 0;
    var D = sxDeck(u, parts); if (!D.passages.length) return 0;
    try { return G.catalog(SX.prep(D, app), SXSUB[app]).length > 0 ? D.passages.length : 0; } catch (e) { return 0; }
  }
  function sxMake(u, parts, app, need, usedSx, seenAll) {
    var D = sxDeck(u, parts), key = u.kind + ':' + app, used = (usedSx[key] || []).slice(), out = [], guard = 0, seen = seenAll || {};
    var Dp = SX.prep(D, app), P = G.byId(Dp);
    /* 고른 구간이 서로 떨어져 있으면 그 사이를 건너뛰는 창(글 묶음)은 쓰지 않는다 */
    var zs = D._flat ? D._flat.zones : [], cut = [];
    D.passages.forEach(function (p, i) {
      if (i + 1 < D.passages.length && u.sx.passages.indexOf(D.passages[i + 1]) !== u.sx.passages.indexOf(p) + 1 && zs[i + 1]) cut.push(zs[i + 1].start);
    });
    function crosses(a, b) { return cut.some(function (c) { return c > a && c <= b; }); }
    function ckey(p) { return p.k === 'abc' ? 'abc|' + p.pid + '|' + p.cuts.join(',') : p.k === 'mi' ? 'mi|' + p.j : 'bl|' + p.pid + '|' + p.bi; }
    while (out.length < need && guard++ < 40) {
      var r = G.genSet(app, Dp, used, Math.random);
      used = r.used;
      r.probs.forEach(function (p) {
        if (cut.length) {
          var q0 = P[p.pid], g = q0 && q0.g0 != null ? q0.g0 : 0, e0 = p.k === 'abc' ? [g, g + q0.en.length - 1] : p.k === 'mi' ? p.win : null;
          if (e0 && crosses(e0[0], e0[1])) return;
        }
        var sig = u.kind + '/' + ckey(p); if (seen[sig] || out.length >= need) return; seen[sig] = 1;
        var ps = P[p.pid], c = {}; for (var k in ps) if (k !== 'base' && k !== '_flat') c[k] = ps[k];
        var pt = null; parts.forEach(function (x) { if (pt === null && inP(u.kind, p.pid, x)) pt = x; });
        out.push({ t: app, kind: u.kind, part: pt, p: p, ps: c });
      });
    }
    usedSx[key] = used;
    return out;
  }

  function buildExam(sel, N, units) {
    var used = lsGet(K_USED) || { ids: {}, sx: {} }; used.ids = used.ids || {}; used.sx = used.sx || {};
    var pools = { find: [], eob: [], awk: [] }, sxk = { abc: [], mun: [], blank: [] };
    kinds().forEach(function (k) {
      var parts = sel[k]; if (!parts || !parts.length) return; var u = units[k]; if (!u) return;
      if (u.find) u.find.D.groups.forEach(function (g, i) {
        var pt = null;
        if (g.items.length < 2 || !g.items.some(function (x) { return x.ans === 'F'; })) return; /* 다른 문장이 없는 묶음은 시험 문제가 못 된다 */
        if (u.find.FZ) { var z = u.find.FZ[i] || []; if (z.some(function (x) { return inAny(k, x, parts); })) pt = firstPart(k, z, parts); }
        else if (parts.indexOf(u.find.FP[i]) >= 0) pt = u.find.FP[i];
        if (pt !== null) pools.find.push({ id: k + ':find:' + i, t: 'find', kind: k, part: pt, g: g });
      });
      if (u.eob) u.eob.tq.forEach(function (q, i) {
        var z = u.eob.EZ[i]; if (z == null || !inAny(k, z, parts)) return;
        var sls = [].slice.call(q.querySelectorAll('.sl')); if (!sls.length) return;
        var ans = [].map.call(q.querySelectorAll('.bk'), function (b) { return +b.getAttribute('data-a'); });
        if (!ans.length) return;
        pools.eob.push({ id: k + ':eob:' + q.id, t: 'eob', kind: k, part: firstPart(k, [z], parts), html: sls.map(function (x) { return x.outerHTML; }).join(''), ans: ans });
      });
      if (u.awk) u.awk.Q.forEach(function (q) {
        var pt = null;
        if (u.awk.Z) { var z = u.awk.Z[q.id] || []; if (z.some(function (x) { return inAny(k, x, parts); })) pt = firstPart(k, z, parts); }
        else if (u.awk.P && parts.indexOf(u.awk.P[q.id]) >= 0) pt = u.awk.P[q.id];
        if (pt !== null) pools.awk.push({ id: k + ':awk:' + q.id, t: 'awk', kind: k, part: pt, q: q });
      });
      Object.keys(sxk).forEach(function (a) { var n = sxAvail(u, parts, a); if (n) sxk[a].push({ k: k, u: u, parts: parts, n: n }); });
    });
    var avail = {};
    ['find', 'eob', 'awk'].forEach(function (t) { avail[t] = pools[t].length; });
    Object.keys(sxk).forEach(function (a) { avail[a] = sxk[a].length ? 999 : 0; });
    var cnt = {}, left = N, types = Object.keys(avail).filter(function (t) { return avail[t] > 0; });
    types.forEach(function (t) { cnt[t] = 0; });
    var cap = Math.max(1, Math.ceil(N * 0.3)); /* 한 유형이 몰리지 않게: 다른 유형이 바닥나면 한도를 올린다 */
    while (left > 0) {
      var open = types.filter(function (t) { return cnt[t] < avail[t] && cnt[t] < cap; });
      if (!open.length) { if (types.some(function (t) { return cnt[t] < avail[t]; })) { cap++; continue; } break; }
      var tot = open.reduce(function (a, t) { return a + WEIGHT[t]; }, 0), r = Math.random() * tot, pick = open[0];
      for (var i = 0; i < open.length; i++) { r -= WEIGHT[open[i]]; if (r < 0) { pick = open[i]; break; } }
      cnt[pick]++; left--;
    }
    var picked = [], seenSx = {};
    ['find', 'eob', 'awk'].forEach(function (t) {
      if (!cnt[t]) return;
      var fresh = shuffle(pools[t].filter(function (c) { return !used.ids[c.id]; })), old = shuffle(pools[t].filter(function (c) { return used.ids[c.id]; }));
      fresh.concat(old).slice(0, cnt[t]).forEach(function (c) { picked.push(c); used.ids[c.id] = 1; });
    });
    Object.keys(sxk).forEach(function (a) {
      if (!cnt[a]) return;
      var per = {}, list = sxk[a], tw = list.reduce(function (s, x) { return s + x.n; }, 0);
      for (var n = 0; n < cnt[a]; n++) { var rr = Math.random() * tw, ch = list[0]; for (var j = 0; j < list.length; j++) { rr -= list[j].n; if (rr < 0) { ch = list[j]; break; } } per[ch.k] = (per[ch.k] || 0) + 1; }
      list.forEach(function (x) { if (per[x.k]) sxMake(x.u, x.parts, a, per[x.k], used.sx, seenSx).forEach(function (c) { picked.push(c); }); });
    });
    /* 모자라면(범위가 좁을 때) 남은 문제로 채운다 */
    if (picked.length < N) {
      var have = {}; picked.forEach(function (c) { if (c.id) have[c.id] = 1; });
      var rest = []; ['find', 'eob', 'awk'].forEach(function (t) { pools[t].forEach(function (c) { if (!have[c.id]) rest.push(c); }); });
      shuffle(rest).slice(0, N - picked.length).forEach(function (c) { picked.push(c); used.ids[c.id] = 1; });
    }
    for (var tr = 0; tr < 3 && picked.length < N; tr++) {
      Object.keys(sxk).forEach(function (a) {
        sxk[a].forEach(function (x) { if (picked.length < N) sxMake(x.u, x.parts, a, N - picked.length, used.sx, seenSx).forEach(function (c) { if (picked.length < N) picked.push(c); }); });
      });
    }
    lsSet(K_USED, used);
    return shuffle(picked).slice(0, N);
  }

  /* ---------- 문제 화면 ---------- */
  function ansInit(c) {
    if (c.t === 'find') return { sel: [] };
    if (c.t === 'eob') return { s: c.ans.map(function () { return -1; }) };
    if (c.t === 'awk') return { sel: [] };
    return sxCfg(SXAPP[c.t]).initSt();
  }
  function nFalse(c) { return c.g.items.filter(function (x) { return x.ans === 'F'; }).length; }
  function qHtml(c, st, i) {
    var h = '<div class="qh"><span class="qn">' + (i + 1) + '</span><span class="tg">' + TYPE_NAME[c.t] + '</span></div>';
    if (c.t === 'find') {
      h += '<div class="ask">본문과 <b>다른 문장 ' + nFalse(c) + '개</b>를 고르세요.</div><div class="fl">';
      c.g.items.forEach(function (it, n) { h += '<button type="button" class="fi' + (st.sel.indexOf(n) >= 0 ? ' sel' : '') + '" data-act="find" data-n="' + n + '"><b>' + (n + 1) + '</b> ' + E(it.en) + '</button>'; });
      return h + '</div>';
    }
    if (c.t === 'eob') {
      h += '<div class="ask">알맞은 쪽을 고르세요.</div><div class="eb">' + c.html + '</div>';
      return h;
    }
    if (c.t === 'awk') {
      var q = c.q, n = q.items.length;
      h += '<div class="ask">밑줄 친 곳 중 <b>' + (q.kind === 'ctx' ? '문맥상' : '어법상') + ' 어색한 것 ' + n + '개</b>를 고르세요.</div><div class="ps">';
      if (q.title) h += '<p class="ptitle">' + E(q.title) + '</p>';
      q.paras.forEach(function (p) {
        h += '<p>';
        p.forEach(function (s) {
          if (!s.c) h += E(s.t);
          else h += '<span class="cd' + (st.sel.indexOf(s.c) >= 0 ? ' sel' : '') + '" data-act="awk" data-c="' + s.c + '">' + E(s.t) + '<sup>' + CIRC.charAt(s.c - 1) + '</sup></span>';
        });
        h += '</p>';
      });
      return h + '</div>';
    }
    return h + '<div class="sxq">' + sxCfg(SXAPP[c.t]).view(c.p, st, c.ps, false) + '</div>';
  }
  function paintCard(i) {
    var c = EX.q[i], card = document.getElementById('q' + i);
    card.innerHTML = qHtml(c, EX.a[i], i);
    if (c.t === 'eob') {
      [].forEach.call(card.querySelectorAll('.bk'), function (bk, n) {
        var k = EX.a[i].s[n]; if (k >= 0) { var b = bk.querySelectorAll('button')[k]; if (b) b.classList.add('sel'); }
      });
    }
    if (c.t === 'blank' && EX.a[i].sel >= 0) { var b = card.querySelector('[data-act="o"][data-i="' + EX.a[i].sel + '"]'); if (b) b.classList.add('sel'); }
  }
  function answered(i) {
    var c = EX.q[i], st = EX.a[i];
    if (c.t === 'find') return st.sel.length > 0;
    if (c.t === 'eob') return st.s.every(function (k) { return k >= 0; });
    if (c.t === 'awk') return st.sel.length === c.q.items.length;
    if (c.t === 'abc') return st.sel > 0;
    return st.sel >= 0;
  }
  function nAnswered() { var n = 0; EX.q.forEach(function (c, i) { if (answered(i)) n++; }); return n; }

  /* ---------- 채점 ---------- */
  function isOk(i) {
    var c = EX.q[i], st = EX.a[i];
    if (c.t === 'find') {
      var f = []; c.g.items.forEach(function (it, n) { if (it.ans === 'F') f.push(n); });
      return st.sel.length === f.length && f.every(function (n) { return st.sel.indexOf(n) >= 0; });
    }
    if (c.t === 'eob') return c.ans.every(function (a, n) { return st.s[n] === a; });
    if (c.t === 'awk') {
      var T = c.q.items.map(function (x) { return x.c; });
      return st.sel.length === T.length && T.every(function (x) { return st.sel.indexOf(x) >= 0; });
    }
    var cfg = sxCfg(SXAPP[c.t]), s2 = JSON.parse(JSON.stringify(st)); if (c.t !== 'blank') s2.sub = 1;
    return !!cfg.ok(c.p, s2);
  }
  function answerText(i) { /* 틀린 문제에 보여 줄 정답 */
    var c = EX.q[i], o = [];
    if (c.t === 'find') c.g.items.forEach(function (it, n) { if (it.ans === 'F') o.push((n + 1) + '번 문장이 본문과 다름: ' + it.en + (it.eve ? ' (본문: ' + it.eve + ')' : '')); });
    else if (c.t === 'eob') {
      var d = document.createElement('div'); d.innerHTML = c.html;
      [].forEach.call(d.querySelectorAll('.bk'), function (bk, n) { var b = bk.querySelectorAll('button')[c.ans[n]]; bk.textContent = b ? b.textContent : ''; });
      o.push((d.textContent || '').replace(/\s+/g, ' ').trim());
    } else if (c.t === 'awk') c.q.items.forEach(function (it) { o.push(CIRC.charAt(it.c - 1) + ' ' + it.w + ' → ' + it.r); });
    else if (c.t === 'abc') { var ord = G.ABC_OPTS[c.p.ans - 1]; o.push('정답 ' + GM.CIR[c.p.ans - 1] + ' ' + ord.split('').map(function (x) { return '(' + x + ')'; }).join(' - ')); }
    else if (c.t === 'mun') { var right = c.p.gaps.indexOf(c.p.x); o.push('정답 ' + GM.CIR[right] + ' · 주어진 문장: ' + c.ps.en[c.p.j]); }
    else if (c.t === 'blank') { var b = c.ps.blanks[c.p.bi]; o.push('정답 ' + GM.CIR[c.p.pos] + ' ' + b.ans + ' · ' + c.ps.en[b.s]); }
    return o;
  }

  /* ---------- 화면 ---------- */
  var EX = null, UNITS = {}, SETUP = null;
  function head(extra) { return '<h1>' + E(CFG.title || '내신 테스트') + '</h1><p class="lede">' + E(CFG.sub || '') + '</p>' + (extra || ''); }
  function weekday(d) { return '일월화수목금토'.charAt(d.getDay()); }
  function stamp(ts) { var d = new Date(ts), p = function (n) { return (n < 10 ? '0' : '') + n; }; return (d.getMonth() + 1) + '/' + d.getDate() + '(' + weekday(d) + ') ' + p(d.getHours()) + ':' + p(d.getMinutes()); }

  function setupView() {
    var st = SETUP || lsGet(K_SET) || {}; SETUP = st;
    var ks = kinds(); st.sel = st.sel || {}; st.n = st.n || 10;
    var h = '<a class="homebtn" href="../exit/">← TEST 링크 모음</a>' + head();
    h += '<div class="exs"><div class="sh">풀코스 문제 풀기</div><div class="rn">범위</div>';
    ks.forEach(function (k) {
      var ps = partNums(k), cur = st.sel[k] || [], all = ps.length && ps.every(function (p) { return cur.indexOf(p) >= 0; });
      if (!document.getElementById('rgcss')) { var rs = document.createElement('style'); rs.id = 'rgcss'; rs.textContent = '#ex .rgh{margin:0 0 6px}#ex .rgb{border:0;background:transparent;color:var(--sub);font:inherit;font-weight:800;font-size:14px;padding:2px 2px;cursor:pointer}#ex .rgb.pk{color:var(--pri)}#ex .rgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(92px,1fr));gap:8px}#ex .rgrid.one{grid-template-columns:1fr}#ex .rgrid .ch{width:100%;padding:10px 4px;text-align:center;border-radius:12px}'; document.head.appendChild(rs); }
      h += '<div class="rg"><div class="rgh"><button type="button" class="rgb' + (all ? ' pk' : '') + '" data-act="all" data-k="' + k + '">' + KN[k] + '</button></div><div class="rgrid' + (k === 'mock' ? ' one' : '') + '">';
      ps.forEach(function (p) { h += '<button type="button" class="ch' + (cur.indexOf(p) >= 0 ? ' on' : '') + '" data-act="part" data-k="' + k + '" data-p="' + p + '">' + E(partName(k, p)) + '</button>'; });
      h += '</div></div>';
    });
    h += '<div class="sh">문항 수</div><div class="chips">';
    COUNTS.forEach(function (n) { h += '<button type="button" class="ch' + (st.n === n ? ' on' : '') + '" data-act="n" data-n="' + n + '">' + n + '문항</button>'; });
    var any = ks.some(function (k) { return (st.sel[k] || []).length; });
    h += '</div><button type="button" class="go" data-act="start"' + (any ? '' : ' disabled') + '>시험 시작</button></div>';
    var cur = lsGet(K_CUR);
    if (cur && cur.q && !cur.done) h += '<div class="resume">진행 중이던 시험이 있어요 (' + cur.q.length + '문항)<div class="rb"><button type="button" class="go2" data-act="resume">이어서 풀기</button></div></div>';
    root.innerHTML = h;
  }
  function testView() {
    var h = head() + '<div class="bar"><span id="cnt"></span><span class="sp"></span><button type="button" class="sub" data-act="submit">제출하기</button></div><div id="qs">';
    EX.q.forEach(function (c, i) { h += '<div class="exq" id="q' + i + '"></div>'; });
    h += '</div><button type="button" class="go fin" data-act="submit">제출하기</button>';
    root.innerHTML = h;
    EX.q.forEach(function (c, i) { paintCard(i); });
    updCount();
  }
  function updCount() {
    var n = nAnswered(), el = document.getElementById('cnt'); if (el) el.innerHTML = '답한 문제 <b>' + n + '</b> / ' + EX.q.length;
    [].forEach.call(document.querySelectorAll('[data-act="submit"]'), function (b) { b.textContent = EX.confirm ? '안 푼 문제 ' + (EX.q.length - n) + '개 · 그래도 제출' : '제출하기'; });
  }
  function resultView() {
    var N = EX.q.length, wrong = [], score = 0;
    EX.q.forEach(function (c, i) { if (isOk(i)) score++; else wrong.push(i); });
    var need = Math.ceil(N * 0.8), pass = score >= need;
    var h = head() + '<div class="exr ' + (pass ? 'pass' : 'fail') + '"><div class="vd">' + (pass ? '합격' : '불합격') + '</div><div class="sc"><b>' + score + '</b> / ' + N + '</div>' +
      '<div class="meta">합격 기준 ' + need + '문항 이상 · ' + stamp(EX.done) + '</div></div>';
    if (wrong.length) {
      h += '<div class="sh">틀린 문제 ' + wrong.length + '개</div>';
      wrong.forEach(function (i) {
        var c = EX.q[i];
        h += '<div class="wq"><div class="wh"><span class="qn">' + (i + 1) + '</span><span class="tg">' + TYPE_NAME[c.t] + '</span><span class="lb">' + KN[c.kind] + ' · ' + E(c.part ? partName(c.kind, c.part) : (c.ps && c.ps.label) || '') + '</span></div>';
        answerText(i).forEach(function (t) { h += '<div class="wa">' + E(t) + '</div>'; });
        h += '</div>';
      });
    } else h += '<p class="lede" style="text-align:center">전부 맞았어요.</p>';
    h += '<button type="button" class="go" data-act="again">새 시험</button>';
    h += '<a class="go homego" href="../exit/">메인으로 (TEST 링크 모음)</a>';
    root.innerHTML = h; window.scrollTo(0, 0);
  }

  function save() { if (EX) lsSet(K_CUR, EX); }
  function startExam() {
    var st = SETUP, sel = {}, need = [];
    kinds().forEach(function (k) { if ((st.sel[k] || []).length) { sel[k] = st.sel[k].slice().sort(function (a, b) { return a - b; }); need.push(k); } });
    lsSet(K_SET, st);
    root.querySelector('[data-act="start"]').textContent = '문제를 고르는 중';
    Promise.all(need.map(loadUnit)).then(function (us) {
      us.forEach(function (u) { UNITS[u.kind] = u; });
      var q = buildExam(sel, st.n, UNITS);
      if (!q.length) { root.querySelector('[data-act="start"]').textContent = '이 범위에는 문제가 없어요'; return; }
      EX = { q: q, a: q.map(ansInit), n: st.n, start: Date.now(), done: 0, confirm: 0 };
      save(); testView(); window.scrollTo(0, 0);
    });
  }
  function submitExam() {
    var n = nAnswered();
    if (n < EX.q.length && !EX.confirm) { EX.confirm = 1; updCount(); return; }
    EX.done = Date.now(); EX.confirm = 0; save(); resultView();
  }
  function hydrate(cur) { /* 새로고침 후 이어 풀기: sx 문제는 저장해 둔 지문으로 그린다 */
    EX = cur; testView();
  }

  root.addEventListener('click', function (e) {
    var t = e.target.closest('[data-act]');
    if (EX && !EX.done && !t) { /* 어법선택 보기 버튼은 data-act 가 없다 */
      var eb = e.target.closest('.bk button'), ecard = eb && eb.closest('.exq');
      if (eb && ecard) {
        var ei = +ecard.id.slice(1), est = EX.a[ei], ebk = eb.parentNode, ebks = [].slice.call(ecard.querySelectorAll('.bk'));
        EX.confirm = 0; est.s[ebks.indexOf(ebk)] = [].indexOf.call(ebk.querySelectorAll('button'), eb);
        paintCard(ei); updCount(); save();
      }
      return;
    }
    if (!t) return;
    var a = t.getAttribute('data-act');
    if (!EX || EX.done) { /* 설정 화면 */
      if (a === 'part') {
        var k = t.getAttribute('data-k'), p = +t.getAttribute('data-p'), cur = SETUP.sel[k] || [], i = cur.indexOf(p);
        if (i >= 0) cur.splice(i, 1); else cur.push(p); SETUP.sel[k] = cur; setupView();
      } else if (a === 'all') {
        var k2 = t.getAttribute('data-k'), ps = partNums(k2), cur2 = SETUP.sel[k2] || [], all = ps.every(function (p) { return cur2.indexOf(p) >= 0; });
        SETUP.sel[k2] = all ? [] : ps; setupView();
      } else if (a === 'n') { SETUP.n = +t.getAttribute('data-n'); setupView(); }
      else if (a === 'start') startExam();
      else if (a === 'resume') { var c = lsGet(K_CUR); if (c && c.q && !c.done) hydrate(c); }
      else if (a === 'again') { EX = null; lsDel(K_CUR); setupView(); window.scrollTo(0, 0); }
      return;
    }
    /* 시험 화면 */
    if (a === 'submit') { submitExam(); return; }
    var card = t.closest('.exq'); if (!card) return;
    var i2 = +card.id.slice(1), c2 = EX.q[i2], st2 = EX.a[i2]; EX.confirm = 0;
    if (c2.t === 'find') { var n = +t.getAttribute('data-n'), ix = st2.sel.indexOf(n); if (ix >= 0) st2.sel.splice(ix, 1); else st2.sel.push(n); }
    else if (c2.t === 'awk') {
      var cc = +t.getAttribute('data-c'), ix2 = st2.sel.indexOf(cc);
      if (ix2 >= 0) st2.sel.splice(ix2, 1); else { if (st2.sel.length >= c2.q.items.length) return; st2.sel.push(cc); }
    } else if (c2.t === 'eob') {
      return;
    } else {
      var el = e.target.closest('[data-act]'), act = el && el.getAttribute('data-act'); if (!act || act === 'sub') return;
      var cfg = sxCfg(SXAPP[c2.t]); if (c2.t === 'blank') st2.sel = -1;
      if (!cfg.act(act, el, c2.p, st2, c2.ps)) return;
    }
    paintCard(i2); updCount(); save();
  });

  /* ---------- 시작 ---------- */
  var cur0 = lsGet(K_CUR);
  if (!window.PARTS || typeof G === 'undefined') { root.innerHTML = '<p>화면을 불러오지 못했어요.</p>'; return; }
  if (cur0 && cur0.q && cur0.done) lsDel(K_CUR);
  setupView();
})();
