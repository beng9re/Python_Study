# -*- coding: utf-8 -*-

'''
    1부터 0 까지의 숫자의 합 구하기
'''

def sum(s):
    returnSum = 0
    for i in range(1,s,1):
        returnSum += i

    return returnSum


def main():
    print '숫자 입력 :'
    number = int(input())

    sumVal = 0

    while 0 < number:
       sumVal += number
       number -= 1

    print sumVal

    print sum(10)

    #s[2:0] = 'hh' ## error 슬라이싱은 변경 불가


#    print len('안녕?')
    # 한글은 2 byte 처

if __name__ == '__main__':
    main()