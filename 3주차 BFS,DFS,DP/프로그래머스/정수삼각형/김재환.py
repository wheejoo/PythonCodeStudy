def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j]+=triangle[i-1][0]
                continue
            if j == len(triangle[i])-1:
                triangle[i][j]+=triangle[i-1][-1]
                continue
            print(i,j, triangle[i][j])
            if triangle[i-1][j-1] > triangle[i-1][j]:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += triangle[i-1][j]
    print(triangle)
    return max(triangle[len(triangle)-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))