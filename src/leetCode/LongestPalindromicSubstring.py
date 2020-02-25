def solse(str): #가장큰대칭 문자열 찾기
    m = ''
    for i in range(len(str)):
        for j in range(len(str), i, -1):
            if len(m) >= j - i:
                break
            elif str[i:j] == str[i:j][::-1]: #대칭인지 판단한다
                m = str[i:j]
                break

    return m


if __name__ == '__main__':
    str = "abccba"
    print(solse(str))



