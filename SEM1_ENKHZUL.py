#Seminar1 DBP221(421) G.Enkhzul
#Bodlogo 1
lists = ['python','php','java']
print(lists[0:3])
#Bodlogo 2
jagsaalt= [1,30,3,11,13,4,6,8,1,3]
c = 0
for i in jagsaalt:
   c = c + i
   i = i + 1 
print(c)

#Bodlogo 3
list2 = [2,2,4,7,6,5]
def urjuuleh(x):
   c = 1
   for i in x:
       c = c * i
       i = i + 1
   print(c)
urjuuleh(list2)

#Bodlogo 4
list3 = [1,2,5,6,6,5]
def multiply():
   numbers = list(map(int, input('').split(',')))
   multiplier = numbers[2]*numbers[-1]
   print(multiplier)    
multiply(list3)

#Bodlogo 5
def funct():
   numbers = list(map(int, input('').split(',')))
   x = max(numbers)
   y = min(numbers)
   print(x,y)

#Bodlogo 6
list = ['222','383','zkz']
def samedigits(list):
 k = 0
 for i in list:
   if  i[0] == i[-1]:
     k += 1
 return k
print(samedigits(list))


#Bodlogo 7
numbers = list(map(int, input('').split(',')))
list2 = set(numbers)
print(list(list2))

#Bodlogo 8
list = []
def func(list):
    if len(list) == 0:
        print('List is empty')  
    else:
        print('List is not empty')
func(list)

#Bodlogo 9
alist = [11,23,4,5,6,7,8,2,3,8]
del alist[3], alist[4], alist[5]
print(alist)

#Bodlogo 10,Bodlogo11
numbers = (1,2,3,5,6,7,8,9,10,11)
y = list(numbers)
y.append(input())
numbers = tuple(y)
print(numbers)

#Bodlogo 12
numbers = (1,2,3,5,6,7,8,9,10,11)
print(numbers[1],numbers[-2])

#Bodlogo 13
y = input()
r = ('12','32','12','jj',y)
if y in cities:
    print('Yes')


#Bodlogo 14
numbers = (11,21,33,15,116,17,58,93,110,111)
k = 0
for i in numbers:
    print(i)
    i += 1

#Bodlogo 15 
beep = {'io','jk','mmm'}
beep2 = {'lol','hah'}
nbeep = beep.union(beep2)
print(nbeep)

#Bodlogo 16
beep = {'io','jk','mmm'}
beep2 = {'lol','mmm'}
nbeep = beep.intersection(beep2)
print(nbeep)

#Bodlogo 17
beep = {'io','jk','mmm'}
length = len(beep)

#Bodlogo 18
x = input()
beep = {'io','jk',x,'mmm'}
print(beep)
beep.remove(x)
print(beep)

#Bodlogo 19
beep = {'hhe','hohoa','mmm'}
beep.clear()


#Bodlogo 20
beep = {'io','jk','mmm'}
del beep

#Bodlogo 21
from audioop import reverse
import operator
num = {hool: huurga,drinks: 100, snack: chiher}
print(sorted(num.items(),key=operator.itemgetter(1)))


#Bodlogo 22
num = {'hool': 'huurga','drinks': 'undaa', 'snack': 'chiher'}
if 'hool' in num:
    print('Yes')
else:
    print('No')

#Bodlogo 23
num = {'hool': 'huurga','drinks': 'undaa', 'snack': 'chiher'}
if 'huurga' in num.values():
    print('Yes')
else:
    print('No')

#Bodlogo 24
num = {'hool': 'huurga','drinks': 'undaa', 'snack': 'chiher'}
for i,k in num.items():
    print(i,k)

#Bodlogo 25
num = {'hool': 'huurga','drinks': 'undaa', 'snack': 'chiher'}
names = {'key1':'Venezuela','key2':'Mongolia'}
num.update(names)
for i,k in num.items():
     print(i,k)

#Bodlogo 26
num = {'hool': huurga,'drinks': undaa, 'snack': chiher} 
print(sum(num.values()))