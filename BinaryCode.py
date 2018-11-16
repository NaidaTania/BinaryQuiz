"""
Created on Thu Oct 12 21:18:50 2017

@author: NaidaTania
"""

import random

print("Welcome to Binary Quiz!")
roundNo = int(input("How many qns are we playing today?\n>> "))
denom = roundNo
if roundNo <= 0:
    print("Lazy bum!")
    roundNo = -1
else: 
    print("Specific qn type? <from 0 to 7, -1 if no specific type>",end="")
    qnType = int(input(">> "))

score = 0

def biDecConv (binaryList):
    '''
    biDecConv (binaryList)
    
    This function converts normal binary to decimal
    
    @binaryList A list of binary numbers to be converted
    
    return decimal value
    '''
    maxIndex = len(binaryList)-1
    for digit in binaryList:
        digitIndex = binaryList.index(digit)
        if digit == 1:
            binaryList[digitIndex] = 2**(maxIndex-digitIndex)
    deci = sum(binaryList)
    return deci

def decBiConv (num):
    '''
    decBiConv (num)
    
    This function converts decimal to normal binary
    
    @num Decimal number to be converted
    
    return A list of binary
    '''
    resultList = []
    if num == 0:
        return [0,0,0,0,0,0,0,0]
    elif num < 0 :
        num = -(num)
    for power in range(-7,1):
        power*=(-1)
        if num - 2**(power) >= 0:
            resultList.insert(len(resultList),1)
            num -= 2**power
        else:
            resultList.insert(len(resultList),0)
    return resultList

def oneSConv(binaryList):
    '''
    oneSConv (binaryList)
    
    This function converts normal binary to 1s complement binary
    
    @binaryList A list of binary numbers to be converted
    
    return A list of binary in 1s complement
    '''
    for index in range(0,len(binaryList)):
        if binaryList[index] == 0:
            binaryList[index] = 1
        else:
            binaryList[index] = 0
    return binaryList
    
def twoSConv(binaryList):
    '''
    twoSConv (binaryList)
    
    This function converts 1s complement to 2s complement binary
    
    @binaryList A list of binary numbers to be converted
    
    return A list of binary in 2s complement
    '''
    passOn = 1
    for revInd in range(-len(binaryList)+1,1):
        binaryList[-revInd] += passOn
        if binaryList[-revInd] == 2:
            binaryList[-revInd] = 0
            passOn = 1
        else:
            passOn = 0
            #print('2s',binaryList)
    return binaryList
            
def revTwoSConv(binaryList):
    '''
    biDecConv (binaryList)
    
    This function converts 2s complement binary to decimal
    
    @binaryList A list of binary numbers to be converted
    
    return decimal value
    '''
    passOn = 1
    for revInd in range(-len(binaryList)+1,1):
        binaryList[-revInd] -= passOn
        #print('2s',binaryList)
        if binaryList[-revInd] < 0:
            #print('into loop!')
            binaryList[-revInd] = 1
            passOn = 1
            #print('2s',binaryList)
            #print('2s',binaryList)
        else:
            passOn = 0
    return binaryList
        
def randNum ():
    '''
    randNum ()
    
    This function generates random positive number from 0 to 255
    
    return A positive integer
    '''
    return random.randint(0,255)

def randNumNeg():
    '''
    randNumNeg()
    
    This function generates random negative number from -1 to -128
    
    return A negative integer
    '''
    return random.randint(-128,-1)


