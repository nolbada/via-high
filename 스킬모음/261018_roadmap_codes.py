# 로드맵 홈 열기코드 만들기 (선생님 코드는 입력만 받고 어디에도 저장하지 않음)
# 사용: python 261018_roadmap_codes.py 개인코드 열쇠 [열쇠 ...]
#   예) python 261018_roadmap_codes.py abcde L4 4-1 4-2 4-3 L3 3-1 3-2 3-3
# 결과: 열기코드(선생님이 학생에게 알려 줄 것) + 홈 index.html 의 UH 배열에 넣을 해시
import sys, hashlib, getpass, json

AL = '23456789abcdefghjkmnpqrstuvwxyz'


def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()


def make(teacher, pc, keys):
    codes, uh = {}, []
    for k in keys:
        d = bytes.fromhex(sha(teacher + ':' + pc + ':' + k))
        codes[k] = ''.join(AL[b % 31] for b in d[:6])
        uh.append(sha(pc + ':' + k + ':' + codes[k]))
    return codes, uh


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit('사용: python 261018_roadmap_codes.py 개인코드 열쇠 [열쇠 ...]  (열쇠: L4, 4-1, 4-2, 4-3 처럼)')
    teacher = getpass.getpass('선생님 코드: ')
    pc, keys = sys.argv[1], sys.argv[2:]
    codes, uh = make(teacher, pc, keys)
    print('\n열기코드 (시트에 적고 학생에게 알려 주기):')
    for k in keys:
        print(' ', k, codes[k])
    print('\n홈 UH 배열에 이어 붙일 해시:')
    print(json.dumps(uh))
    print('\n새 학교 홈을 처음 만들 때만, TH 값:', sha(teacher))
