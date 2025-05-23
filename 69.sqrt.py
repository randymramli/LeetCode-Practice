def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        l=0
        r=x
        while l<=r:
            m = (r-l)/2+l
            print("m1: ", m)
            if(m>x/m):
                r=m-1
                print("r1: ", r)
            elif(m<x/m):
                l=m+1
                print("l1: ", l)
            else:
                print("m: ", m)
        
        print("r: ", r)

if __name__ == "__main__":
     x = 8
     mySqrt(x)