while roundNo > 0:
    
    if qnType >= 0 and qnType<=7:
        qnNum = qnType
    else:
        #Random number used to generate questions randomly
        qnNum = random.randint(0,7)
    
    print()
    
    if qnNum == 0:
        #Positive decimal to binary
        qn = randNum()
        trueAns = decBiConv (qn)
        trueAnsStr = ''.join([str(x) for x in trueAns])
        print("Find the binary of", qn, end="")
        answer = input(">> ")
        point = 0
        for x,y in zip(answer,trueAns):
            if int(x) == y:
                point += 1
        if point == 8:
            print("Answer:", trueAnsStr)
            print("Eyy you got it right!")
            score += 1
        else:
            print("Answer:", trueAnsStr)
            print("Crap, you got it wrong. Next!")
    
    if qnNum == 1:
        #Negative decimal (1s) to binary
        qn = randNum()*-1
        trueAns = oneSConv(decBiConv (qn))
        trueAnsStr = ''.join([str(x) for x in trueAns])
        print("Find the 1s binary of", qn, end="")
        answer = input(">> ")
        point = 0
        for x,y in zip(answer,trueAns):
            if int(x) == y:
                point += 1
        if point == 8:
            print("Answer:", trueAnsStr)
            print("Eyy you got it right!")
            score += 1
        else:
            print("Answer:", trueAnsStr)
            print("Crap, you got it wrong. Next!")
    
    if qnNum == 2:
        #Negative decimal (2s) to binary
        qn = randNumNeg()
        trueAns = twoSConv(oneSConv(decBiConv (qn)))
        trueAnsStr = ''.join([str(x) for x in trueAns])
        print("Find the 2s binary of", qn, end="")
        answer = input(">> ")
        point = 0
        for x,y in zip(answer,trueAns):
            if int(x) == y:
                point += 1
        if point == 8:
            print("Answer:", trueAnsStr)
            print("Eyy you got it right!")
            score += 1
        else:
            print("Answer:", trueAnsStr)
            print("Crap, you got it wrong. Next!")
    
    if qnNum == 3:
        #binary(normal) to decimal
        qn = decBiConv(randNum())
        qnStr = ''.join([str(x) for x in qn])
        trueAns = biDecConv (qn)
        print("Find the decimal of", qnStr, end="")
        answer = input(">> ")
        if int(answer) == trueAns:
            print("Answer:", trueAns)
            print("Eyy you got it right!")
            score += 1
        else:
            print("Answer:", trueAns)
            print("Crap, you got it wrong. Next!")
            
    if qnNum == 4:
        #binary(1s) to decimal
        qn = oneSConv(decBiConv (randNum()*-1))
        qnStr = ''.join([str(x) for x in qn])
        trueAns = biDecConv (oneSConv(qn))
        print("Find the decimal of this 1s binary:", qnStr, end="")
        answer = input(">> ")
        if (int(answer)*-1) == trueAns:
            print("Answer:", (trueAns*-1))
            print("Eyy you got it right!")
            score += 1
        else:
            print("Answer:", (trueAns*-1))
            print("Crap, you got it wrong. Next!")
    
    if qnNum == 5:
        #binary(2s) to decimal
        qn = twoSConv(oneSConv(decBiConv(randNumNeg())))
        qnStr = ''.join([str(x) for x in qn])
        trueAns = biDecConv (oneSConv(revTwoSConv((qn))))
        print("Find the decimal of this 2s binary:", qnStr, end="")
        answer = input(">> ")
        if (int(answer)*-1) == trueAns:
            print("Answer:", (trueAns*-1))
            print("Eyy you got it right!")
            score += 1
        else:
            print("Answer:", (trueAns*-1))
            print("Crap, you got it wrong. Next!")
    
    if qnNum == 6:
        #binary addition (normal and 1s)
        ans1 = randNum()
        qn1 = decBiConv(ans1)
        qn1str = ''.join([str(x) for x in qn1])
        ans2 = randNum()*-1
        qn2 = oneSConv(decBiConv(ans2))
        qn2str = ''.join([str(x) for x in qn2])
        print("Give the decimal value of",qn1str,"+ (1s)",qn2str, end="")
        answer = input(">> ")
        if int(answer) == ans1 + ans2:
            print("Answer:", ans1 + ans2)
            print("Eyy you got it right!")
            score += 1
        else:
            print("Answer:", ans1 + ans2)
            print("Crap, you got it wrong. Next!")
            
    if qnNum == 7:
        #binary addition (normal & 2s)
        ans1 = randNum()
        qn1 = decBiConv(ans1)
        qn1str = ''.join([str(x) for x in qn1])
        ans2 = randNumNeg()
        qn2 = twoSConv(oneSConv(decBiConv(ans2)))
        qn2str = ''.join([str(x) for x in qn2])
        print("Give the binary value of",qn1str,"+ (2s)",qn2str, end="")
        answer = input(">> ")
        if ans1 + ans2 >= 0:
            trueAns = decBiConv(ans1 + ans2)
            trueAnsStr = ''.join([str(x) for x in trueAns])
        else:
            trueAns = twoSConv(oneSConv(decBiConv(ans1 + ans2)))
            trueAnsStr = ''.join([str(x) for x in trueAns])
        trueCount = 0
        for x,y in zip(answer,trueAns):
            if int(x) == y:
                trueCount += 1
        if trueCount== 8:
            print("Answer:", trueAnsStr)
            print("Eyy you got it right!")
            score += 1
        else:
            print("Answer:", trueAnsStr)
            print("Crap, you got it wrong. Next!")
             
    roundNo -= 1

if roundNo != -1:
    print("\nYour score:",score,'/',denom)
    if score/denom > (50/100):
        print("You passed! Not bad~")
    else:
        print("You may want to play again :D")


