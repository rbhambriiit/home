def ThirdGreatest(arr):
  newarr=[]
  for iter in arr:
    newarr.append((len(iter),iter))
  newarr.sort(reverse=True) 
  print(newarr)
  (size,op)=newarr[2]
  return op
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
ip=["one","two","three","four"]
op=ThirdGreatest(ip)
print(op)
print(type(op))


## few remarks:
# list of tuples: sorted. somewhat similar to dictionary.
# type: class. In python, we always talk in term of objects.
## problem credits: coderbyte.com
