import datetime
date = str(datetime.datetime.now().date())
date = date.split('-')
dateee = []
for d in date:
    
    dateee.append(int(d))
bils = [[[2024,3,1],[13,42,00],'مجد أبو النور','CASH',33,3,3,3,[1, 4]],[[2024,3,2],[13,42,00],'مجد أبو النور','CASH',33 ,3,3,3,[2]],[[2024,3,1],[13,47,00],'مجد أبو النور','CASH',33 ,3,3,3,[3]]]
products = [['1',"صلصة بندورة",3],["2" ,'طحين',5],['3',"أرز",5],['4',"عدس",30]]
users = [['majdapoalnoor', '01234' , 'Mohammed Attalaa' , 'moajdddd.jpg'],['hala' , '55', 'MAJD', 'majd.jpg']]
def logd_in(user, passw):
    for j in users:
        if j[0] == user:
            if j[1] == passw:
                return j[2]
            else: return 'WRONG PASSWORD'
    return False
def seachnamebyemail(username):

    for n in users:
        if n[0] == username:
            return n[3], n[0]
def getallorders():
    oo = []
    for i in bils :
        if i[0] == dateee:
            oo.append(i)
    return oo
data= getallorders()
print(data)
