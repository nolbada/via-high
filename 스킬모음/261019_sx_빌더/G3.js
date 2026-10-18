
/* 문제 생성 로직 (순수 함수, DOM 없음). 브라우저(HTML 안에 삽입)와 node(sim.js) 양쪽에서 쓴다. */
(function (root) {
  'use strict';
  var G = {};
  G.SIZES = { ko: 6, mg: 4, mi: 6, abc: 6, blank: 8 };
  G.ABC_OPTS = ['ACB', 'BAC', 'BCA', 'CAB', 'CBA']; // 시험처럼 (A)(B)(C) 그대로인 순서는 없다
  var NEED = { ko: 'ko', mg: 'mun', mi: 'mun', abc: 'abc', blank: 'blank' };

  function rr(rnd) { return rnd || Math.random; }
  G.rint = function (n, rnd) { return Math.floor(rr(rnd)() * n); };
  G.shuffle = function (a, rnd) {
    a = a.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(rr(rnd)() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  };
  G.sample = function (a, k, rnd) { return G.shuffle(a, rnd).slice(0, k); };
  G.byId = function (D) { var m = {}; D.passages.forEach(function (p) { m[p.id] = p; }); return m; };

  /* ---------- 가능한 모양 ---------- */
  G.windows = function (ps) { // [a, k] : 주어진 첫 문장 a + 이어지는 k문장(3 또는 2), 그 사이 link가 모두 true
    var L = ps.link, n = ps.en.length, r = [], a, k, t, ok;
    for (a = 0; a < n - 1; a++) for (k = 3; k >= 2; k--) {
      if (a + k >= n) continue;
      ok = true; for (t = 0; t < k; t++) if (!L[a + t]) ok = false;
      if (ok) r.push([a, k]);
    }
    return r;
  };
  G.shapes = function (ps) { // ABC: [c0,c1,c2]
    var L = ps.link, n = ps.en.length, r = [];
    for (var c0 = 0; c0 <= n - 4; c0++) {
      if (!L[c0]) continue;
      for (var c1 = c0 + 1; c1 <= n - 3; c1++) {
        if (!L[c1]) continue;
        for (var c2 = c1 + 1; c2 <= n - 2; c2++) {
          if (!L[c2]) continue;
          var x = c1 - c0, y = c2 - c1, z = n - 1 - c2;
          if (Math.max(x, y, z) - Math.min(x, y, z) <= 1) r.push([c0, c1, c2]);
        }
      }
    }
    return r;
  };
  G.insList = function (ps) {
    var n = ps.en.length, L = ps.link;
    return (ps.ins || []).filter(function (j) {
      return j >= 1 && j <= n - 1 && L[j - 1] && (j >= n - 1 || L[j]);
    });
  };

  /* ---------- 카탈로그: 앱별 (지문, 문제 정체성) 목록 ---------- */
  G.catalog = function (D, app) {
    var need = NEED[app], out = [];
    D.passages.forEach(function (ps, pi) {
      if ((ps.modes || []).indexOf(need) < 0) return;
      var items = [], id = ps.id, g0 = ps.g0 || 0;
      if (app === 'ko' || app === 'mg') {
        G.windows(ps).forEach(function (w) { items.push({ id: id + '|' + app + '|' + w[0] + '|' + w[1], a: w[0], k: w[1], span: [g0 + w[0], g0 + w[0] + w[1]] }); });
      } else if (app === 'mi') {
        var n = ps.en.length, Lw = Math.min(n, 7);
        if (n >= 5) G.insList(ps).forEach(function (j) {
          var lo = Math.max(0, j - (Lw - 1)), hi = Math.min(j - 1, n - Lw);
          if (hi < lo) { lo = Math.max(0, Math.min(j - 1, n - Lw)); hi = lo; }
          for (var s = lo; s <= hi; s++) items.push({ id: id + '|mi|' + j + '|' + s, j: j, s: s, span: [g0 + s, g0 + s + Lw - 1] });
        });
      } else if (app === 'abc') {
        if (ps.en.length >= 7) G.shapes(ps).forEach(function (c) { items.push({ id: id + '|abc|' + c.join(','), c: c, span: [g0, g0 + ps.en.length - 1] }); });
      } else if (app === 'blank') {
        (ps.blanks || []).forEach(function (b, bi) {
          if (ps.en[b.s] && ps.en[b.s].indexOf(b.ans) >= 0 && b.opts && b.opts.length === 4)
            items.push({ id: id + '|blank|' + bi, bi: bi });
        });
      }
      if (items.length) out.push({ pi: pi, cls: ps.taught === true ? 'T' : 'U', items: items });
    });
    return out;
  };

  function wchoice(ws, rnd) {
    var t = 0, i; for (i = 0; i < ws.length; i++) t += ws[i];
    var r = rr(rnd)() * t;
    for (i = 0; i < ws.length; i++) { r -= ws[i]; if (r < 0) return i; }
    return ws.length - 1;
  }

  /* ---------- 한 판 계획: 약 2/3 수업에서 다룬 지문, 안 쓴 문제 우선 ---------- */
  G.planSet = function (entries, usedMap, n, rnd, prevPi, carry) {
    var used = {}, k;
    for (k in usedMap) used[k] = 1;
    var inSet = {}, setPis = {}, picks = [], reset = false, chosen = [], relax = false;
    var hasT = entries.some(function (e) { return e.cls === 'T'; });
    var hasU = entries.some(function (e) { return e.cls === 'U'; });
    var plan = [], i;
    if (hasT && hasU) {
      var nT = Math.round(n * 2 / 3);
      for (i = 0; i < n; i++) plan.push(i < nT ? 'T' : 'U');
      plan = G.shuffle(plan, rnd);
    } else for (i = 0; i < n; i++) plan.push(hasT ? 'T' : 'U');
    function avail(cls) {
      var r = [];
      entries.forEach(function (e) {
        if (cls && e.cls !== cls) return;
        var free = e.items.filter(function (it) { return !used[it.id] && !inSet[it.id] && (relax || !clash(it)); });
        if (free.length) r.push({ e: e, free: free });
      });
      return r;
    }
    function clash(it) {
      if (!it.span) return false;
      var len = it.span[1] - it.span[0] + 1, lim = Math.ceil(len / 2), q;
      for (q = 0; q < chosen.length; q++) {
        var ov = Math.min(it.span[1], chosen[q][1]) - Math.max(it.span[0], chosen[q][0]) + 1;
        if (ov >= lim) return true;
      }
      return false;
    }
    var prev = prevPi == null ? -1 : prevPi;
    for (k = 0; k < n; k++) {
      var cl = plan[k], oth = cl === 'T' ? 'U' : 'T';
      relax = false;
      var av = avail(cl);
      if (!av.length) av = avail(oth);
      if (!av.length) { relax = true; av = avail(cl); if (!av.length) av = avail(oth); }
      if (!av.length) { // 한 바퀴 끝: 직전에 쓴 문제(최대 carry*n개)는 계속 막고 나머지(가장 오래된 것)부터 다시 쓴다 -> 5판 안 겹침 유지
        var mine = {}; entries.forEach(function (e) { e.items.forEach(function (it) { mine[it.id] = 1; }); });
        var all = Object.keys(used), others = all.filter(function (x) { return !mine[x]; }), keys = all.filter(function (x) { return mine[x]; });
        var c = Math.min(keys.length, carry == null ? 0 : carry * n), need = n - k;
        reset = true;
        for (;;) {
          used = {}; others.forEach(function (x) { used[x] = 1; });
          keys.slice(keys.length - c).forEach(function (x) { used[x] = 1; });
          var tot = 0; avail(null).forEach(function (x) { tot += x.free.length; });
          if (tot >= need || c <= 0) break;
          c--;
        }
        av = avail(cl); if (!av.length) av = avail(oth);
      }
      if (!av.length) { // 가능한 모양이 한 판보다 적다: 어쩔 수 없이 겹침 허용
        av = entries.map(function (e) { return { e: e, free: e.items }; });
      }
      if (av.length > 1) {
        var f = av.filter(function (x) { return x.e.pi !== prev; });
        if (f.length) av = f;
      }
      var ws = av.map(function (x) { return Math.sqrt(x.free.length) * (setPis[x.e.pi] ? 0.35 : 1); });
      var ch = av[wchoice(ws, rnd)];
      var it = ch.free[G.rint(ch.free.length, rnd)];
      inSet[it.id] = 1; setPis[ch.e.pi] = 1; prev = ch.e.pi; if (it.span) chosen.push(it.span);
      picks.push({ pi: ch.e.pi, item: it });
    }
    picks.forEach(function (p) { used[p.item.id] = 1; });
    return { picks: picks, used: used, reset: reset };
  };

  /* ---------- 정답 번호 수열: 고르게, 연속 같은 번호 없이 ---------- */
  G.ansSeq = function (n, rnd) {
    var out = [], bag = [], last = -1;
    while (out.length < n) {
      if (!bag.length) bag = G.shuffle([1, 2, 3, 4, 5], rnd);
      var idx = -1;
      for (var i = bag.length - 1; i >= 0; i--) if (bag[i] !== last) { idx = i; break; }
      if (idx < 0) { bag = bag.concat(G.shuffle([1, 2, 3, 4, 5].filter(function (v) { return v !== last; }), rnd)); idx = bag.length - 1; }
      last = bag.splice(idx, 1)[0]; out.push(last);
    }
    return out;
  };

  /* ---------- 문제 만들기 ---------- */
  G.makeSeq = function (kind, ps, item, rnd) {
    var a = item.a, K = item.k || 3, idx = [], t = 0, pool, i;
    for (i = 1; i <= K; i++) idx.push(a + i);
    do { pool = G.shuffle(idx, rnd); t++; } while (t < 30 && pool.join() === idx.join());
    return { k: kind, pid: ps.id, a: a, K: K, pool: pool };
  };
  G.makeAbc = function (ps, item, ans) {
    return { k: 'abc', pid: ps.id, cuts: item.c.slice(), ans: ans };
  };
  G.abcParts = function (ps, p) { // 주어진 글 / 세 덩어리(문장 번호 목록) / 라벨
    var n = ps.en.length, c = p.cuts, order = G.ABC_OPTS[p.ans - 1], r = function (s, e) { var o = []; for (var i = s; i <= e; i++) o.push(i); return o; };
    var chunks = [r(c[0] + 1, c[1]), r(c[1] + 1, c[2]), r(c[2] + 1, n - 1)];
    var box = {}; // 라벨 → 덩어리 번호
    for (var k = 0; k < 3; k++) box[order[k]] = k;
    return { given: r(0, c[0]), chunks: chunks, order: order, box: box };
  };
  G.makeIns = function (ps, item, rnd, avoid) {
    var n = ps.en.length, j = item.j, L = Math.min(n, 7), s = item.s, rem = [], i;
    for (i = s; i < s + L; i++) if (i !== j) rem.push(i);
    var x = j - s; // 주어진 문장 앞에 오는 보여 주는 문장 수 = 정답 자리(rem[x-1] 뒤)
    var cand = [];
    for (i = 1; i <= rem.length; i++) if (i !== x) cand.push(i);
    var m = Math.min(4, cand.length), best = null, t;
    for (t = 0; t < 20; t++) {
      var pick = G.sample(cand, m, rnd).concat([x]).sort(function (p, q) { return p - q; });
      if (best === null) best = pick;
      if (pick.indexOf(x) + 1 !== avoid) { best = pick; break; }
    }
    return { k: 'mi', pid: ps.id, j: j, x: x, win: [s, s + L - 1], rem: rem, gaps: best };
  };
  G.makeBlank = function (ps, item, rnd, pos1) {
    var ord = G.shuffle([0, 1, 2, 3], rnd);
    return { k: 'blank', pid: ps.id, bi: item.bi, pos: pos1 - 1, ord: ord };
  };
  G.blankOpts = function (ps, p) { // 화면용 보기 5개 [{en,ko,ok}]
    var b = ps.blanks[p.bi], out = [], d = 0;
    for (var i = 0; i < 5; i++) {
      if (i === p.pos) out.push({ en: b.ans, ko: b.ans_ko, ok: true });
      else { var o = b.opts[p.ord[d++]]; out.push({ en: o.en, ko: o.ko, ok: false }); }
    }
    return out;
  };

  /* ---------- 한 판 만들기 ---------- */
  G.genSet = function (app, D, usedList, rnd) {
    var used = {}, probs = [], reset = false, P = G.byId(D);
    (usedList || []).forEach(function (x) { used[x] = 1; });
    var prevPi = null;
    function run(sub, n, fn) {
      var ent = G.catalog(D, sub);
      if (!ent.length || n <= 0) return;
      var pool = 0; ent.forEach(function (e) { pool += e.items.length; });
      var n0 = n;
      n = Math.min(n, Math.max(2, Math.floor(pool / 5))); // 5판 겹침 없음을 지킬 수 있게 풀이 작으면 한 판 문제 수를 줄인다
      var r = G.planSet(ent, used, n, rnd, prevPi, 4);
      used = r.used; reset = reset || (r.reset && pool >= 6 * n0); // 풀이 아주 작으면 매번 돌려 쓰므로 안내하지 않는다
      r.picks.forEach(function (pk, idx) { probs.push(fn(P[D.passages[pk.pi].id], pk.item, idx)); prevPi = pk.pi; });
    }
    var sz = G.SIZES, seq;
    if (app === 'ko') run('ko', sz.ko, function (ps, it) { return G.makeSeq('ko', ps, it, rnd); });
    else if (app === 'abc') {
      seq = G.ansSeq(sz.abc, rnd);
      run('abc', sz.abc, function (ps, it, i) { return G.makeAbc(ps, it, seq[i]); });
    } else if (app === 'blank') {
      seq = G.ansSeq(sz.blank, rnd);
      run('blank', sz.blank, function (ps, it, i) { return G.makeBlank(ps, it, rnd, seq[i]); });
    } else if (app === 'mun') {
      var prevAns = -1;
      run('mi', sz.mi, function (ps, it) { var p = G.makeIns(ps, it, rnd, prevAns); prevAns = p.gaps.indexOf(p.x) + 1; return p; });
    }
    return { probs: probs, used: Object.keys(used), reset: reset };
  };

  /* ---------- 순서도 재료 ---------- */
  G.flow = function (ps, idxs, givenSet) {
    return idxs.map(function (i) {
      return { ch: ps.key[i][0] || '', line: ps.key[i][1], g: !!(givenSet && givenSet[i]) };
    });
  };

  if (typeof module !== 'undefined' && module.exports) module.exports = G; else root.G = G;
})(typeof window !== 'undefined' ? window : this);