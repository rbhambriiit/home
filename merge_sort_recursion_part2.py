## notice the division in python 3
## notice how list initialisation in metode definition impacts
def merge(list1,list2):
    mlist=[]
    n1=len(list1)
    n2=len(list2)
    #print(n1,n2)
    c1=0
    c2=0
    while (c1 < n1 and c2 < n2):
        #print (c1,c2)
        if(list1[c1]<=list2[c2]):
            mlist.append(list1[c1])
            c1 += 1
        else:      
            mlist.append(list2[c2])
            c2 += 1
    #print (c1,c2)
    while(c1<n1):
        mlist.append(list1[c1])
        c1 += 1
    while(c2<n2):
        mlist.append(list2[c2])
        c2 += 1
    return mlist


def mergesort(listinput):
    n=len(listinput)
    if(n>1):
        ##print(n//2)
        left=listinput[0:n//2]
        ##print("left:",left)
        right=listinput[n//2:n+1]
        ##print("right:",right)
    ##    print("leftsubarray :",left)
        ltop=mergesort(left)
      ##  print("rightsubarray :",right)
        rtop=mergesort(right)
        print("merging ",ltop,"and",rtop)
        mergedop=merge(ltop,rtop)
  ##      print("returning mergedop:",mergedop)
        return(mergedop)
    else:
        return [listinput[0]]
    
    

listinput=[2,4,1,6,8,5,3,7,12,-6,71]
##listinput=[2,4,1,6]
print("ip:",listinput)
listoutput=mergesort(listinput)
print(listoutput)
