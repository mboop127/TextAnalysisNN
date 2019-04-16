import random
import os

win = 0
fail = 0
count = 0
rate = 0
GenInc = 0

LayerOne = []
LayerTwo = []
LayerThree = []
LayerFour = []
Analysis = []
WordListInts = []
OutputOrder = []

LayerFourNeuron2 = []

OutputLength = 25

fitness = None

A = 0
B = 100
C = B**2
D = 0
E = 0
F = int(10000/OutputLength)
G = 0
H = 7
J = 0
K = 0
L = 0
chance = .01
MagUpper = 1.025
MagLower = .975

def mutate(list):
    for i in range(len(list)):
        if random.random() < chance:
            list[i] = float(list[i]) * random.uniform(MagUpper,MagLower)

def Vmutate(variable):
    if random.random() < chance:
        variable = variable * random.uniform(MagUpper,MagLower)

def normalize(list):
    for i in range(len(list)):
        list[i] = int(list[i])

if os.path.isfile("GenCount.txt"):
    f = open("GenCount.txt")
    Gen = f.read()
    f.close()
    Gen = int(Gen)
    GenInc = Gen

while 0 == 0:
    LayerOne = []
    LayerTwo = []
    LayerThree = []
    LayerFour = []
    Analysis = []
    LayerFourNeuron2 = []
    AnalyzedLine= []
    K = 0

    #generate or read

    if os.path.isfile("OutputOrder.txt"):
        f = open("OutputOrder.txt")
        OutputOrder = f.read().split(',')
        f.close()
        OutputOrder = OutputOrder[:-1]
    else:
        OutputOrder = [x for x in range(OutputLength)]

    if os.path.isfile("WordList.txt"):
        f = open("WordList.txt")
        WordList = f.read().split(',')
        f.close()
        WordList = WordList[:-1]

    if os.path.isfile("WordListInts.txt"):
        f = open("WordListInts.txt")
        WordListInts = f.read().split(',')
        f.close()
        WordListInts = WordListInts[:-1]
    else:
        WordListInts = [random.randint(0,(len(WordList)-1)) for x in range(len(WordList))]

    if os.path.isfile("LayerThreeNeuron1.txt"):
        f = open("LayerThreeNeuron1.txt")
        LayerThreeNeuron1 = f.read().split(',')
        f.close()
        LayerThreeNeuron1 = LayerThreeNeuron1[:-1]

    if os.path.isfile("LayerThreeNeuron2.txt"):
        f = open("LayerThreeNeuron2.txt")
        LayerThreeNeuron2 = f.read().split(',')
        f.close()
        LayerThreeNeuron2 = LayerThreeNeuron2[:-1]

    else:
        LayerThreeNeuron1 = [random.randint(1000,100000) for x in range(C)]
        LayerThreeNeuron2 = [random.randint(1,1000) for x in range(C)]

        f = open("LayerThreeNeuron1.txt", "w+")
        for i in range(len(LayerThreeNeuron1)):
            f.write(str(LayerThreeNeuron1[i]) + ',')
        f.close()

        f = open("LayerThreeNeuron2.txt", "w+")
        for i in range(len(LayerThreeNeuron2)):
            f.write(str(LayerThreeNeuron2[i]) + ',')
        f.close()

    if os.path.isfile("LayerFourNeuron1.txt"):
        f = open("LayerFourNeuron1.txt")
        LayerFourNeuron1 = f.read().split(',')
        LayerFourNeuron1 = LayerFourNeuron1[:-1]

    else:
        LayerFourNeuron1 = [random.randint(0,1000000) for x in range(C)]
        f = open("LayerFourNeuron1.txt", "w+")
        for i in range(len(LayerFourNeuron1)):
            f.write(str(LayerFourNeuron1[i]) + ',')
        f.close()


    if os.path.isfile("GenCount.txt"):
        f = open("GenCount.txt")
        Gen = f.read()
        f.close()
        Gen = int(Gen)
    else:
        Gen = 0

    if os.path.isfile("Variables.txt"):
        f = open("Variables.txt")
        H = float(f.readline())
        MagLower = float(f.readline())
        MagUpper = float(f.readline())
        chance = float(f.readline())
        f.close()
    else:
        H = random.randint(0,30)

    Vmutate(H)
    Vmutate(MagLower)
    Vmutate(MagUpper)
    Vmutate(chance)

    mutate(WordListInts)
    mutate(LayerThreeNeuron1)
    mutate(LayerFourNeuron2)
    mutate(LayerFourNeuron1)

    if random.random() < chance:
        random.shuffle(OutputOrder)

    #read and analyze function
    text_file = open("1.txt", "r")
    LayerOne = text_file.read().split(',')
    text_file.close()
    LayerOne = LayerOne[:-1]

    normalize(WordListInts)
    normalize(LayerOne)
    normalize(LayerFourNeuron1)
    normalize(LayerFourNeuron2)
    normalize(LayerThreeNeuron1)
    normalize(OutputOrder)


    while A < 100:
        while LayerOne[K] != 35 and LayerOne[K] != 27:
            K = random.randint(0,(len(LayerOne) - 100))
        for i in range(K, (K + 100)):
            LayerTwo.append(LayerOne[i]*LayerOne[A]+(A/1000))
        A = A+1
    A = 0

    for i in range(K, (K + 100)):
        AnalyzedLine.append(LayerOne[i])

    f = open("TempPrint.txt" , "w+")
    for i in range(len(AnalyzedLine)):
        f.write(str(AnalyzedLine[i]) + ',')
    f.close()

    with open('TempPrint.txt', 'r') as file:
        filedata = file.read()

    filedata = filedata.replace(',','~')
    filedata = filedata.replace('36',',')
    filedata = filedata.replace('35','\n')
    filedata = filedata.replace('34','"')
    filedata = filedata.replace('33','-')
    filedata = filedata.replace('32',':')
    filedata = filedata.replace('31',';')
    filedata = filedata.replace('30',' ')
    filedata = filedata.replace('29','?')
    filedata = filedata.replace('28','!')
    filedata = filedata.replace('27','.')
    filedata = filedata.replace('26','z')
    filedata = filedata.replace('25','y')
    filedata = filedata.replace('24','x')
    filedata = filedata.replace('23','w')
    filedata = filedata.replace('22','v')
    filedata = filedata.replace('21','u')
    filedata = filedata.replace('20','t')
    filedata = filedata.replace('19','s')
    filedata = filedata.replace('18','r')
    filedata = filedata.replace('17','q')
    filedata = filedata.replace('16','p')
    filedata = filedata.replace('15','o')
    filedata = filedata.replace('14','n')
    filedata = filedata.replace('13','m')
    filedata = filedata.replace('12','l')
    filedata = filedata.replace('11','k')
    filedata = filedata.replace('10','j')
    filedata = filedata.replace('9','i')
    filedata = filedata.replace('8','h')
    filedata = filedata.replace('7','g')
    filedata = filedata.replace('6','f')
    filedata = filedata.replace('5','e')
    filedata = filedata.replace('4','d')
    filedata = filedata.replace('3','c')
    filedata = filedata.replace('2','b')
    filedata = filedata.replace('1','a')
    filedata = filedata.replace('~','')

    print(filedata)
    print()
    print()

    filedata = None

    normalize(LayerTwo)

    for i in range(len(LayerFourNeuron1)):
        LayerThree.append(float(LayerThreeNeuron1[i])/(float(LayerTwo[i])*(float(LayerThreeNeuron2[i]))))

    for i in range(B):
        while J < 100:
            LayerFourNeuron2.append(LayerOne[i]/(i + 1))
            J = J+1
        J = 0

    for i in range(C):
        LayerFourNeuron1[i] = int(LayerFourNeuron1[i])

    for i in range(C):
        LayerFour.append(LayerFourNeuron1[i]/LayerFourNeuron2[i])

    for i in range(C):
        while LayerFour[i] > 10000:
            LayerFour[i] = (LayerFour[i]/H)

    normalize(LayerFour)

    while D < OutputLength:
        for i in range(E,F):
            G = G + (LayerThree[LayerFour[i]])
        Analysis.append(G)
        F = int(F + (10000/OutputLength))
        E = int(E + (10000/OutputLength))
        D = D+1
        G = 0
    D = 0
    F = int(10000/OutputLength)
    E = 0

    for i in range(len(Analysis)):
        while Analysis[i] > len(WordList):
            Analysis[i] = (Analysis[i] / H)

    f = open("Analysis.txt" , "w+")
    for i in range(len(Analysis)):
        Analysis[i] = int(Analysis[i])
        f.write(str(Analysis[OutputOrder[i]]) + ',')
    f.close()


    #temporary test of word frequencies
    f = open("AnalysisRaw.txt" , "a")
    for i in range(len(Analysis)):
        Analysis[i] = int(Analysis[i])
        f.write(str(Analysis[i]) + '\n')
    f.close()

    filedata = None
    # Read in the file
    with open('Analysis.txt', 'r') as file:
        filedata = file.read()

    L = len(WordList)
    for i in range(len(WordList)):
        if WordListInts[i] > len(WordList):
            WordListInts[i]  = len(WordList) - 1
        filedata = filedata.replace(str(L), WordList[WordListInts[i]])
        L = L - 1
    L = 0

    filedata = filedata.replace(',', ' ')

    with open('Analysis.txt', 'w+') as file:
        file.write(filedata)
    print(filedata)

    while fitness != 'a' and fitness != 'd':
        print("Pass (a) or Fail (d)?")
        fitness = input()

    if fitness == 'a':

        Gen = Gen + 1
        GenInc = GenInc + 1
        count = count + 1
        win = win + 1

        f = open("GenCount.txt", "w+")
        f.write(str(Gen))
        f.close()

        f = open("LayerThreeNeuron1.txt", "w+")
        for i in range(len(LayerThreeNeuron1)):
            f.write(str(LayerThreeNeuron1[i]) + ',')
        f.close()

        f = open("LayerThreeNeuron2.txt", "w+")
        for i in range(len(LayerThreeNeuron2)):
            f.write(str(LayerThreeNeuron2[i]) + ',')
        f.close()

        f = open("LayerFourNeuron1.txt", "w+")
        for i in range(len(LayerFourNeuron1)):
            f.write(str(LayerFourNeuron1[i]) + ',')
        f.close()

        f = open("WordListInts.txt", "w+")
        for i in range(len(WordListInts)):
            f.write(str(WordListInts[i]) + ',')
        f.close()

        f = open("OutputOrder.txt", "w+")
        for i in range(len(OutputOrder)):
            f.write(str(OutputOrder[i]) + ',')
        f.close()

        f = open("Variables.txt" , "w+")
        f.write(str(H)  + "\n" + str(MagLower) + "\n" + str(MagUpper) + "\n" + str(chance))
        f.close()

    if fitness == 'd':
        fail = fail + 1
        count = count + 1

#    if count == 100:
 #       rate = 100((int(win) + 1) / (int(count) + 1))
  #      print(str(rate) + "% sucess in the last 100 generations")
   #     count = 0
    #    fail = 0
     #   win = 0

    if GenInc == 10:
        GenInc = 0
        f = open(str(Gen) + ".txt.", "w+")
        f.write(filedata)
        f.close()

    fitness = None
