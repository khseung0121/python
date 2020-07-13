with open('words_27.txt','r') as file: ##파일을 읽기모드로 열어줍니다.
    words = file.readlines() ##파일의 내용을 리스트로 불러옵니다.
    words=words[0].split() ##파일의 내용이 한 줄이므로 0번째에 문자열이 들어있습니다.
    for i in words:
        if 'c' in i:
            print(i.strip(',.')) ## 콤마와 점을 없애고 출력합니다.
