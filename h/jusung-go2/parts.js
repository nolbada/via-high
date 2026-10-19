/* 덩어리(part) 정의: ?part=1|2|3 으로 각 활동 페이지가 자기 범위만 보여 준다.
   교과서 4과  : 1=본문 ❶❷❸(L4-1~3) 2=❹❺(L4-4~5) 3=❻❼(L4-6~7)
   모의고사    : 1=22년 11월 2=23년 11월 3=24년 10월
   기록 키     : "<구간>p<번호>:<활동>"  예) L4p1:ko, mockp2:abc
*/
var PARTS={
  L4:{1:['L4-1','L4-2','L4-3'],2:['L4-4','L4-5'],3:['L4-6','L4-7']},
  mock:{1:'2211',2:'2311',3:'2410'},
  names:{L4:{1:'본문 ❶~❸',2:'본문 ❹~❺',3:'본문 ❻~❼'},mock:{1:'22년 11월',2:'23년 11월',3:'24년 10월'}}
};
var PART=(function(){var m=/[?&]part=([123])\b/.exec(location.search);return m?+m[1]:0})();
/* 패시지 id가 이 덩어리에 속하는지. kind: 'L4' 또는 'mock' */
function inPart(kind,pid,part){part=part||PART;if(!part)return true;
  if(kind==='L4')return PARTS.L4[part].indexOf(pid)>=0;
  return String(pid).indexOf(PARTS.mock[part]+'-')===0}
function partKey(kind){return PART?kind+'p'+PART:kind}
