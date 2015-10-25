import datetime
print ('Hi hello')
while 1:
    time1 = [int(x) for x in input ('First time? ').split()]
    time2 = [int(x) for x in input ('Second time? ').split()]
    try:
        time1 = datetime.timedelta(0, time1[2], 0, time1[3], time1[1], time1[0])
        time2 = datetime.timedelta(0, time2[2], 0, time2[3], time2[1], time2[0])
        print (str(time2-time1) + '\n')
    except:
        print (time1, time2)
        print ('Error, incorrect input. Input as hours minutes seconds milliseconds only separated by space.')