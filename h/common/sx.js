
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
/* ===== 브라우저 공통: 저장, 러너(한 문제씩 → 제출/확인 → 다음), 화면 조각, 설명(앞뒤 흐름 + 단서) ===== */
var GM = {};
GM.esc = function (s) { return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); };
GM.endp = function (s) { return /[.?!]["”’')]*$/.test(s) ? s : s + '.'; };
GM.ls = {
  get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
  set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
  del: function (k) { try { localStorage.removeItem(k); } catch (e) {} }
};
GM.CIR = ['①', '②', '③', '④', '⑤'];
/* 한글 문장 속 (English 표어)는 파랗게 */
GM.kline = function (s) {
  return GM.esc(s).replace(/\(([^()]*[A-Za-z][^()]*)\)/g, '(<span class="en">$1</span>)');
};
/* "However(그러나)" → 영어는 파랗게, 뜻은 괄호 그대로 */
GM.chip = function (k0) {
  if (!k0) return '';
  var m = /^(.*?)\s*(\([^)]*\))$/.exec(k0);
  if (m) return '<span class="cc"><span class="en">' + GM.esc(m[1]) + '</span>' + GM.esc(m[2]) + '</span>';
  return '<span class="cc"><span class="en">' + GM.esc(k0) + '</span></span>';
};
GM.conn = function (k0) {
  if (!k0) return '';
  var m = /^(.*?)\s*(\([^)]*\))$/.exec(k0);
  if (m) return '<span class="en">' + GM.esc(m[1]) + '</span>' + GM.esc(m[2]) + ', ';
  return '<span class="en">' + GM.esc(k0) + '</span>, ';
};
GM.num = function (ps, i) { return ps.nums && ps.nums[i] != null ? ps.nums[i] : i + 1; };

/* ---- 전체 흐름 속 내 위치 ----
 o: {from,to: 노란 박스로 감쌀 문장 범위(이 문제 글 기준), mark: 강조할 문장, markLab, tags: {문장idx:'(A)'}, cap, title}
 단원이면 ps.base(단원 전체 이어 붙인 글)·ps.g0(시작 위치)로 앞뒤 구역까지 보여 준다 */
GM.ctx = function (D, ps, o) {
  o = o || {};
  var B = ps.base || ps, g0 = ps.g0 || 0, from = g0 + o.from, to = g0 + o.to, mark = o.mark == null ? null : g0 + o.mark;
  var zones = B.zones || [{ start: 0, len: ps.en.length, label: ps.label, gist: ps.gist }];
  var h = '<div class="ctx"><div class="wd">' + GM.esc(o.title || '전체 흐름 속 내 위치') + '</div>';
  zones.forEach(function (z) {
    var z0 = z.start, z1 = z.start + z.len - 1;
    if (z1 < from || z0 > to) {
      h += '<div class="zc"><span class="zt">' + (z1 < from ? '앞 내용' : '뒷 내용') + '</span><b>' + GM.esc(z.label) + '</b>' + (z.gist ? ' · ' + GM.kline(z.gist) : '') + '</div>';
      return;
    }
    h += '<div class="zx"><div class="zh"><b>' + GM.esc(z.label) + '</b>' + (z.gist ? '<span class="zg">' + GM.kline(z.gist) + '</span>' : '') + '</div>';
    var inbox = false, i;
    for (i = z0; i <= z1; i++) {
      var inr = i >= from && i <= to;
      if (inr && !inbox) { h += '<div class="hlbox"><div class="hlt">' + GM.esc(o.cap || '지금 푼 부분') + '</div>'; inbox = true; }
      if (!inr && inbox) { h += '</div>'; inbox = false; }
      var mk = mark === i, tg = o.tags && o.tags[i - g0];
      h += '<div class="cr' + (mk ? ' mk1' : '') + '"><span class="cn">' + (B.nums && B.nums[i] != null ? B.nums[i] : i + 1) + '</span><div class="cb">' +
        (tg ? '<span class="tgl">' + GM.esc(tg) + '</span>' : '') + (mk && o.markLab ? '<span class="tgl y">' + GM.esc(o.markLab) + '</span>' : '') +
        GM.chip(B.key[i][0]) + '<span class="cl">' + GM.kline(B.key[i][1]) + '</span></div></div>';
    }
    if (inbox) h += '</div>';
    h += '</div>';
  });
  return h + '</div>';
};
/* ---- 왜 이 순서/자리인가: 단서 목록 ---- items: [{lab, i}] i = "i번 문장이 바로 앞과 이어지는 이유" ---- */
GM.why = function (ps, items, title) {
  var h = '<div class="why"><div class="wd">' + GM.esc(title) + '</div><ol class="chain">';
  items.forEach(function (it) {
    var t = ps.why && ps.why[it.i];
    if (!t) { var k = ps.key[it.i]; t = (k[0] ? k[0] + ' ' : '') + k[1]; }
    h += '<li><span class="jl">' + GM.esc(it.lab) + '</span><span class="jt">' + GM.kline(t) + '</span></li>';
  });
  return h + '</ol></div>';
};

