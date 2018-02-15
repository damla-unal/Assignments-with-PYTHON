import numpy as np
import matplotlib.pyplot as plt
import sys
first_file=sys.argv[1]
parametre=sys.argv[2].split(",")



def retrieveData(filename,listofnominee):
    file=open(filename,"r")
    outfile=open("retrievedData.txt","w")


    global parametre2
    parametre2=[]
    parametre2.extend(listofnominee)


    global ilksatır
    ilksatır=file.readline().rstrip("\n").split(",")
    kalan=file.readlines()


    global liste
    global int_oy
    liste=[]
    for k in kalan:
        liste.append(k.rstrip("\n").split(","))


    oylar=[]

    for i in listofnominee:
        y=ilksatır.index(i)
        for j in kalan:
            j=j.rstrip("\n").split(",")
            oylar.append(j[y])
    int_oy=[]
    for b in oylar:
        b=int(b)
        int_oy.append(b)
    outfile.writelines(str(int_oy))
    return int_oy


    outfile.close()
retrieveData(first_file,parametre)


def DispBarPlot():

    eyalet=[]
    for data in liste:
        eyalet.append(data[0])

    if len(int_oy)==102:
        liste1=[]
        x=sum(int_oy[:51])
        y=sum(int_oy[51:102])
        liste1.append(x)
        liste1.append(y)


    elif 102<len(int_oy)<204:
        liste1=[]
        x=sum(int_oy[:51])
        y=sum(int_oy[51:102])
        z=sum(int_oy[102:154])
        liste1.append(x)
        liste1.append(y)
        liste1.append(z)


    else:
        liste1=[]
        x=sum(int_oy[:51])
        y=sum(int_oy[51:102])
        z=sum(int_oy[102:154])
        t=sum(int_oy[154:204])
        liste1.append(x)
        liste1.append(y)
        liste1.append(z)
        liste1.append(t)


    sort=sorted(liste1)

    liste2=[]
    liste2.extend(sort[-2:])


    isimler=[]
    for i in liste2:
        h=liste1.index(i)
        isimler.append(parametre2[h])

    sözlük={}
    a=[]
    b=[]
    for data in liste:
        a.append(data[ilksatır.index(isimler[0])])
        b.append(data[ilksatır.index(isimler[1])])
    a1=[int(i) for i in a]
    b1=[int(i) for i in b]



    sözlük[isimler[0]]=a1
    sözlük[isimler[1]]=b1



        # data to plot

    s_obama = sözlük[isimler[1]]
    s_romney =sözlük[isimler[0]]

# create plot
    #fig, ax = plt.subplots()
    index = np.arange(len(s_obama))
    bar_width = 0.35
    opacity = 0.8



    #fig = plt.figure()
    y1 = plt.bar(index, s_romney, bar_width,
                 alpha=opacity,
                 color='r',
                 label=isimler[0])

    y2 = plt.bar(index + bar_width, s_obama, bar_width,
                 alpha=opacity,
                 color='b',
                 label=isimler[1])

    plt.xlabel('States')
    plt.ylabel('Vote Count')
    plt.xticks(index + bar_width, (eyalet),rotation=90)
    plt.legend()
    plt.savefig("ComparativeVotes.pdf",bbox_inches="tight")

    plt.tight_layout()
    plt.close()

DispBarPlot()

def compareVoteonBar():


    index=[]
    for t in parametre2:
        index.append(ilksatır.index(t))


    if len(int_oy)==51*len(index):


        x=sum(int_oy[:51])
        y=sum(int_oy[51:102])
        z=sum(int_oy[102:153])
        t=sum(int_oy[153:204])


    total=sum(int_oy)


    x1=round(x*100/total,3)

    y1=round(y*100/total,3)

    z1=round(z*100/total,3)

    t1=round(t*100/total,3)


    objects = [x1,y1,z1,t1]
    y_pos = np.arange(len(objects))
    performance = [x1,y1,z1,t1]

    for i in parametre2:
        if parametre2.index(i)==0:
            plt.bar(y_pos, performance, align='center', alpha=0.7,color="rbyc",label="{}".format(i))

        elif parametre2.index(i)==1:
            plt.bar(y_pos, performance, align='center', alpha=0.7,color="rbyc",label="{}".format(i))

        elif parametre2.index(i)==2:
            plt.bar(y_pos, performance, align='center', alpha=0.7,color="rbyc",label="{}".format(i))

        elif parametre2.index(i)==3:
            plt.bar(y_pos, performance, align='center', alpha=0.7,color="rbyc",label="{}".format(i))


    #fig = plt.figure()
    plt.xticks(y_pos, objects)
    plt.ylabel('Vote Percentages')
    plt.title('Nominees')
    plt.legend()
    plt.savefig("CompVotePercs.pdf")

    plt.close()


compareVoteonBar()


def obtainHistogram(liste):

    str_liste=[]
    for i in liste:
        str_liste.append(str(i))

    for s in str_liste:
        if len(s)==1:
            str_liste.remove(s)
            a= "0"+s
            str_liste.append(a)

    digits=[]
    for t in str_liste:
        digits.append(t[-1])
        digits.append(t[len(t)-2])


    sıfır=digits.count("0")
    bir=digits.count("1")
    iki=digits.count("2")
    üc=digits.count("3")
    dort=digits.count("4")
    bes=digits.count("5")
    altı=digits.count("6")
    yedi=digits.count("7")
    sekız=digits.count("8")
    dokuz=digits.count("9")

    #global sıklık
    sıklık=[]
    sıklık.append(sıfır/(len(liste)*2))
    sıklık.append(bir/(len(liste)*2))
    sıklık.append(iki/(len(liste)*2))
    sıklık.append(üc/(len(liste)*2))
    sıklık.append(dort/(len(liste)*2))
    sıklık.append(bes/(len(liste)*2))
    sıklık.append(altı/(len(liste)*2))
    sıklık.append(yedi/(len(liste)*2))
    sıklık.append(sekız/(len(liste)*2))
    sıklık.append(dokuz/(len(liste)*2))

    return sıklık




