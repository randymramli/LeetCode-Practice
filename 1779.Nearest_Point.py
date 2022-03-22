def nearestValidPoint(x, y, points):
    result = abs(x-points[0][0]) + abs(y-points[0][1])
    index = 0
    abc = len(points)
    if (abc == 1 and result == 0) :
        print(index)

    elif (abc ==1 and result < 0) :
        print(result)

    for i in range(1,abc-1):
        dist = abs(x-points[i][0]) + abs(y-points[i][1])
        result = min(dist,result)
        if result == dist:
            index = i
    print(index)



if __name__ == '__main__':
    x = 3
    y = 4
    points = [[3,4]]
    nearestValidPoint(x,y,points)