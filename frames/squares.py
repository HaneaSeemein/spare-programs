from blessed import Terminal
term = Terminal()
import pygame.time

def thinking_box(l1,l2,l3):
    pygame.time.wait
    #the window
    y_co = 0
    mul=0
    fac = term.width-2
    h = term.height 
    if bool(term.height%2):  h = h-1 #to make it compatible for even numbered height...bcs we have three rows in the middle
    s = l1
    k= l2
    t = l3
    while(y_co<=h):
     if(y_co==h/2):#middle 3 rows- multiplying characters with numbers....
        print(f"{term.turquoise2_on_gray1}│"*mul+f"{term.turquoise2_on_gray1} "*int((fac+3-len(s))/2)+s+f"{term.turquoise2_on_gray1} "*int((fac+2-len(s))/2)+f"{term.turquoise2_on_gray1}│"*mul,end='\n') 
        print(f"{term.turquoise2_on_gray1}│"*mul+f"{term.turquoise2_on_gray1} "*int((fac+3-len(k))/2)+k+f"{term.turquoise2_on_gray1} "*int((fac+2-len(k))/2)+f"{term.turquoise2_on_gray1}│"*mul,end='\n')
        print(f"{term.turquoise2_on_gray1}│"*mul+f"{term.turquoise2_on_gray1} "*int((fac+3-len(t))/2)+t+f"{term.turquoise2_on_gray1} "*int((fac+2-len(t))/2)+f"{term.turquoise2_on_gray1}│"*mul,end='\n')
        y_co = y_co+1       
     elif(y_co>h/2):#upper half
        print(f"{term.turquoise2_on_gray1}│"*(mul-1)+f"{term.turquoise2_on_gray1}└"+f"{term.turquoise2_on_gray1}─"*(fac+2)+f"{term.turquoise2_on_gray1}┘"+f"{term.turquoise2_on_gray1}│"*(mul-1),end='\n')
        y_co = y_co+1
        mul = mul-1
        fac = fac + 2
     else:#lower half
        print(f"{term.turquoise2_on_gray1}│"*mul+f"{term.turquoise2_on_gray1}┌"+f"{term.turquoise2_on_gray1}─"*fac+f"{term.turquoise2_on_gray1}┐"+f"{term.turquoise2_on_gray1}│"*mul,end='\n')
        y_co = y_co+1
        mul = mul+1
        fac = fac - 2     
    h = term.height
    w = term.width
    #to place the input pointer?
    with term.location(x=int(w/2+5), y=int(h/2-3)):
        y = input()
    if y:
       exit()
    term.normal

l1=''
l2='hanea'
l3='will be rich'
thinking_box(l1,l2,l3)