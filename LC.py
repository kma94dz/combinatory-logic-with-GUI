from tkinter import *
import tkinter.font as tkFont

win = Tk() # This is to create a basic window
#win.geometry("1950x900")  # this is for the size of the window 
win.resizable(0, 0)  # this is to prevent from resizing the window
win.title("Logique Combinatoire")

###################Starting with functions ####################
# 'btn_click' function : 
# This Function continuously updates the 
# input field whenever you enter a number










def getDistances(P,start,end):
        N=[]
        NP=[]
        C=[]
        PPP=0
        P2=[]
        for i in range(end):
            #P2=[]
            if P[0][i] == 1:
                NP.append(1)
                C.append(P[2][i])
                N.append(P[0][i])
                #P2.append(N)
                #P2.append(NP)
                #P2.append(C)
            else:
                C.append("B")
                C.append(P[2][i])

                N.append(1)
                N.append(1)
                
                NP.append(P[0][i]-1)
                NP.append(1)
                 
                
                
                #P2.append(N)
                #P2.append(NP)
                #P2.append(C)
                PPP=i
                break   
        for i in range(PPP+1,len(P[1])):
            NP.append(P[1][i])
            C.append(P[2][i])
            N.append(P[0][i])
        P2.append(N)
        P2.append(NP)
        P2.append(C)            
        return P2 


def getPuissances(P,start,end):
        
        N=[]
        NP=[]
        C=[]
        P2=[]
        PPP=0
        for i in range(end):
            #P2=[]
            if P[1][i] == 1:
                NP.append(1)
                C.append(P[2][i])
                N.append(P[0][i])
                #P2.append(N)
                #P2.append(NP)
                #P2.append(C)
            else:
                C.append("B")
                C.append(P[2][i])
                C.append(P[2][i])
                
                NP.append(1)
                NP.append(1)
                NP.append(P[1][i]-1)             

                N.append(1)
                N.append(1)
                N.append(1) 

                #P2.append(N)
                #P2.append(NP)
                #P2.append(C)
                PPP=i
                break  
        for i in range(PPP+1,len(P[1])):
            NP.append(P[1][i])
            C.append(P[2][i])
            N.append(P[0][i])
        P2.append(N)
        P2.append(NP)
        P2.append(C)
            
        return P2        



###print(V)
#P="".join(V[2])
###print(P)


def getBragets(P,s):
    for i in range(s,len(P)):
        par=[]
        if P[i]=="(":
            start=i
            end=0
            count=1
            for j in range(i+1,len(P)):
                if P[j]=="(":
                    count=count+1
                if P[j]==")":
                    count=count-1
                if count==0:
                    end=j
                    for k in range(start,end+1):
                        par.append(P[k])
                    break
           
        if len(par)>=3:
          return par,start,end
        else:
          #print("found empty braquet")
          return par
          
def refineBraq(P,v):
 N=[]
 NP=[]
 C=[]
 P3=[]
 if v==1:
  for i in range(len(P[2])):
   if P[2][i]=="(":
    count=0
    for j in range(i,len(P[2])):
     if P[2][j]=="(":
      count=count+1
     if P[2][j]==")":
      count=count-1
     if count==0:
      N.append(P[0][i])
      NP.append(P[1][i])
      C.append(P[2][i])
      break
   else:
    N.append(P[0][i])
    NP.append(P[1][i])
    C.append(P[2][i])
  P3.append(N)
  P3.append(NP)
  P3.append(C)  
  return P3
 if v==2:
  for i in range(len(P[2])):
   if P[2][i]==")":
    count=0
    for j in range(i,len(P[2])):
     if P[2][j]==")":
      count=count+1
     if P[2][j]=="(":
      count=count-1
     if count==0:
      #P3.append(P[i])
      N.append(P[0][i])
      NP.append(P[1][i])
      C.append(P[2][i])
      break
   else:
    #P3.append(P[i])
    N.append(P[0][i])
    NP.append(P[1][i])
    C.append(P[2][i])
  P3.append(N)
  P3.append(NP)
  P3.append(C) 
  return P3



