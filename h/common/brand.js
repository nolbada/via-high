/* 목록 버튼에 학원 이름 표시 (261022): 모든 "⌂ 목록" 버튼(a.homefab)을 두 줄(이름 + 목록)로 바꾸고, 옆의 빠른정답 버튼이 겹치지 않게 민다. 페이지마다 코드를 붙이지 않고 이 파일 하나로 관리한다. */
(function(){
  var NAME='비타민 영어클리닉';
  function fit(){
    var f=document.querySelector('a.homefab'),q=document.getElementById('fq');
    if(f&&q){var w=f.getBoundingClientRect().width||88;q.style.right=Math.round(12+w+8)+'px'}
  }
  function up(){
    var a=document.querySelectorAll('a.homefab');
    for(var i=0;i<a.length;i++){var f=a[i];if(f.getAttribute('data-vb'))continue;f.setAttribute('data-vb','1');
      f.innerHTML='<span style="display:block;font-size:8.5px;font-weight:600;letter-spacing:.04em;line-height:1.1;margin-bottom:3px;opacity:.9">'+NAME+'</span><span style="display:block;font-size:13px;font-weight:700;line-height:1.1">⌂ 목록</span>';
      f.style.textAlign='center';f.style.whiteSpace='nowrap';f.style.lineHeight='1.1';f.style.padding='7px 11px'}
    fit();
  }
  up();
  addEventListener('load',up);addEventListener('resize',fit);
})();
