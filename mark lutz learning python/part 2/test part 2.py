"""Упражнение 1"""
print(2**16)
print(2/5, 2/5.0)
print('spam'+'eggs')
S='ham'
print('eggs'+S)
print(S*5)
print(S[:0])
print('green %s and %s' %('eggs', S))
print('green {0} and {1}'.format('eggs', S))
print(('x',)[0])
print(('x','y')[1])
L=[1,2,3]+[4,5,6]
print(L, L[:], L[-2], L[-2:])
print(([1,2,3]+[4,5,6])[2:4])
print(L[2], L[3])
L.reverse()
print(L)
L.sort()
print(L)
print(L.index(4))
print(({'a':1, 'b':2})['b'])
D={'x':1,'y':2,'z':3}
D['w']=0
print(D['x']+D['w'])
D[(1,2,3)]=4
print(D)
print(list(D.keys()))
print(list(D.values()))
print((1,2,3) in D)
print([[]],['',(),[], {}, None])
"""Упражнение 2"""
L=[1,2,3,4]
print(L[3:1])
L[3:1]=['?']
print(L)
print(L[4])
"""Упражнение 3"""
L=[0,1,2,3]
L[2]=[]
print(L)
L[2:3]=[] #присваивание срезу удаляет значение и добавляет туда новое значение
print(L)
del L[0]
print(L)
del L[1:]
print(L)
# L[1:2]=1 #ошибка
#print(L)
"""Упражнение 4"""
x='spam'
y='eggs'
x,y = y,x
print(x,y) #присваивание кортежу. Python сначала создает временный
# кортеж в правой части из текущих значений y и x затем присваивает x,y как индексы
#кортежа
"""Упражнение 5"""
D={}
D[1]='a'
D[2]='b'
print(D)
D[(1,2,3)]='c'
print(D)



