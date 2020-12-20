from collections import defaultdict

class Multiset:
    def __init__(self, **kwargs):
        self.multiset=[]
        self.d=defaultdict(int)
        
        return super().__init__(**kwargs)

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.multiset.append(val)

    def remove(self, val):
        for i,v in enumerate(reversed(self.multiset)):
            if v==val:
                self.multiset.pop(self.multiset.__len__()-1-i)
                break

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        if self.d[val]==0:
            return False
        return True
    
    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.multiset)
    
def performOperations(ops):
    multiset=Multiset()
    result=[]
    
    for o in ops:
        if o=="size":
            result.append(multiset.__len__())
        else:
            o1,o2=o.split(" ")
            
            if o1=="query":
                result.append(multiset.__contains__(str(o2)))
            elif o1=="add":
                #if str(o2) in 
                multiset.d[o2]+=1
                multiset.add(o2)
            elif o1=="remove":
                if multiset.d[o2]==1:
                    multiset.multiset.remove(o2)
                elif multiset.d[o2]>1:
                    multiset.remove(o2)

                multiset.d[o2]-=1        

    return result

if __name__ == '__main__':
    operations=["query 1","add 1","query 1","remove 1","query 1","add 2","add 2","size","query 2","remove 2","query 2","size"]
    result=performOperations(operations)
    print(result)