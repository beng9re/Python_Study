# -*- coding: utf-8 -*-


#list 활용법
'''
list.index( value ) : 값을 이용하여 위치를 찾는 기능
list.extend( [value1, value2] ) : 리스트 뒤에 값을 추가 (‘+’연산자 보다 성능이 좋음)
list.insert( index, value ) : 원하는 위치에 값을 추가
list.sort( ) : 값을 순서대로 정렬
list.reverse( ) : 값을 역순으로 정렬
list.pop()
list.append()

'''




if __name__ == '__main__':
    _list = ['a','b','c','d','e']

    print len(_list)    #리스트의 길이

    print _list.index('c') #해당 문자열 포함한 리스트 찾기

    _list.append('x') # 리스트에 추가하기

    _listCapy = _list[3:5];

    # 리스트 끼리 합 칠수 있음

    print "34".join(_listCapy) #구분자 만들기


    print _list[::2]    # Step 2번씩 뛰어넘기 가능