GM.badge = function (ps) {
  if (ps.taught === true) return '<span class="bd t">수업에서 다룬 지문</span>';
  if (ps.taught === false) return '<span class="bd u">수업에서 다루지 않은 지문</span>';
  return '';
};
GM.mockInfo = function (D) {
  var any = D.passages.some(function (p) { return p.taught === true || p.taught === false; });
  if (!any) return '';
  return '<div class="mi2"><div><span class="bd t">수업에서 다룬 지문</span>중간고사에서 문항의 약 2/3(63%)가 수업에서 다룬 지문에서 나왔어요. 꼭 익숙해지세요.</div>' +
    '<div><span class="bd u">수업에서 다루지 않은 지문</span>대의 파악, 순서, 삽입, 무관한 문장, 요약문 유형으로 나오니 그 유형을 염두에 두고 읽어요.</div></div>';
};

/* ---- 러너 ---- */
GM.run = function (cfg) {
  var D = cfg.D, P = G.byId(D), run = null;
  var KR = 'sx-res:' + location.pathname.replace(/[^a-z0-9]/gi, '');
  var UK = 'sx-used:' + cfg.set + ':' + cfg.gen;
  var stage = document.getElementById('stage'), cnt = document.getElementById('cnt');
  function usedList() { try { var a = JSON.parse(GM.ls.get(UK)); return Array.isArray(a) ? a : []; } catch (e) { return []; } }
  function save() { GM.ls.set(KR, JSON.stringify(run)); }
  function newRun() {
    var r = G.genSet(cfg.gen, D, usedList(), Math.random);
    GM.ls.set(UK, JSON.stringify(r.used));
    run = { v: 2, probs: r.probs, st: r.probs.map(cfg.initSt), cur: 0, fin: false, reset: r.reset };
    save(); render(); window.scrollTo(0, 0);
  }
  function restore() {
    try {
      var o = JSON.parse(GM.ls.get(KR));
      if (!o || o.v !== 2 || !o.probs || !o.probs.length || o.probs.length !== o.st.length) return false;
      for (var i = 0; i < o.probs.length; i++) if (!P[o.probs[i].pid]) return false;
      run = o; return true;
    } catch (e) { return false; }
  }
  function nOk() { var n = 0; run.probs.forEach(function (p, i) { if (cfg.done(p, run.st[i]) && cfg.ok(p, run.st[i])) n++; }); return n; }
  function anyDone() { return run.probs.some(function (p, i) { return cfg.done(p, run.st[i]); }); }
  function render() {
    var N = run.probs.length, h = '';
    if (run.fin) {
      var m = nOk();
      h = '<div class="sum"><h3>' + N + '문제 중 ' + m + '개</h3><p>' + (cfg.sumNote || '맞힌 문제') + '</p><div class="chips">' +
        run.probs.map(function (p, i) { var o = cfg.ok(p, run.st[i]); return '<span class="' + (o ? 'o' : 'x') + '">' + (i + 1) + (o ? ' ○' : ' ×') + '</span>'; }).join('') +
        '</div><button class="nx" type="button" data-act="again">새 문제로 다시 풀기</button><a class="nx sub" href="../index.html">← 목록</a></div>';
      stage.innerHTML = h; cnt.innerHTML = '<b>' + N + '</b>문제 중 <b>' + m + '</b>개';
      if (!run.hw && cfg.hw) { run.hw = 1; save(); try { GK.hw(cfg.hw); } catch (e) {} }
      return;
    }
    var i = run.cur, p = run.probs[i], st = run.st[i], ps = P[p.pid], done = cfg.done(p, st);
    if (run.reset && i === 0) h += '<div class="notice">준비된 문제를 한 바퀴 모두 풀었어요. 처음부터 다시 섞어서 시작해요.</div>';
    h += '<div class="q' + (done ? ' done' : '') + '"><div class="qh"><span class="qn">' + (i + 1) + '</span><span class="tg">' + GM.esc(cfg.tag(p)) + '</span>' +
      GM.badge(ps) + '<span class="lb">' + GM.esc(ps.label) + '</span></div>' + cfg.view(p, st, ps, done);
    if (done) h += '<button class="nx" type="button" data-act="next">' + (i + 1 < N ? '다음 문제' : '결과 보기') + '</button>';
    h += '</div>';
    stage.innerHTML = h;
    cnt.innerHTML = '문제 <b>' + (i + 1) + '</b> / ' + N + ' · 맞힌 문제 <b>' + nOk() + '</b>';
  }
  stage.addEventListener('click', function (e) {
    var s = e.target.closest && e.target.closest('.sent');
    if (s && !s.classList.contains('blk')) { s.classList.toggle('open'); return; }
    var t = e.target.closest && e.target.closest('[data-act]');
    if (!t || !run) return;
    var a = t.getAttribute('data-act');
    if (a === 'again') { newRun(); return; }
    if (a === 'next') { if (run.cur + 1 < run.probs.length) run.cur++; else run.fin = true; save(); render(); stage.scrollIntoView(); return; }
    var i = run.cur, p = run.probs[i];
    if (cfg.act(a, t, p, run.st[i], P[p.pid])) { save(); render(); }
  });
  var rs = document.getElementById('rs');
  rs.addEventListener('click', function () {
    if (run && !run.fin && anyDone() && !confirm('지금까지 푼 기록이 사라지고 새 문제가 나와요. 새로 시작할까요?')) return;
    newRun();
  });
  var kt = document.getElementById('kt');
  function setK(v) {
    document.body.classList.toggle('kon', v);
    if (kt) kt.textContent = v ? '한글 해석 닫기' : '한글 해석 보기';
    GM.ls.set('gk-blank-kr', v ? '1' : '0');
  }
  if (cfg.kr) { setK(GM.ls.get('gk-blank-kr') === '1'); kt.addEventListener('click', function () { setK(!document.body.classList.contains('kon')); }); }
  else if (kt) kt.style.display = 'none';
  if (!restore()) newRun(); else render();
  window.__gm = { run: function () { return run; }, newRun: newRun };
};

