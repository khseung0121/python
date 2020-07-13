with open('words_28.txt','r') as file:
    words=file.readlines()
for i in range(len(words)):##각 줄마다 한 단어씩 들어있으므로 바로 for문 실행
	a=words[i].strip('\n')##줄바꿈 표시를 없애줍니다.
	b=list(reversed(a))
	if list(a)==b:##회문이 맞으면 줄바꿈 표시를 없앤 a를 출력합니다.
		print(a)
