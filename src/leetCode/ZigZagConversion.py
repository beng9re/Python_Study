class Solution:

    #지그재그 출력하기
    ##
    '''
       AYPALISHIRING  IS Reeturn  "PAHNAPLSIIGYIR"

        P   A   H   N
        A P L S I I G
        Y   I   R



    '''



    def convert(self, s: str, numRows: int) -> str:
        array = [] 

        for a in range(numRows):
            array.append([])

        upFlag = 0
        downFlag = numRows - 1
        cursur = 0
        flag = -1
        returnStr = ""

        if numRows == 1:
            return s

        for index in range(len(s)):
            if cursur == upFlag or cursur == downFlag:
                flag *= -1
            array[cursur].append(s[index])
            cursur += flag

        for line in range(len(array)):
            returnStr += "".join(array[line])

        return returnStr






         #   if index % (numRows+1) == 0:

        print(returnStr)

        return array















if __name__ == '__main__':
    Solution.convert(Solution,'PAYPALISHIRING',3)