# COMBINATORS
def B(P,f,x,y):
 N=[]
 NP=[]
 C=[]
 R=[]

 #F
 try:
  if len(f)>1:
   for i in range(f[0],f[1]+1):
    N.append(P[0][i])
    NP.append(P[1][i])
    C.append(P[2][i])
 except:
   N.append(P[0][f])
   NP.append(P[1][f])
   C.append(P[2][f])

 #(
 N.append(1)
 NP.append(1)
 C.append("(")

 #X
 try:
  if len(x)>1:
   for i in range(x[0],x[1]+1):
    N.append(P[0][i])
    NP.append(P[1][i])
    C.append(P[2][i])
 except:
   N.append(P[0][x])
   NP.append(P[1][x])
   C.append(P[2][x])

 #Y
 try:
  if len(y)>1:
   for i in range(y[0],y[1]+1):
    N.append(P[0][i])
    NP.append(P[1][i])
    C.append(P[2][i])
 except:
   N.append(P[0][y])
   NP.append(P[1][y])
   C.append(P[2][y])

 #)
 N.append(1)
 NP.append(1)
 C.append(")")

 R.append(N)
 R.append(NP)
 R.append(C)
 ##print(R)
 #return f+"("+x+y+")"
 return R

def C(P,f,x,y):
 N=[]
 NP=[]
 C=[]
 R=[]
 ##print("----1")
 #F
 try:
  if len(f)>1:
   for i in range(f[0],f[1]+1):
    N.append(P[0][i])
    NP.append(P[1][i])
    C.append(P[2][i])
 except:
   N.append(P[0][f])
   NP.append(P[1][f])
   C.append(P[2][f])
 ##print("----2")

 #Y
 try:
  if len(y)>1:
   for i in range(y[0],y[1]+1):
    N.append(P[0][i])
    NP.append(P[1][i])
    C.append(P[2][i])
 except:
   ##print("----C")
   ##print(P)
   ##print(P[0][y])
   N.append(P[0][y])
   ##print("----C")
   NP.append(P[1][y])
   C.append(P[2][y])
   ##print("----C")
 

 #X
 try:
  if len(x)>1:
   for i in range(x[0],x[1]+1):
    N.append(P[0][i])
    NP.append(P[1][i])
    C.append(P[2][i])
 except:
   N.append(P[0][x])
   NP.append(P[1][x])
   C.append(P[2][x])


 R.append(N)
 R.append(NP)
 R.append(C)
 ##print(R)
 ##print(R)
 #return f+"("+x+y+")"
 return R



def K(P,x):
 N=[]
 NP=[]
 C=[]
 R=[]

 #X
 try:
  if len(x)>1:
   for i in range(x[0],x[1]+1):
    N.append(P[0][i])
    NP.append(P[1][i])
    C.append(P[2][i])
 except:
   N.append(P[0][x])
   NP.append(P[1][x])
   C.append(P[2][x])

 R.append(N)
 R.append(NP)
 R.append(C)
 print(R)
 return R



def W(P,f,x):
 N=[]
 NP=[]
 C=[]
 R=[]
 ##print("----1")
 #F
 try:
  if len(f)>1:
   for i in range(f[0],f[1]+1):
    N.append(P[0][i])
    NP.append(P[1][i])
    C.append(P[2][i])
 except:
   N.append(P[0][f])
   NP.append(P[1][f])
   C.append(P[2][f])
 ##print("----2")
 

 #X
 try:
  if len(x)>1:
   for i in range(x[0],x[1]+1):
    N.append(P[0][i])
    NP.append(P[1][i])
    C.append(P[2][i])
 except:
   N.append(P[0][x])
   NP.append(P[1][x])
   C.append(P[2][x])

 #X
 try:
  if len(x)>1:
   for i in range(x[0],x[1]+1):
    N.append(P[0][i])
    NP.append(P[1][i])
    C.append(P[2][i])
 except:
   N.append(P[0][x])
   NP.append(P[1][x])
   C.append(P[2][x])


 R.append(N)
 R.append(NP)
 R.append(C)
 ##print(R)
 ##print(R)
 #return f+"("+x+y+")"
 return R