/* ---- 한글 순서배열(ko) ---- */
GM.seqText = function (ps, i) {
  return GM.conn(ps.key[i][0]) + GM.esc((ps.kox && ps.kox[i]) || ps.ko[i]);
};
GM.seqInit = function () { return { pk: [], sub: 0 }; };
GM.seqDone = function (p, st) { return !!st.sub; };
GM.seqOk = function (p, st) { return !!st.sub && st.pk.length === p.K && st.pk.every(function (x, k) { return x === p.a + 1 + k; }); };
GM.seqView = function (D, p, st, ps, done) {
  var a = p.a, K = p.K, h = '<div class="ask">맨 위 문장 다음에 이어질 순서대로 <b>한글 문장 ' + K + '개</b>를 눌러 쌓은 뒤 제출해요.</div>';
  h += '<div class="gv"><span class="tg2">주어진 문장</span>' + GM.seqText(ps, a) + '</div><div class="slots">';
  var good = 0, k;
  for (k = 0; k < K; k++) {
    var idx = st.pk[k];
    if (idx == null) h += '<div class="slot"><span class="no">' + (k + 1) + '</span><span>비어 있어요</span></div>';
    else {
      var o = idx === a + 1 + k; if (o) good++;
      h += '<button type="button" class="slot f' + (done ? (o ? ' o' : ' n') : '') + '" data-act="slot" data-k="' + k + '"><span class="no">' + (k + 1) + '</span><span>' + GM.seqText(ps, idx) + '</span>' +
        (done ? '<span class="ox ' + (o ? 'o">○' : 'n">×') + '</span>' : '<span class="x">빼기</span>') + '</button>';
    }
  }
  h += '</div>';
  if (!done) {
    h += '<div class="pool"><div class="lbl">이어질 순서대로 문장을 누르세요' + (st.pk.length < K ? ' (' + (st.pk.length + 1) + '번째)' : '') + '</div>';
    p.pool.forEach(function (i) { if (st.pk.indexOf(i) < 0) h += '<button type="button" class="pb" data-act="pick" data-n="' + i + '">' + GM.seqText(ps, i) + '</button>'; });
    h += '</div><button type="button" class="sb" data-act="sub"' + (st.pk.length < K ? ' disabled' : '') + '>제출하기</button>';
  } else {
    h += '<div class="res ' + (good === K ? 'o' : 'x') + '">' + K + '자리 중 ' + good + '자리가 맞아요.</div>';
    var labs = ['주어진 문장 → 첫째', '첫째 → 둘째', '둘째 → 셋째'], items = [];
    for (k = 0; k < K; k++) items.push({ lab: labs[k], i: a + 1 + k });
    h += GM.why(ps, items, '왜 이 순서일까요? 이어지는 단서');
    h += GM.ctx(D, ps, { from: a, to: a + K, mark: a, markLab: '주어진 문장', cap: '지금 푼 부분 (주어진 문장 + 이어진 ' + K + '문장)' });
  }
  return h;
};
GM.seqAct = function (act, el, p, st) {
  if (st.sub) return false;
  if (act === 'pick') { if (st.pk.length >= p.K) return false; st.pk.push(+el.getAttribute('data-n')); return true; }
  if (act === 'slot') { st.pk.splice(+el.getAttribute('data-k'), 1); return true; }
  if (act === 'sub') { if (st.pk.length < p.K) return false; st.sub = 1; return true; }
  return false;
};

