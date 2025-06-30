tuple1 = (3, 3, 3)

print(tuple1.index(3))
print(tuple1.index(3))
print(tuple1.index(3), end = "\n\n")

tuple1 = ('a', 3, 3)

print(tuple1.index('a'))
print(tuple1.index(3))
print(tuple1.index(3))

i = tuple1.index(3)
before = tuple1[:i]        # все элементы слева от 'a'
after  = tuple1[i+1:]      # все элементы справа от 'a'
print(before, after)
print(len(before), len(after))

# tuple.index(x) всегда возвращает индекс первого вхождения x в кортеж.
# Он не “продвигает” поиск дальше после первого вызова — каждый раз ищет с начала.

list5 = [1,2,2,33,4,4,11,22,3,3,2]

list5  = set(list5)
print(list5)