def C2(P,x,y):
 N=[]
 NP=[]
 C=[]
 R=[]
 ##print("----1")
 #F
 '''
 try:
  if len(f)>1:
   for i in range(f[0],f[1]+1):
    N.append(P[0][i])
    NP.append(P[1][i])
    C.append(P[2][i])
 except:
   N.append(P[0][f])
   NP.append(P[1][f])
   C.append(P[2][f])
 ##print("----2")
 '''

 #Y
 try:
  if len(y)>1:
   for i in range(y[0],y[1]+1):
    N.append(P[0][i])
    NP.append(P[1][i])
    C.append(P[2][i])
 except:
   ##print("----C")
   ##print(P)
   ##print(P[0][y])
   N.append(P[0][y])
   ##print("----C")
   NP.append(P[1][y])
   C.append(P[2][y])
   ##print("----C")
 

 #X
 try:
  if len(x)>1:
   for i in range(x[0],x[1]+1):
    N.append(P[0][i])
    NP.append(P[1][i])
    C.append(P[2][i])
 except:
   N.append(P[0][x])
   NP.append(P[1][x])
   C.append(P[2][x])


 R.append(N)
 R.append(NP)
 R.append(C)
 ##print(R)
 ##print(R)
 #return f+"("+x+y+")"
 return R


def S(x,y,z):
 return x+z+"("+y+z+")"
##########
 
def fxyz(P,s,v,F,Pos):
 # this function is the backbone of the combinatory logic, as it is able to
 # return the variables, exemple the combinator B needs 3 parameters f,x and y
 # so we give to our function fxyz() P: the sentence, s: is the position from where
 # to start in the sentence, v: the number of parameters to return, F: an empty list wich will
 # contain the parameters, Pos: an empty list taht will contain the positions of the start and end of
 # every parameter found in the sentece.
 try:
  if P[s]=="(":
   b=getBragets(P,s)
   F.append("".join(b[0]))
   T=[]
   T.append(b[1])
   T.append(b[2])
   Pos.append(T)
   v=v-1
   if v!=0:
    fxyz(P,b[2],v,F,Pos)
  if P[s]==")":
   for j in range(s,len(P)):
    if P[j]!=")":
     fxyz(P,j,v,F,Pos)
     break
  if P[s]!="(" and P[s]!=")":
   F.append(P[s])
   Pos.append(s)
   v=v-1
   s=s+1
   if v!=0:
    fxyz(P,s,v,F,Pos)
 except:
  print(">>>>>>could not find a variable to complete, please check your sentence")
   
def Place(P,SENTENCE,i,F,Pos,operation):
 # this function is able to place the changes made by the combinators,
 # first part(FP) is the part of the sentence before the combinator, and second part (SP)
 # is the part affected by the combinator and Third part (TP) is the part after the changes also not affected by
 # the combinator as exemple: S=aBfxyc -> FP(S)=a, SP(S)=Bfxy, TP(S)=c  
 # the changes SP will be placed in the right place : af(xy)c
 ##print("placing"+str(SENTENCE[2]))
 P4=[]
 N=[]
 NP=[]
 C=[]

 #placing FP
 try:
  if len(Pos[0])>1:
   ##print(Pos[0])
   w=Pos[0]
   for j in range(w[0]-1):
    #P4.append(P[j])
    N.append(P[0][j])
    NP.append(P[1][j])
    C.append(P[2][j])    
 except:
  ##print(Pos[0])
  ##print(i)
  for j in range(Pos[0]-1):
   #P4.append(P[j])
   N.append(P[0][j])
   NP.append(P[1][j])
   C.append(P[2][j])   

 #placing SP  
 #P4.append(SENTENCE)
 ##print(len(SENTENCE[2]))
 ##print("placing + "+str(SENTENCE[2]))
 for i in range(len(SENTENCE[2])):
  ##print(i)
  N.append(SENTENCE[0][i])
  NP.append(SENTENCE[1][i])
  C.append(SENTENCE[2][i])
 #placing TP
 if operation==1:
  try:
   if len(Pos[len(Pos)-1])>1:
    w=Pos[len(Pos)-1]
    for j in range(w[1]+1,len(P[2])):
     #P4.append(P[j])
     N.append(P[0][j])
     NP.append(P[1][j])
     C.append(P[2][j])
  except:
   for j in range(Pos[len(Pos)-1]+1,len(P[2])):
    '''#print(j)
    #print(len(P[2]))
    #print(P[0])
    #print(P[1])
    #print(P[2])'''
    #P4.append(P[j])
    N.append(P[0][j])
    NP.append(P[1][j])
    C.append(P[2][j]) 
 P4.append(N)
 P4.append(NP)
 P4.append(C)

 ##print(P4)
 return P4
  
 
  
