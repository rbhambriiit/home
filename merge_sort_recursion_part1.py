## merge sub:
## given 2 sorted arrays of size n1,n2 resp. create a new sorted array (n1+n2)


def merge(list1,list2,mlist=[]):
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

def merge_using_slice(list1,list2,mlist=[]):
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
    print (c1,c2)
    if(c1<n1):
        slice=list1[c1:n1+1]
        ##print(slice)
        #mlist.append(slice)
        mlist.extend(slice)
    ## similar 1 more case ...
    return mlist



#list1=[2,4,6,8]
#list1=[0,2,4,6,8]
list2=[-2,-4,6,8,10,12]
list1=[1,3,5,7]
mlist=merge(list1,list2)
##mlist2=merge_using_slice(list1,list2)
print(mlist)