/* ---- 앱 ---- */
var SX = { apps: {} };
/* 교과서 단원(lesson)은 구역들을 한 글로 이어 붙여 출제한다: ko·삽입은 이어 붙인 글 전체에서, ABC는 7~10문장 창을 미끄러뜨려, 빈칸은 구역 단위로.
   해설의 '전체 흐름'은 이어 붙인 글(base)과 시작 위치(g0)로 그린다. */
SX.prep = function (D, app) {
  if (!D.lesson) return D;
  if (!D._flat) {
    var f = { id: 'flat', label: D.title, taught: null, en: [], ko: [], key: [], why: [], nums: [], link: [], ins: [], blanks: [], zones: [], modes: ['ko', 'mun'] }, off = 0;
    D.passages.forEach(function (p) {
      var n = p.en.length, i;
      f.zones.push({ start: off, len: n, label: p.label, gist: p.gist });
      for (i = 0; i < n; i++) { f.en.push(p.en[i]); f.ko.push(p.ko[i]); f.key.push(p.key[i]); f.why.push(p.why[i]); f.nums.push(p.nums ? p.nums[i] : off + i + 1); }
      for (i = 0; i < n - 1; i++) f.link.push(!!p.link[i]);
      f.link.push(false);
      (p.ins || []).forEach(function (j) { f.ins.push(off + j); });
      p.g0 = off; p.base = f; off += n;
    });
    f.link.pop();
    D._flat = f;
  }
  var f2 = D._flat;
  if (app === 'ko' || app === 'mun') return { set: D.set, title: D.title, lesson: true, passages: [f2] };
  if (app === 'abc') {
    var ws = [], N = f2.en.length, ln, s;
    function zl(i) { var r = ''; f2.zones.forEach(function (z) { if (i >= z.start && i < z.start + z.len) r = z.label; }); return r; }
    for (ln = 7; ln <= 10; ln++) for (s = 0; s + ln <= N; s++) {
      var a = zl(s), b = zl(s + ln - 1);
      ws.push({ id: 'w' + s + '_' + ln, label: a === b ? a : a + ' ~ ' + b, taught: null, modes: ['abc'], g0: s, base: f2,
        en: f2.en.slice(s, s + ln), ko: f2.ko.slice(s, s + ln), key: f2.key.slice(s, s + ln), why: f2.why.slice(s, s + ln),
        nums: f2.nums.slice(s, s + ln), link: f2.link.slice(s, s + ln - 1), ins: [], blanks: [] });
    }
    return { set: D.set, title: D.title, lesson: true, passages: ws };
  }
  return D;
};
SX.start = function (app, D, opt) {
  document.getElementById('mockinfo').innerHTML = GM.mockInfo(D);
  SX.apps[app](SX.prep(D, app), opt || {});
};

