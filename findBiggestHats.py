def size(inpu):
	i = 0
 
	for a in inpu:
		i=i+1
  
	return i


def printNum(inpu):
    for num in inpu:
        print(num)

def printHatInfo(names, sizes, prices):
    for index in range(0,size(names)):
        print(names[index],sizes[index],prices[index] )
    
def findMax(inpu):
    biggest = -1    
    for num in inpu:
        if (num>biggest):
            biggest = num
    return biggest

def findMaxAndPos(inpu):
    biggest = -1 
    pos = 0
    maxpos = 0
    for num in inpu:
        if (num>biggest):
            biggest = num
            maxpos=pos
        pos=pos+1
    return biggest,maxpos

aaa = [1,2,3,4,5]

print ('size is: ',size(aaa))
printNum(aaa)


N=['A','B','C']
S=[1,8,30]
P=[10,20,30]

printHatInfo(N,S,P)

print('The biggest is :', findMax(aaa))


big,pos=findMaxAndPos(aaa)
print('The biggest is: ',big,'at position ',pos)






def findBiggestHat(names,sizes,prices):
    bigsize,pos = findMaxAndPos(sizes)
    print('The biggest hat is', names[pos],'with size', bigsize,'and price',prices[pos])
    
findBiggestHat(N,S,P)

def findMbiggestHat(names,sizes,prices,M):
    biggestPos=[]
    for i in range(0,M):
        biggest = -1 
        pos = 0
        maxpos = 0
        for num in sizes:
            if (num>biggest and (pos not in biggestPos)):
                biggest = num
                maxpos=pos
            pos=pos+1
        biggestPos.append(maxpos)
    return biggestPos

def printMLargestHats(n,s,p,M):
    pos=findMbiggestHat(n,s,p,M)    
    for i in range(0,M):
        print('The No.',i+1,'largest hat is',n[pos[i]],'with size of',s[pos[i]],'and price of',p[pos[i]])

printMLargestHats(N,S,P,2)

