country = [
[0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1],
[0 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1],
[0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1],
[0 ,1 ,1 ,0 ,0 ,0 ,0 ,1 ,1],
[0 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1],
[1 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,0],
[0 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,0],
[0 ,1 ,1 ,1 ,0 ,1 ,1 ,0 ,1]
]
infection_queue = []
originof1 = int(input('Enter the origin: '))-11
neighbours = [1,-1,10,-10]

def show():
 for i in country:
    for k in i:
        print(k,end=' ')
    print()
 print()
 print()

def clean(citynumber):
    if(citynumber>9):
     citynumber = str(citynumber)
     return int(citynumber[0]),int(citynumber[1])
    elif(citynumber>0):
     citynumber = '0'+str(citynumber)
     return int(citynumber[0]),int(citynumber[1])

def infect(city,disease,causes):
    for i in neighbours:
        try:
         x,y = clean(city+i)
         if (country[x][y]==causes):
            infection_queue.append(city+i)
        except:
            ok='ok'
    x,y = clean(city)
    infection_queue.pop(0)
    country[x][y]=disease
    show()

def plague(steep):
    infection_queue.append(steep)
    while(len(infection_queue)):
        infect(infection_queue[0],' ',1)
print()
print()
print()
plague(originof1)