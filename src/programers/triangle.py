# -*- coding: utf-8 -*-#



def solution(triangle):
    answer = 0

    answer = triangle[0][0];
    currentIdnex = 0
    for i in triangle: #i 높이
        if i == currentIdnex:
            answer += max(triangle[i][currentIdnex],triangle[i][currentIdnex+1])

        else :
            answer += max(triangle[i][currentIdnex-1],triangle[i][currentIdnex])




    return answer


if __name__ == '__main__':
    solist = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

    print solution(solist)




