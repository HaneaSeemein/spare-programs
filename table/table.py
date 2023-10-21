def make_table(rows,labels=False,centered=False):
    def maxlen(megalist):
        mc = []
        def cs (megalist, indx):
            k = []
            for list in megalist:
                k.append(len(str(list[indx])))
            y = max(k)
            return y 
        ############
        r = 0
        while r < int(len(megalist[0])):
            mc.append(cs(megalist,r))
            r=r+1
        return mc
    #############
    all=list(rows)
    if(labels): 
     all.append(labels)
    gap = maxlen(all)
    
    def edge(l,c,r):
        print(l,end="")
        for yo in gap:
         if(gap.index(yo)==len(gap)+1):
          print("─"*(yo+2)+r)  
         else:  
          print("─"*(yo+2)+c, end="")

    def labul(label):
        f = 0
        if(labels):
         print('│',end='')
        for e in label:
            t = gap[f]
            align(e,t)
            f=f+1
        print()   
        edge("├","┼","┤")
    
    def align(e,m):
     if(centered):
         spa= m-len(str(e))+2
         s1=int(spa/2)
         s2=int(spa/2)+spa%2
         print((" "*s1)+str(e)+(" "*s2)+"│",end='') 
     else:
         print(" "+str(e)+" "*(m-len(str(e))+1)+"│",end='')
    
    ##first line
    edge("┌","┬","┐",)
    ##label and its bottom line
    try: 
        labul(labels)  
    except:
        pass
    ##the body
    for L in rows:
        f = 0
        print('│',end='')
        for e in L:
            n = gap[f]
            align(e,n)
            f=f+1
        print() 
    ##last line
    edge("└","┴","┘")

make_table(
            rows=[
                ["Apple", 5],
                ["Banana", 3],
                ["Cherry", 7],
            ],
        ),
make_table(
            rows=[
                ["Apple", 5],
                ["Banana", 3],
                ["Cherry", 7],
            ],
            labels=["Fruit", "Tastiness"],
        ),
make_table(
            rows=[
                ["Apple", 5],
                ["Banana", 3],
                ["Cherry", 7],
            ],
            labels=["Fruit", "Tastiness"],
            centered=True
        )