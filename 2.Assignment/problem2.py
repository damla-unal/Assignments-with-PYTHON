import sys
inputfile=sys.argv[1]
infile=open(inputfile,"r")

def calculateTotalCost(list):
    ResultList=[]
    for i in list:
        i[0]=int(i[0])
        i[1]=int(i[1])
        i[2]=float(i[2])
        ResultList.append(i[0]+i[1]*10+i[0]*10*i[2])
    return ResultList


def displayCosts(list):
    displayList=calculateTotalCost(list)
    print("The total cost of each house:",sep="\n")

    for i in range(len(displayList)):
        print("{}.house's total cost is {}".format(i+1,displayList[i]))


def selectBestBuy(list):
    BestBuyList=calculateTotalCost(list)
    bestchoice=BestBuyList[0]

    for elm in BestBuyList:
        if elm<bestchoice:
            bestchoice=elm
    print("You should select {}. house whose total cost is {}".format(BestBuyList.index(bestchoice)+1,bestchoice))


bulletList=[]
for line in infile.readlines():
    bulletList.append(line.rstrip("\n").split(" "))


displayCosts(bulletList)
selectBestBuy(bulletList)


infile.close()
