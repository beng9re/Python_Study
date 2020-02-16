
# -*- coding: utf-8 -*-


# 주어진 숫자 n개 중 가장 큰 숫자를 찾는 알고리즘을 만들어 보세요.
# 2way : Max Index 찾기


def listSearch(lisval):
    maxVal = 0
    maxIndex = 0
    index = 0

    for i in range(len(lisval)):
        if maxVal < lisval[i]:
            maxVal = lisval[i];
            maxIndex = i;

    return [maxVal,maxIndex]

def main():
    listNumber = [7, 92, 18, 33, 58, 7, 33, 42]
    maxval = 0

    print 'one way: ' + str(listSearch(listNumber))

    maxval = max(listNumber)

    print 'two way:' + str(listNumber)
    print 'two way:' + str(listNumber.index(maxval))




if __name__ == '__main__':
    main()
