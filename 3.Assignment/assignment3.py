#------------------------------------------------------------#
# Student Name:Damla Nur Ünal
# Student ID:21527511
# BBM103 Introduction to Programming Laboratory I, Fall 2016
# Assignment 3: Mission: Save the Earth
#------------------------------------------------------------#


import sys


dictionary=open(sys.argv[1],"r")
binarian_transmission=open(sys.argv[2],"r")
peace_message=open(sys.argv[3],"r")
binarian_message=open(sys.argv[4],"w")
computations=open(sys.argv[5],"w")
message=open(sys.argv[6],"w")


#mission1
dict1={}
for items in dictionary.readlines():
    listdict=items.rstrip().split(" ")
    dict1[listdict[0]]=listdict[1]


liste=[]
liste1=[]
for item in binarian_transmission.readlines():
    liste.extend(item.strip(" ").rstrip("\n").split(" \n"))

for i in liste:
    if i[0]!="#":
        liste1.append(i)

liste2=[]
for elm in liste1:
    if elm[0]!="+":
        liste2.append(elm)

for d in liste2:
    t=d.split(" ")
    print(" ")
    binarian_message.write(" "+"\n")


    for r in t:
        if r in dict1:
            r=dict1[r]
        print(r,end=" ")
        binarian_message.write(str(r)+" ")


#mission2


from decimal import Decimal
def ly_to_km(distance):
    a=9.4607e+12 * distance
    return "{:.6e}".format(Decimal(a))


liste3=[]
for i in liste:
    if i[0]=="+":
        liste3.append(i)
print("\n")


print("Data about Binarian planet:")
computations.write("Data about Binarian planet:"+"\n")
for k in liste3:
    x=k.split(" ")


    for t in range(len(x)):
        try:
            if dict1[x[t]]=="distance":
                binary=x[t+1]
                distance=int(binary,2)
                a=(ly_to_km(distance))


            elif dict1[x[t]]=="temperature":
                binary=x[t+1]
                b=float(int(binary,2))

            elif dict1[x[t]]=="orbital-speed":
                binary=x[t+1]
                c=float(int(binary,2))

        except:
            pass

print("Distance from the Earth: ",a,"km")
computations.write("Distance from the Earth: "+str(a)+" km"+"\n")
print("Planet temperature: ",b,"degrees Celsius")
computations.write("Planet temperature: "+str(b)+" degrees Celsius"+"\n")
print("Orbital speed: ",c,"km/s")
computations.write("Orbital speed: "+str(c)+" km/s"+"\n")




#mission3

items=[]
for line in peace_message.readlines():
    items.extend(line.strip(" ").rstrip("\n").split("\n"))


new_items=[el.rstrip('\'\"-,.:;!?') for el in items]


yeni=[]
for item in new_items:
    yeni.append(item.split(" "))


x=[]
for y in yeni:
    x.append([i.strip('\'\"-,.:;!?') for i in y])


def decimal_to_binary(n):
    return bin(int(n))[2:]


for item in x:
    for i,items in enumerate(item):
        if items.isnumeric()==True:
            item[i]=decimal_to_binary(items)



def reverse_dict(sözlük):

    dict2=dict((y,x) for x,y in sözlük.items())
    return dict2

def english_to_binarian():

    for item in x:
        l=[]
        for i in item:
            i1=i.lower()
            if i1 in reverse_dict(dict1):
                i=reverse_dict(dict1)[i1]
            l.append(i)

        print(" ")
        message.write(" "+"\n")
        for z in l :
            print("".join(z),end=" ")
            message.write(str("".join(z))+" ")

english_to_binarian()


dictionary.close()
binarian_transmission.close()
peace_message.close()
binarian_message.close()
computations.close()
message.close()