'''
#print("INPUT P:"+str(P))
V2 = getDistances(P,0,1)
#print("RESOLUTION DES DISTANCES:"+str(V2))
V = getCombs(V2,0,1)
'''




def getCombs(P):
 comb=0
 #listing the number of combinators in the SENTENCE
 for l in P:
  if l=="B" or l=="C" or l=="S" or l=="G" or l=="K" or l=="W":
   comb=comb+1
 return comb



def pars(P):
 c=0
 Q=[]
 while(c<=getCombs(P[2])):
  for i in range(len(P[2])):
   ##print(P[2])
   try:
    if P[2][i]=="B":
     if(P[0][i]>1):
      P = getDistances(P,0,i+1)
      #print("RESOLUTION DE DISTANCE:")
      #print("D: "+ " ".join(str(x) for x in P[0]) )
      #print("P: "+ " ".join(str(x) for x in P[1]) )
      #print("S: "+ " ".join(str(x) for x in P[2]) )
      c=1
      break
     if(P[1][i]>1):
      P = getPuissances(P,0,i+1)
      #print("RESOLUTION DE PUISSANCE:")
      #print("D: "+ " ".join(str(x) for x in P[0]) )
      #print("P: "+ " ".join(str(x) for x in P[1]) )
      #print("S: "+ " ".join(str(x) for x in P[2]) )
      c=1
      break
     ##print("found B")
     F=[]
     Pos=[]
     fxyz(P[2],i+1,3,F,Pos)
     ##print(F)
     ##print(Pos)
     #SENTENCE=B(F[0],F[1],F[2])
     SENTENCE=B(P,Pos[0],Pos[1],Pos[2])
     P=Place(P,SENTENCE,i-1,F,Pos,1)
     
     ####refine P
     P2=refineBraq(P,1)
     P2[0].reverse()
     P2[1].reverse()
     P2[2].reverse()
     #P3="".join(P2)
     P3=refineBraq(P2,2)
     P3[0].reverse()
     P3[1].reverse()
     P3[2].reverse()
     P=P3
     ##print(P)
     ##print(P)

     break

   except Exception as e:
     print("could not find variables for combinator B " + str(e))
     exit()    
   if P[2][i]=="C":
    try:
     if(P[0][i]>1):
      P = getDistances(P,0,i+1)
      #print("RESOLUTION DE DISTANCE:")
      #print("D: "+ " ".join(str(x) for x in P[0]) )
      #print("P: "+ " ".join(str(x) for x in P[1]) )
      #print("S: "+ " ".join(str(x) for x in P[2]) )
      c=0
      break
     if(P[1][i]>1):
      P = getPuissances(P,0,i+1)
      #print("RESOLUTION DE PUISSANCE:")
      #print("D: "+ " ".join(str(x) for x in P[0]) )
      #print("P: "+ " ".join(str(x) for x in P[1]) )
      #print("S: "+ " ".join(str(x) for x in P[2]) )
      c=0
      break    
     ##print(P)
     ##print(i)
     F=[]
     Pos=[]
     fxyz(P[2],i+1,3,F,Pos)
     ##print(F)
     ##print(Pos)
     SENTENCE=C(P,Pos[0],Pos[1],Pos[2])
     ##print(SENTENCE)
     P=Place(P,SENTENCE,i-1,F,Pos,1)
     
     ####refine P
     P2=refineBraq(P,1)
     P2[0].reverse()
     P2[1].reverse()
     P2[2].reverse()
     #P3="".join(P2)
     P3=refineBraq(P2,2)
     P3[0].reverse()
     P3[1].reverse()
     P3[2].reverse()
     P=P3
     ##print(P)
     break
    except:
     print("could not find variables for combinator C ")
     exit()

   if P[2][i]=="W":
    try:
     if(P[0][i]>1):
      P = getDistances(P,0,i+1)
      #print("RESOLUTION DE DISTANCE:")
      #print("D: "+ " ".join(str(x) for x in P[0]) )
      #print("P: "+ " ".join(str(x) for x in P[1]) )
      #print("S: "+ " ".join(str(x) for x in P[2]) )
      c=0
      break
     if(P[1][i]>1):
      P = getPuissances(P,0,i+1)
      #print("RESOLUTION DE PUISSANCE:")
      #print("D: "+ " ".join(str(x) for x in P[0]) )
      #print("P: "+ " ".join(str(x) for x in P[1]) )
      #print("S: "+ " ".join(str(x) for x in P[2]) )
      c=0
      break    
     ##print(P)
     ##print(i)
     F=[]
     Pos=[]
     fxyz(P[2],i+1,2,F,Pos)
     ##print(F)
     ##print(Pos)
     SENTENCE=W(P,Pos[0],Pos[1])
     ##print(SENTENCE)
     P=Place(P,SENTENCE,i-1,F,Pos,1)
     
     ####refine P
     P2=refineBraq(P,1)
     P2[0].reverse()
     P2[1].reverse()
     P2[2].reverse()
     #P3="".join(P2)
     P3=refineBraq(P2,2)
     P3[0].reverse()
     P3[1].reverse()
     P3[2].reverse()
     P=P3
     ##print(P)
     break
    except Exception as e:
     print("could not find variables for combinator W " + str(e))
     exit() 

   if P[2][i]=="G":
    try:
     ##print(i)
     F=[]
     Pos=[]
     fxyz(P[2],i+1,2,F,Pos)
     ##print(F)
     SENTENCE=C2(P,Pos[0],Pos[1])
     P=Place(P,SENTENCE,i-1,F,Pos,1)
     ####refine P
     P2=refineBraq(P,1)
     P2[0].reverse()
     P2[1].reverse()
     P2[2].reverse()
     #P3="".join(P2)
     P3=refineBraq(P2,2)
     P3[0].reverse()
     P3[1].reverse()
     P3[2].reverse()
     P=P3
     ##print(P)
     break
    except:
     print("could not find variables for combinator C* ")
     exit()

   if P[2][i]=="K":
    try:
     if(P[0][i]>1):
      P = getDistances(P,0,i+1)
      #print("RESOLUTION DE DISTANCE:")
      #print("D: "+ " ".join(str(x) for x in P[0]) )
      #print("P: "+ " ".join(str(x) for x in P[1]) )
      #print("S: "+ " ".join(str(x) for x in P[2]) )
      c=1
      break
     if(P[1][i]>1):
      P = getPuissances(P,0,i+1)
      #print("RESOLUTION DE PUISSANCE:")
      #print("D: "+ " ".join(str(x) for x in P[0]) )
      #print("P: "+ " ".join(str(x) for x in P[1]) )
      #print("S: "+ " ".join(str(x) for x in P[2]) )
      c=1
      break
     ##print("found B")
     F=[]
     Pos=[]
     fxyz(P[2],i+1,2,F,Pos)
     ##print(F)
     ##print(Pos)
     #SENTENCE=B(F[0],F[1],F[2])
     SENTENCE=K(P,Pos[0])
     P=Place(P,SENTENCE,i-1,F,Pos,1)
     
     ####refine P
     P2=refineBraq(P,1)
     P2[0].reverse()
     P2[1].reverse()
     P2[2].reverse()
     #P3="".join(P2)
     P3=refineBraq(P2,2)
     P3[0].reverse()
     P3[1].reverse()
     P3[2].reverse()
     P=P3
     ##print(P)
     ##print(P)

     break
    except Exception as e:
     print("could not find variables for combinator K "+str(e))
     exit()
     
   if P[2][i]=="S":
    try:
     F=[]
     Pos=[]
     fxyz(P,i+1,3,F,Pos)
     ##print(F)
     SENTENCE=S(F[0],F[1],F[2])
     P=Place(P,SENTENCE,i,F,Pos,1)
     ####refine P
     P2=refineBraq(P,1)
     P2.reverse()
     P3="".join(P2)
     P3=refineBraq(P3,2)
     P3.reverse()
     P="".join(P3)
     ##print(P)
     break
    except:
     print("could not find variables for combinator S ")
     exit()
   
  c=c+1
  print("SENTENCE: "+str("".join(P[2])))
  print("D: "+ " ".join(str(x) for x in P[0]) )
  print("P: "+ " ".join(str(x) for x in P[1]) )
  print("S: "+ " ".join(str(x) for x in P[2]) )
  #print(P)

  M=P[2]
  if getCombs(M)>0:
    c=1
 return P