from pylab import *

def plotHistogram():

    global s
    global s12
    t = arange(0,10,1)
    s5 = np.mean(obtainHistogram(int_oy))
    s=[s5 for i in range(0,10)]
    s12 = obtainHistogram(int_oy)

    plt.plot(t, s,"--",color="g",label="Mean")
    plt.plot(t, s12,color="r",label="Digit Dist.")

    plt.xlabel('Digits')
    plt.ylabel('Distribution')
    plt.title('Histogram of least sign. digits')
    plt.legend()
    plt.savefig("Histogram.pdf")

    close()

plotHistogram()


#import numpy as np

def plotHistogramWithSample():
    #1.grafik

    s4=np.random.randint(100, size=10)
    t = arange(0,10,1)
    s5 = 0.1
    s=[s5 for i in range(0,10)]
    s2 =obtainHistogram(s4)
    plot(t, s,"--",color="g",label="Mean")
    plot(t, s2,color="r",label="Digit Dist.")

    xlabel('Digits')
    ylabel('Distribution')
    title('Histogram of least sign. digits - Sample:1')
    plt.legend()
    plt.savefig("HistogramofSample1.pdf",bbox_inches="tight")

    close()

    #2.grafik

    x1=np.random.randint(100, size=50)
    t = arange(0,10,1)
    s5 = 0.1
    s=[s5 for i in range(0,10)]
    s2 =obtainHistogram(x1)
    plot(t, s,"--",color="g",label="Mean")
    plot(t, s2,color="b",label="Digit Dist.")

    xlabel('Digits')
    ylabel('Distribution')
    title('Histogram of least sign. digits - Sample:2')
    plt.legend()
    plt.savefig("HistogramofSample2.pdf",bbox_inches="tight")

    close()

    #3.grafik

    x2=np.random.randint(100, size=100)
    t = arange(0,10,1)
    s5 = 0.1
    s=[s5 for i in range(0,10)]
    s2 =obtainHistogram(x2)
    plot(t, s,"--",color="g",label="Mean")
    plot(t, s2,color="y",label="Digit Dist.")

    xlabel('Digits')
    ylabel('Distribution')
    title('Histogram of least sign. digits - Sample:3')
    plt.legend()
    plt.savefig("HistogramofSample3.pdf",bbox_inches="tight")

    close()

    #4.grafik

    x3=np.random.randint(100, size=1000)
    t = arange(0,10,1)
    s5 = 0.1
    s=[s5 for i in range(0,10)]
    s2 =obtainHistogram(x3)
    plot(t, s,"--",color="g",label="Mean")
    plot(t, s2,color="g",alpha=0.2,label="Digit Dist.")

    xlabel('Digits')
    ylabel('Distribution')
    title('Histogram of least sign. digits - Sample:4')
    plt.legend()
    plt.savefig("HistogramofSample4.pdf",bbox_inches="tight")

    close()

    #5.grafik

    x8=np.random.randint(100, size=10000)
    t = arange(0,10,1)
    s5 = 0.1
    s=[s5 for i in range(0,10)]
    s2 =obtainHistogram(x8)
    plot(t, s,"--",color="g",label="Mean")
    plot(t, s2,color="m",label="Digit Dist.")

    xlabel('Digits')
    ylabel('Distribution')
    title('Histogram of least sign. digits - Sample:5')
    plt.legend()
    plt.savefig("HistogramofSample5.pdf",bbox_inches="tight")

    close()

plotHistogramWithSample()


def calculateMSE(list_1,list_2):
    global MSE
    MSE=[]
    for i in range(len(list_1)):
        MSE.append((list_1[i]-list_2[i])**2)
    return sum(MSE)



def compareMSEs():

    step9=[]
    for i in range(10000):
        random1=np.random.randint(100,size=len(int_oy))
        step9.append(obtainHistogram(random1))

    Mses=[]
    for a in step9:
         Mses.append(calculateMSE(a,[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]))


    global büyük
    global küçük
    büyük=[]
    küçük=[]
    for m in Mses:
        if sum(MSE)<=m:
            büyük.append(m)
        elif sum(MSE)>m:
            küçük.append(m)



compareMSEs()

answer=open("myAnswer.txt","w")

print("MSE value of 2012 USA election is {}".format(calculateMSE(s12,s)))
answer.write("MSE value of 2012 USA election is {}\n".format(calculateMSE(s12,s)))
print("The number of MSE of random samples which are larger than or equal to USA election MSE is {}".format(len(büyük)))
answer.write("The number of MSE of random samples which are larger than or equal to USA election MSE is {}\n".format(len(büyük)))
print("The number of MSE of random samples which are smaller than USA election MSE is {}".format(len(küçük)))
answer.write("The number of MSE of random samples which are smaller than USA election MSE is {}\n".format(len(küçük)))
print("2012 USA election rejection level p is {}".format(len(küçük)/10000))
answer.write("2012 USA election rejection level p is {}\n".format(len(küçük)/10000))

if len(büyük)<=500:
    print("Finding: We reject the null hypothesis at the p={} level".format(format(len(küçük)/10000)))
    answer.write("Finding: We reject the null hypothesis at the p={} level\n".format(format(len(küçük)/10000)))

else:
    print("Finding: There is no statistical evidence to reject null hypothesis")
    answer.write("Finding: There is no statistical evidence to reject null hypothesis\n")

answer.close()
































