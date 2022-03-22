def generate(numRows):
    result = []

    for row_num in range(numRows):
        row = [None for _ in range(row_num+1)]
        row[0],row[-1] = 1,1

        for j in range(1, len(row)-1):
            row[j] = result[row_num-1][j-1] +  result[row_num-1][j]

        result.append(row)
    print(result)

if __name__ == '__main__':
    numRows = 5
    generate(numRows)