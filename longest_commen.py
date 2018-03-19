str1 = ['str123','str134','strsl']
print(min(str1))
print(*str1)
print(str1)
print(str1[0][:1])
print(enumerate(zip(*str1)))
str2 = "ansmsdkjfjhgh"
for i in range(len(str2)):
    print(i)
print(str2[2])
"""
if not str1:
    print('')
for i,letter_group in enumerate(zip(*str1)):
    if len(set(letter_group))>1:
        print(str[0][:i])
    else:
        print(min(str1))
"""