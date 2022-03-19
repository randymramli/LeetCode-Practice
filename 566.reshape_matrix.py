import numbers


def matrixReshape(mat, r, c):
    if mat == [] or r * c != (len(mat) *len(mat[0])):
        return mat

    ans = [[0 for j in range(c)] for i in range(r)]
    k = 0

    for row in mat:
        for num in row:
            ans[k//c][k%c] = num
            k += 1
    
    print(ans)

if __name__ == '__main__':
    mat = [[1,2],[3,4]]
    r = 1
    c = 4
    matrixReshape(mat,r,c)