SX.apps.ko = function (D, o) {
  GM.run({ D: D, set: o.set, gen: 'ko', kr: false, hw: o.hw,
    tag: function () { return '한글 순서배열'; },
    initSt: GM.seqInit, done: GM.seqDone, ok: GM.seqOk,
    view: function (p, st, ps, done) { return GM.seqView(D, p, st, ps, done); },
    act: GM.seqAct });
};

SX.apps.abc = function (D, o) {
  function seqs(ps, idxs) { return idxs.map(function (i) { return '<span class="s2">' + GM.esc(ps.en[i]) + '<small class="kr">' + GM.esc(ps.ko[i]) + '</small></span> '; }).join(''); }
  GM.run({ D: D, set: o.set, gen: 'abc', kr: true, hw: o.hw,
    tag: function () { return 'ABC 순서'; },
    initSt: function () { return { sel: 0, sub: 0 }; },
    done: function (p, st) { return !!st.sub; },
    ok: function (p, st) { return !!st.sub && st.sel === p.ans; },
    view: function (p, st, ps, done) {
      var P = G.abcParts(ps, p), h = '<div class="ask">주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?</div>';
      h += '<div class="pbox given"><span class="lab">주어진 글</span>' + seqs(ps, P.given) + '</div>';
      ['A', 'B', 'C'].forEach(function (L) { h += '<div class="pbox"><span class="lab">(' + L + ')</span>' + seqs(ps, P.chunks[P.box[L]]) + '</div>'; });
      G.ABC_OPTS.forEach(function (op, k) {
        var c = 'ob'; if (done) { if (k + 1 === p.ans) c += ' ok'; else if (k + 1 === st.sel) c += ' ng'; } else if (st.sel === k + 1) c += ' sel';
        h += '<button type="button" class="' + c + '" data-act="o" data-n="' + (k + 1) + '"><b class="cn">' + GM.CIR[k] + '</b> ' + op.split('').map(function (x) { return '(' + x + ')'; }).join(' - ') + '</button>';
      });
      if (!done) return h + '<button type="button" class="sb" data-act="sub"' + (st.sel ? '' : ' disabled') + '>제출하기</button>';
      var ok = st.sel === p.ans, ord = P.order.split('');
      h += '<div class="res ' + (ok ? 'o' : 'x') + '">' + (ok ? '정답이에요.' : '아쉬워요. 정답은 ' + GM.CIR[p.ans - 1] + ' ' + ord.map(function (x) { return '(' + x + ')'; }).join(' - ') + ' 이에요.') + '</div>';
      var items = [], prev = '주어진 글', k;
      for (k = 0; k < 3; k++) {
        items.push({ lab: prev + ' → (' + ord[k] + ')', i: P.chunks[k][0] });
        prev = '(' + ord[k] + ')';
      }
      h += GM.why(ps, items, '왜 이 순서일까요? 이어지는 단서');
      var tags = {}; tags[0] = '주어진 글';
      for (k = 0; k < 3; k++) tags[P.chunks[k][0]] = '(' + ord[k] + ')';
      h += GM.ctx(D, ps, { from: 0, to: ps.en.length - 1, tags: tags, cap: '지금 푼 글 전체 (정답 순서대로)' });
      return h;
    },
    act: function (a, el, p, st) {
      if (st.sub) return false;
      if (a === 'o') { st.sel = +el.getAttribute('data-n'); return true; }
      if (a === 'sub' && st.sel) { st.sub = 1; return true; }
      return false;
    } });
};

