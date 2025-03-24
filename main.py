#averid
#lesson16
#march24/25
# working with lists

# import random
# num=[random.randint(0,100)for i in range(100)]
# print(num)
# count=100
# average=int(sum(num)/count)
# print ("the average of your numbers is",average)

import random
numberslist=[]
for i in range(100):
    num=random.randint(0,100)
    numberslist.append(num)
print(numberslist)
count=100
average=(sum(numberslist)/count)
print ("the average of your numbers is",average)