'''
Caroline Wang
4/17/2019
Problem 6.3
Create functions that reverses an integer and return true if number is palindrom
'''


num = '123'
s=len(num)
newnum= []
for i in num:
    s=s-1
    newnum.append(num[s])


print(newnum)

#need to zip up new num