#-----------------Document Reader-------------------------#
# Line - (string)
#LINE - (numpy.darray)
filename="33215-00GULFWHITTENBURG135PAYDECK(3).txt"
f=open(filename,"r")
LINE=[]
for line in f:
    LINE=np.append(LINE,line)
f.close()

p=0   # prints the whole text file if p=1
if p==1:
   for i in range(len(LINE)):
       print(LINE[i])

#--------------------------------------------------------#

#------------------Line Delimiter------------------------#
# Finds a phrase in a specified line and prints it
# nile - split up LINE
# phrases - words that mark lines not wanted (array of strings)


#print(type(LINE[4]))
#formatted=str(LINE[4])
#print(type(phrases[3]))
#print(type(formatted))


def match(x,y):
# searches array x and array y to see if theres a match
# and returns true if there is a match
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i]==y[j]:
                return True

delimit=1 # delimits text file if delimit=1
phrases=["Taxpayer","TypeOwner","Pay","PAY","DCP","Exhibit","Meter","\\pitlilesrv0l", " ","Page","A.RPT"]
if delimit==1:
    for i in range(len(LINE)):
        nile=LINE[i]
        splitline=nile.split()
        if match(splitline,phrases)!=True: 
            print(LINE[i])