##키와 값을 따로 받는 문제이므로 zip()함수를 이용합니다.
keys=input().split()
values=list(map(int,input().split()))##각각 리스트로 받은 뒤에
mydict={}
mydict.update(zip(keys,values))##딕셔너리 한곳에 몰아넣습니다.
mydict={key:value for key,value in mydict.items() if value != 30 and key != 'delta'}
##딕셔너리에서 for문으로 키,값을 제거 시 딕셔너리의 길이가 변해 에러가 발생하므로
##제거하고 싶은 키,값 쌍을 제외한 나머지만으로 새로 딕셔너리를 만들어줍니다.
print(mydict)