##print(P)






# function to convert to superscript
def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(super_s),''.join(normal))
    return x.translate(res)


# function to convert to subscript
def get_sub(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans( ''.join(sub_s), ''.join(normal))
    return x.translate(res)



P=[]
D=[]
NP=[]
CC=[]



       
# 'bt_clear' function :This is used to clear 
# the input field
def bt_click(x): 
    global expression 
    expression = input_text.get() + x
    input_text.set(expression)
    expression=""

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
    P.clear()
    NP.clear()
    CC.clear()
    print(P)
 
# 'bt_equal':This method calculates the expression 
# present in input field
 
def bt_equal():
    P=[]
    D=[]
    NP=[]
    CC=[]
    print(input_text.get())
    super_s = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    sub_s = "₀₁₂₃₄₅₆₇₈₉"
    INPUT=input_text.get()

    for i in range(len(INPUT)):
        if INPUT[i] not in sub_s and INPUT[i] not in super_s:
            CC.append(INPUT[i])
    i=0
    while(i<len(INPUT)):
        spec=[]
        try:
            
            if INPUT[i+1] in super_s:
                for j in range(i+1,len(INPUT)):
                    if INPUT[j] not in super_s:
                	    i=j-1
                	    break
                    spec.append(get_super(INPUT[j]))
                if len(spec)>0:
                    NP.append( int("".join(spec)) )
                    D.append(1)          
        except:
        	err=1


        try:
            
            if INPUT[i+1] in sub_s:
                for j in range(i+1,len(INPUT)):
                    if INPUT[j] not in sub_s:
                	    i=j-1
                	    break
                    spec.append(get_sub(INPUT[j]))
                if len(spec)>0:
                    NP.append( 1 )
                    D.append( int("".join(spec)) )          
        except:
        	err=1


        if INPUT[i] not in sub_s and INPUT[i] not in super_s:
            NP.append( 1 )
            D.append(1)
            print(INPUT[i]+str(i)+" "+str(len(INPUT)))        	
        i=i+1
        '''
        if INPUT[i+1] not in sub_s and INPUT[i+1] not in super_s:
            NP.append( 1 )
            P.append( 1 )
        '''

 


    P.append(D)
    P.append(NP)
    P.append(CC)
    
    print(P)

    try:
        FF=P
        ####refine P
        P2=refineBraq(FF,1)
        P2[2].reverse()
        #P3="".join(P2)
        P3=refineBraq(P2,2)
        P3[2].reverse()
        #print("INPUT: "+"".join(P3[2]))
        #print("D: "+ " ".join(str(x) for x in P[0]) )
        #print("P: "+ " ".join(str(x) for x in P[1]) )
        #print("S: "+ " ".join(str(x) for x in P[2]) )
        #print("------SOLVING----- " )
        FF=P3
        FF=pars(FF)
        input_text.set(str("".join(FF[2])))
        print("RESULT SENTENCE: "+str("".join(FF[2])))
        print("D: "+ " ".join(str(x) for x in FF[0]) )
        print("P: "+ " ".join(str(x) for x in FF[1]) )
        print("S: "+ " ".join(str(x) for x in FF[2]) )
    except Exception as e:
        print(e)
        
    
    
 
expression = ""
 
# 'StringVar()' :It is used to get the instance of input field
 
input_text = StringVar()
 
# Let us creating a frame for the input field
 
input_frame = Frame(win, width=1000, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)
 
#Let us create a input field inside the 'Frame'
customFont = tkFont.Font(family='Raavi', size=20)
input_field = Entry(input_frame, font=customFont, textvariable=input_text, width=100, bg="#eee", bd=0, justify=LEFT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
 
#Let us creating another 'Frame' for the button below the 'input_frame'
 
btns_frame = Frame(win, width=500, height=400, bg="grey")
 
btns_frame.pack()
 
# first row
 
clear = Button(btns_frame, text = "RESET", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 1, padx = 1, pady = 1)
 
btnG = Button(btns_frame, text = "SOLVE", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: bt_equal()).grid(row = 1, column = 1,  padx = 1, pady = 1)


super_ss = "⁰¹²³⁴⁵⁶⁷⁸⁹"

U0 = Button(btns_frame, text = "x⁰", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("⁰")).grid(row = 0, column = 2, padx = 1, pady = 1)
U1 = Button(btns_frame, text = "x¹", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("¹")).grid(row = 0, column = 3, padx = 1, pady = 1)
U2 = Button(btns_frame, text = "x²", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("²")).grid(row = 0, column = 4, padx = 1, pady = 1)
U3 = Button(btns_frame, text = "x³", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("³")).grid(row = 0, column = 5, padx = 1, pady = 1)
U4 = Button(btns_frame, text = "x⁴", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("⁴")).grid(row = 0, column = 6, padx = 1, pady = 1)
U5 = Button(btns_frame, text = "x⁵", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("⁵")).grid(row = 0, column = 7, padx = 1, pady = 1)
U6 = Button(btns_frame, text = "x⁶", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("⁶")).grid(row = 0, column = 8, padx = 1, pady = 1)
U7 = Button(btns_frame, text = "x⁷", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("⁷")).grid(row = 0, column = 9, padx = 1, pady = 1)
U8 = Button(btns_frame, text = "x⁸", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("⁸")).grid(row = 0, column = 10, padx = 1, pady = 1)
U9 = Button(btns_frame, text = "x⁹", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("⁹")).grid(row = 0, column = 11, padx = 1, pady = 1)

sub_ss = "₀₁₂₃₄₅₆₇₈₉"
S0 = Button(btns_frame, text = "x₀", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("₀")).grid(row = 1, column = 2, padx = 1, pady = 1)
S1 = Button(btns_frame, text = "x₁", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("₁")).grid(row = 1, column = 3, padx = 1, pady = 1)
S2 = Button(btns_frame, text = "x₂", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("₂")).grid(row = 1, column = 4, padx = 1, pady = 1)
S3 = Button(btns_frame, text = "x₃", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("₃")).grid(row = 1, column = 5, padx = 1, pady = 1)
S4 = Button(btns_frame, text = "x₄", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("₄")).grid(row = 1, column = 6, padx = 1, pady = 1)
S5 = Button(btns_frame, text = "x₅", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("₅")).grid(row = 1, column = 7, padx = 1, pady = 1)
S6 = Button(btns_frame, text = "x₆", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("₆")).grid(row = 1, column = 8, padx = 1, pady = 1)
S7 = Button(btns_frame, text = "x₇", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("₇")).grid(row = 1, column = 9, padx = 1, pady = 1)
S8 = Button(btns_frame, text = "x₈", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("₈")).grid(row = 1, column = 10, padx = 1, pady = 1)
S9 = Button(btns_frame, text = "x₉", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_click("₉")).grid(row = 1, column = 11, padx = 1, pady = 1)






win.mainloop()
