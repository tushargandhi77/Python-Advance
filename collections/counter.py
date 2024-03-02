from collections import Counter

lst = [1,2,3,54,2,4,3,5,6,3,4,5,3,5,3,4,6,4]

clist = Counter(lst)

for ele,count in clist.items():
    print(ele,count)
    

