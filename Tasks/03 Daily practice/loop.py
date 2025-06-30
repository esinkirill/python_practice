x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('x==3')
    else:
        print('continuing...')
        continue
# Notice the tuple unpacking!

for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))
print(list(enumerate('abcde')))
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

zip(mylist1,mylist2)

print(list(zip(mylist1,mylist2)))

for item1, item2 in zip(mylist1,mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))