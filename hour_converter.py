def timeConversion(s):
    hour, minute, secondampm = s.split(":")

    print(hour, minute, secondampm)

   
    if "PM" in secondampm and hour == "12":
        hour = "12"
    elif "PM" in secondampm and hour != "12":
        hour = str(int(hour) + 12)
    elif "AM" in secondampm and hour == "12":
        hour = "00"
    
    new_time = hour + ":" + minute + ":" + secondampm[:2]
    
    print(new_time)

if __name__ == '__main__':
    a = "12:45:54PM"
    timeConversion(a)