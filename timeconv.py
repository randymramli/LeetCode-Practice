def timeConversion(s):
    # Write your code here
    hour_time = ''
    if s[-2] == 'P':
        hour_time = str(int(s[0:2]) + 12)
        if hour_time == '24':
            hour_time = '12'
    else:
        hour_time = str(int(s[0:2]))
        if hour_time == '12':
            hour_time = '00'
        else:
            hour_time = '0' + hour_time
    
    result = hour_time + s[2:8]
    print(result)

if __name__ == '__main__':
    a = '06:40:03AM'
    timeConversion(a)