# d = {'simple_key':'hello'}
# # Grab 'hello'
# print(d['simple_key'])
#
# d = {'k1':{'k2':'hello'}}
# print(hash('k1'))
# print(d['k1']['k2'])
#
# d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# print(d['k1'][0]['nest_key'][1][0])
#
# d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#
# print(d['k1'][2]['k2'][1]['tough'][2][0])

# TABLE_SIZE = 10
#
# hash_table = [None] * TABLE_SIZE
#
# def put(key, value):
#     h = hash(key)
#     index = h % TABLE_SIZE
#     print(f"PUT: hash({key!r}) = {h}, index = {index}")
#     hash_table[index] = (key, value)
#
# def get(key):
#     h = hash(key)
#     index = h % TABLE_SIZE
#     print(f"GET: hash({key!r}) = {h}, index = {index}")
#     entry = hash_table[index]
#     if entry and entry[0] == key:
#         return entry[1]
#     return None
#
# put("name", "Alice")
# put("age", 30)
#
# print("→", get("name"))  # Alice
# print("→", get("age"))   # 30

#Для того, чтобы хеш-таблица работала, хеш-функция должна быть детерминирована: один и тот же ключ → один и тот же хеш (в рамках жизни таблицы).
# Любая “переменная” или “рандомная” хеш-функция ломает механизм поиска и уничтожает преимущество O(1).

TABLE_SIZE = 10

# Вместо [None]*N делаем список из пустых списков
hash_table = [[] for _ in range(TABLE_SIZE)]

def put(key, value):
    h = hash(key)
    index = h % TABLE_SIZE
    bucket = hash_table[index]
    for i, (k, v) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, value)
            return
    bucket.append((key, value))

def get(key):
    h = hash(key)
    index = h % TABLE_SIZE
    bucket = hash_table[index]
    for k, v in bucket:
        if k == key:
            return v
    return None

# Пример
people = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35),
    ("Diana", 28),
    ("Eve", 22),
    ("Frank", 40)
]

for name, age in people:
    put(name, age)

print("Текущее состояние hash_table:")
for idx, bucket in enumerate(hash_table):
    print(f"{idx}: {bucket}")

print("\nПроверка get():")
for name, _ in people:
    print(f"{name} →", get(name))

