
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

/* ---- 전체 흐름(순서도): 한글 한 줄씩 ▼로 잇고 기·승·전·결 소제목, 푼 부분은 노란 박스 ---- */
GM.strip = function (s) { return String(s).replace(/\s*\([^()]*[A-Za-z][^()]*\)\s*$/, ''); };
GM.ctx = function (D, ps, o) {
  o = o || {};
  var B = ps.base || ps, g0 = ps.g0 || 0, from = g0 + o.from, to = g0 + o.to, mark = o.mark == null ? null : g0 + o.mark;
  var zones = B.zones || [{ start: 0, len: ps.en.length, label: ps.label, gist: ps.gist, stt: ps.stt }];
  var first = -1, last = -1;
  zones.forEach(function (z, zi) { if (z.start + z.len - 1 >= from && z.start <= to) { if (first < 0) first = zi; last = zi; } });
  var h = '<div class="ctx"><div class="wd">' + GM.esc(o.title || '전체 흐름 · 이 순서로 기억해요') + '</div>';
  zones.forEach(function (z, zi) {
    if (zi < first - 1 || zi > last + 1) return;
    var z0 = z.start, z1 = z.start + z.len - 1;
    if (zi < first || zi > last) {
      h += '<div class="zc"><span class="zt">' + (zi < first ? '앞 내용' : '뒷 내용') + '</span><b>' + GM.esc(z.label) + '</b>' + (z.gist ? ' · ' + GM.esc(GM.strip(z.gist)) : '') + '</div>';
      return;
    }
    h += '<div class="zx"><div class="zh"><b>' + GM.esc(z.label) + '</b>' + (z.gist ? '<span class="zg">' + GM.esc(GM.strip(z.gist)) + '</span>' : '') + '</div><div class="flw">';
    var inbox = false, prevSt = null, i, firstNode = true;
    for (i = z0; i <= z1; i++) {
      var inr = i >= from && i <= to;
      if (inr && !inbox) { h += '<div class="hlbox"><div class="hlt">' + GM.esc(o.cap || '지금 푼 부분') + '</div>'; inbox = true; }
      if (!inr && inbox) { h += '</div>'; inbox = false; }
      var st = B.st && B.st[i];
      if (st && st !== prevSt) { h += '<div class="stg"><b>' + GM.esc(st) + '</b>' + (z.stt && z.stt[st] ? ' ' + GM.esc(z.stt[st]) : '') + '</div>'; prevSt = st; firstNode = true; }
      var mk = mark === i, tg = o.tags && o.tags[i - g0];
      if (!firstNode) h += '<div class="far">▼</div>';
      firstNode = false;
      h += '<div class="fd' + (mk ? ' mk1' : '') + '">' + (tg ? '<span class="tgl">' + GM.esc(tg) + '</span>' : '') + (mk && o.markLab ? '<span class="tgl y">' + GM.esc(o.markLab) + '</span>' : '') +
        GM.chip(B.key[i][0]) + '<span class="cl">' + GM.esc(GM.strip(B.key[i][1])) + '</span></div>';
    }
    if (inbox) h += '</div>';
    h += '</div></div>';
  });
  return h + '</div>';
};

/* ---- 왜 이 순서/자리인가: 단서 카드(유형 칩 + 신호어 + 한 줄) + 앞→이 문장, 긴 설명은 접어 둔다 ---- */
GM.why = function (ps, items, title) {
  var h = '<div class="why"><div class="wd">' + GM.esc(title) + '</div><ol class="chain">';
  items.forEach(function (it) {
    var i = it.i, c = ps.cl && ps.cl[i], t = ps.why && ps.why[i];
    h += '<li><span class="jl">' + GM.esc(it.lab) + '</span><div class="jt">';
    if (c) {
      h += '<div class="jc"><span class="ct">' + GM.esc(c.t) + '</span>' + (c.w ? '<b class="cw">' + GM.esc(c.w) + '</b>' : '') + '</div><div class="jm">' + GM.esc(c.m) + '</div>';
      if (i > 0) h += '<div class="jf"><div><span class="fa">앞</span>' + GM.esc(GM.strip(ps.key[i - 1][1])) + '</div><div><span class="fa y">이 문장</span>' + GM.esc(GM.strip(ps.key[i][1])) + '</div></div>';
      if (t) h += '<details class="mo"><summary>자세히 보기</summary><div>' + GM.kline(t) + '</div></details>';
    } else {
      if (!t) { var k = ps.key[i]; t = (k[0] ? k[0] + ' ' : '') + k[1]; }
      h += GM.kline(t);
    }
    h += '</div></li>';
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
    var f = { id: 'flat', label: D.title, taught: null, en: [], ko: [], key: [], why: [], nums: [], link: [], ins: [], blanks: [], zones: [], cl: [], st: [], modes: ['ko', 'mun'] }, off = 0;
    D.passages.forEach(function (p) {
      var n = p.en.length, i;
      f.zones.push({ start: off, len: n, label: p.label, gist: p.gist, stt: p.stt });
      for (i = 0; i < n; i++) { f.en.push(p.en[i]); f.ko.push(p.ko[i]); f.key.push(p.key[i]); f.why.push(p.why[i]); f.cl.push(p.cl ? p.cl[i] : null); f.st.push(p.st ? p.st[i] : null); f.nums.push(p.nums ? p.nums[i] : off + i + 1); }
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
    for (ln = 6; ln <= 10; ln++) for (s = 0; s + ln <= N; s++) {
      var a = zl(s), b = zl(s + ln - 1);
      ws.push({ id: 'w' + s + '_' + ln, label: a === b ? a : a + ' ~ ' + b, taught: null, modes: ['abc'], g0: s, base: f2,
        en: f2.en.slice(s, s + ln), ko: f2.ko.slice(s, s + ln), key: f2.key.slice(s, s + ln), why: f2.why.slice(s, s + ln), cl: f2.cl.slice(s, s + ln),
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
