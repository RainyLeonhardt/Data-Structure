hash = {}
hash['a'] = 1
hash['b'] = 2
print(hash)
for key in hash:
    print(key)
for key in hash:
    print(key, hash[key])
print('a' in hash)
print('x' in hash)
del hash['a']
print(hash)