SX.apps.mun = function (D, o) {
  GM.run({ D: D, set: o.set, gen: 'mun', kr: true, hw: o.hw,
    tag: function () { return '문장 삽입'; },
    initSt: function () { return { sel: -1, sub: 0 }; },
    done: function (p, st) { return !!st.sub; },
    ok: function (p, st) { return !!st.sub && p.gaps[st.sel] === p.x; },
    view: function (p, st, ps, done) {
      var rem = p.rem, right = p.gaps.indexOf(p.x), i, h;
      function mk(k) {
        var c = 'mk'; if (done) { if (k === right) c += ' ok'; else if (k === st.sel) c += ' ng'; } else if (st.sel === k) c += ' sel';
        return '<button type="button" class="' + c + '" data-act="mk" data-k="' + k + '">' + GM.CIR[k] + '</button>';
      }
      h = '<div class="ask">글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳을 고르세요.</div>';
      h += '<div class="gv"><span class="tg2">주어진 문장</span>' + GM.esc(ps.en[p.j]) + '<small class="kr">' + GM.esc(ps.ko[p.j]) + '</small></div><div class="pbox">';
      for (i = 0; i < rem.length; i++) {
        h += GM.esc(ps.en[rem[i]]) + ' ';
        var gk = p.gaps.indexOf(i + 1); if (gk >= 0) h += mk(gk) + ' ';
      }
      h += '<div class="pko">' + rem.map(function (x) { return '<div>' + GM.esc(ps.ko[x]) + '</div>'; }).join('') + '</div></div>';
      if (!done) return h + '<button type="button" class="sb" data-act="sub"' + (st.sel >= 0 ? '' : ' disabled') + '>제출하기</button>';
      var ok = p.gaps[st.sel] === p.x;
      h += '<div class="res ' + (ok ? 'o' : 'x') + '">' + (ok ? '정답이에요.' : '아쉬워요. 정답은 ' + GM.CIR[right] + '이에요.') + '</div>';
      var items = [{ lab: '앞 문장과 (' + GM.CIR[right] + ' 바로 앞)', i: p.j }];
      if (p.j + 1 < ps.en.length) items.push({ lab: '뒤 문장과 (' + GM.CIR[right] + ' 바로 뒤)', i: p.j + 1 });
      h += GM.why(ps, items, '왜 ' + GM.CIR[right] + '번 자리일까요? 단서');
      h += GM.ctx(D, ps, { from: p.win[0], to: p.win[1], mark: p.j, markLab: '주어진 문장', cap: '지금 푼 부분 (노란 칸 안이 이 문제의 글)' });
      return h;
    },
    act: function (a, el, p, st) {
      if (st.sub) return false;
      if (a === 'mk') { st.sel = +el.getAttribute('data-k'); return true; }
      if (a === 'sub' && st.sel >= 0) { st.sub = 1; return true; }
      return false;
    } });
};

