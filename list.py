#problem1
n = []
a = 'str'
b = 1
c = 2.0
d = True
e =[1]
n.append(a)
n.append(b)
n.append(c)
n.append(d)
n.append(e)
print(n)

#problem2
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
n = names.count('Jack')
print(n)

#problem3

d = names[1:11:2] + names[11:]
print(d)

#problem4
lst = []
a = 'Beksultan'
b = '2004'
c = 'Python'
lst.append(a)
lst.append(b)
lst.append(c)
print(lst)

#problem5
a = ['Beksultan', 'Shermat', 'Bayel', 'Daniel', 'Ahmet']
n = ','
print(n.join(a))
