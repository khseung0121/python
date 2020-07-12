files = input().split()

print(list(map(lambda x: '{0:03d}.{1}'.format(int(x.split('.')[0]), x.split('.')[1]), files)))
## files의 요소를 각각 람다 표현식으로 만든 함수에 넣어 반환하도록 map을 사용합니다.
## '.'을 기준으로 한 번 더 나눠야 하기 때문에 format에서 0위치엔 int로, 1위치엔 문자로 받고
## 숫자 세자리에 공백은 0으로 채워주는 0:03d를 사용합니다.