SX.apps.blank = function (D, o) {
  GM.run({ D: D, set: o.set, gen: 'blank', kr: true, hw: o.hw,
    tag: function () { return '빈칸 추론'; },
    initSt: function () { return { sel: -1 }; },
    done: function (p, st) { return st.sel >= 0; },
    ok: function (p, st) { return st.sel === p.pos; },
    view: function (p, st, ps, done) {
      var b = ps.blanks[p.bi], opts = G.blankOpts(ps, p), h = '<div class="psg">';
      ps.en.forEach(function (s, i) {
        var inner, bk = (i === b.s && !done);
        if (i === b.s) { var q = s.indexOf(b.ans); inner = GM.esc(s.slice(0, q)) + (done ? '<mark>' + GM.esc(b.ans) + '</mark>' : '<span class="bl">____</span>') + GM.esc(s.slice(q + b.ans.length)); }
        else inner = GM.esc(s);
        h += '<span class="sent' + (bk ? ' blk' : '') + '">' + inner + '<span class="kr">' + GM.esc(ps.ko[i]) + '</span></span>';
      });
      h += '</div><div class="ask">빈칸에 들어갈 말로 가장 알맞은 것은?</div>';
      opts.forEach(function (op, i) {
        var c = 'ob'; if (done) { if (op.ok) c += ' ok'; else if (i === st.sel) c += ' ng'; }
        h += '<button type="button" class="' + c + '" data-act="o" data-i="' + i + '"><b class="cn">' + GM.CIR[i] + '</b> ' + GM.esc(op.en) + '</button>';
      });
      if (!done) return h;
      var ok = st.sel === p.pos;
      h += '<div class="ex"><div class="res ' + (ok ? 'o' : 'x') + '">' + (ok ? '정답이에요.' : '아쉬워요. 정답은 ' + GM.CIR[p.pos] + '이에요.') + '</div>';
      var q2 = ps.en[b.s].indexOf(b.ans);
      h += '<div class="ans"><b>' + GM.CIR[p.pos] + '</b> ' + GM.esc(ps.en[b.s].slice(0, q2)) + '<mark>' + GM.esc(b.ans) + '</mark>' + GM.esc(ps.en[b.s].slice(q2 + b.ans.length)) + '<span class="ko">' + GM.esc(ps.ko[b.s]) + '</span><span class="ko">' + GM.esc(b.ans) + ' : ' + GM.esc(b.ans_ko) + '</span></div>';
      h += '<ul class="ol">'; opts.forEach(function (op, i) { if (!op.ok) h += '<li><b>' + GM.CIR[i] + '</b> ' + GM.esc(op.ko) + '</li>'; });
      h += '</ul>';
      if (b.clue) h += '<div class="why"><div class="wd">이 빈칸은 무슨 내용일까요?</div><div class="jt1">' + GM.kline(b.clue) + '</div></div>';
      h += GM.ctx(D, ps, { from: Math.max(0, b.s - 1), to: Math.min(ps.en.length - 1, b.s + 1), mark: b.s, markLab: '빈칸 문장', cap: '빈칸이 있는 부분 (앞뒤 문장 포함)' });
      return h + '</div>';
    },
    act: function (a, el, p, st) {
      if (st.sel >= 0) return false;
      if (a === 'o') { st.sel = +el.getAttribute('data-i'); return true; }
      return false;
    } });
};
