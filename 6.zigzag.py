def convert( s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [[] for row in range(numRows)]

        index = 0
        step = -1
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        
        for i in rows:
             print(i)
        
        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        
        a = ''.join(rows)
        print(a)

if __name__ == '__main__':
     s = "PAYPALISHIRING"
     num = 3
     convert(s, num)