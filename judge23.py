col, row = map(int, input().split())
matrix = []
for i in range(row):###2차원 리스트 만들기###
    matrix.append(list(input()))
for i in range(col):
    for j in range(row):
        if matrix[i][j]=="*": ###지뢰면 넘겨줍니다.###
            continue
        matrix[i][j]=0 ###지뢰 갯수를 세어 더해주기 위해서 0으로 바꿔줍니다.###
        for row2 in range(i - 1, i + 2): ### 주변 8칸을 확인합니다.###
            for col2 in range(j - 1, j + 2):
                if row2<0 or row2>=row or col2<0 or col2>=col :
                    continue ###리스트를 벗어나는 것을 막아줍니다.###
                if matrix[row2][col2] == "*":
                    matrix[i][j]+=1 ###지뢰 발견 시 1씩 증가시킵니다.###
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end="")
    print()
