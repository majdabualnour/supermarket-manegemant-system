import datetime 
print(datetime.datetime.today())
time = str(datetime.datetime.today())
time = time.split(' ')[1]
time = time.split('.')[0]
print(time)

