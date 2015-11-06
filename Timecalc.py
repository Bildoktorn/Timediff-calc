import datetime
print ('Hi. Enter timestamps as \'hours minutes seconds milliseconds\' without quotes.\n')
while 1:
    loads = []
    try:
        runstart = [int(x) for x in input ('Run starts at? ').split()]
        while 1:
            loadstart = [int(x) for x in input ('Load starts at? Type \'0\' without quotes if none or finished. ').split()]
            if loadstart == [0]:
                break
            loadend = [int(x) for x in input ('Load ends at? ').split()]
            loadstart = datetime.timedelta(0, loadstart[2], 0, loadstart[3], loadstart[1], loadstart[0])
            loadend = datetime.timedelta(0, loadend[2], 0, loadend[3], loadend[1], loadend[0])
            loads.append(loadend-loadstart)            
        runend = [int(x) for x in input ('Run ends at? ').split()]
        runstart = datetime.timedelta(0, runstart[2], 0, runstart[3], runstart[1], runstart[0])
        runend = datetime.timedelta(0, runend[2], 0, runend[3], runend[1], runend[0])
        runtime = runend-runstart
        if loads:
            for x in loads:
                runtime -= x
            
        print (str(runtime) + '\n')
    except (ValueError, IndexError):
        print ('Incorrect input. Input as \'hours minutes seconds milliseconds\' without quotes.')
    