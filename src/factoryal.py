# -*- coding: utf-8 -*-


def factoryal(n):
    if n < 1 :
        return 1
    return n * factoryal(n-1)


#두 자연수 a와 b의 최대공약수를 구하는 알고리즘을 만들어 보세요.

def soulution (a,b):
    list1 = sol(a)
    list2 = sol(b)


    for i in list1:
        for j in list2:
            if(i==j):
                return i

    return 0

def uclie (a,b):

    if b == 0:  # 종료 조건

        return a

    return uclie(b, a % b)  # 좀 더 작은 값으로 자기 자신을 호출

def fivo (n):
    if (n==0):
        return 0
    if (n<3) :
       return 1
    else:
       return fivo(n-1) + fivo(n-2)



def sol(a):
    returnList = []

    for i in range(1,a+1):
        if (a%i == 0):
            returnList.append(i)
    returnList.reverse()

    return returnList






if __name__ == '__main__':
    print (factoryal(5))
    print (soulution(10,5))

    fivoList = []

    for i in range(10) :
        fivoList.append(fivo(i))

    print fivoList


