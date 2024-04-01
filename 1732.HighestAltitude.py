def largestAltitude(gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        start = 0
        alt = [0]

        length = len(gain)

        for i in range(length):
            result = start + gain[i]
            alt.append(result)
            start = result
        
        return max(alt)

if __name__ == '__main__':
    gain= [-5,1,5,0,-7]
    largestAltitude(gain)