korean, english, mathematics, science = map(int, input().split())
def get_min_max_score(*args): # 인수의 개수가 정해지지 않은 가변 인수 함수를 만들어야 합니다.
    max=0 # 가장 높은 점수를 max에 넣을 것이므로 기본값은 제일 작아야 합니다.
    min=100 # 마찬가지로 제일 높아야 합니다.
    for i in args:
        if max < i:
            max = i
        if min > i:
            min = i
    return min, max # 아래를 보면 min_score가 max_score보다 앞에있으므로 min먼저 return합니다.

def get_average(**kwargs): # 키워드 인수를 사용하는 가변 인수 함수를 만들어야 합니다.
    sum=0
    for i,j in kwargs.items():
        sum += j # j가 값을 의미하므로 키를 의미하는 i를 더하지 않도록 주의합니다.
    return sum / len(kwargs.items())

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean,english=english,mathematics=mathematics,science=science)
print('낮은 점수: {0:.2f}, 높은점수 : {1:.2f}, 평균점수 : {2:.2f}'
      .format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은점수 : {1:.2f}, 평균점수 : {2:.2f}'
      .format(min_score, max_score, average_score))
