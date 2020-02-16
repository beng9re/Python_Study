
# -*- coding: utf-8 -*-
# n명의 사람 이름 중에서 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘을 만들어 보세요.


# [“Tom”, “Jerry”, “Mike”, “Tom”]

def soulution(a):
    #다른 풀이

    n = len(a)  # 리스트의 자료 개수를 n에 저장

    result = set()  # 결과를 저장할 빈 집합

    for i in range(0, n - 1):  # 0부터 n -2까지 반복

        for j in range(i + 1, n):  # i+1부터 n -1까지 반복

            if a[i] == a[j]:  # 이름이 같으면

                result.add(a[i])  # 찾은 이름을 result에 추가

    return result










if __name__ == '__main__':
    listval = ['Tom', 'Jerry', 'Mike', 'Tom']
    listMap = {};
    returnVal = [];


    for i in listval:
        if (listMap.get(i) == None):
            listMap[i] = 0
        else:
            listMap[i] = listMap[i]+1


    print listMap

    for k,v in listMap.items() :
        if (v > 0) :
            returnVal.append(k);


    print returnVal


