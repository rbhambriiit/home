arr=[-3,4,12,22,45]
sum1=34
sum2=15

def possible(list,num):
    l=0;
    r=len(list)-1
    while(l<r):
        print("indexes:" , l,r)
        our_sum=list[l]+list[r];
        print("our sum:" ,our_sum)
        if(our_sum<num):
            l=l+1;
        elif(our_sum>num):
            r=r-1;
        else:
            print("optimal soultion found for:", list[l],list[r])
            return True 
    return False
    

op1=possible(arr,sum1)
print(op1)
op2=possible(arr,sum2)
print(op2)
