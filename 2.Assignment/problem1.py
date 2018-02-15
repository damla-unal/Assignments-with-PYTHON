import sys
inputfile=sys.argv[1]
infile=open(inputfile,"r")

def avgFirstThreeDigit(ListIntegers):

    for i in range(len(ListIntegers)):
        first_threedigit=ListIntegers[i][0:3]
        first_threedigit=list(first_threedigit)

        total=0
        for number in first_threedigit:
            total+=int(number)
        liste.append(total/3)

    print(liste)

liste=[]
ListIntegers=[]
for line in infile.readlines():
    ListIntegers.extend(line.rstrip("\n").split(";"))

    for i in range(len(ListIntegers)//2):
        ListIntegers[i],ListIntegers[-(1+i)]=ListIntegers[-(1+i)],ListIntegers[i]



avgFirstThreeDigit(ListIntegers)


infile.close()
