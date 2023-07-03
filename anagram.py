str1='reed'
str2='deer'

list1=[*str1]
list2=[*str2]

dict1={}
dict2={}

for letter in list1:
    if letter not in dict1.keys():
        dict1[letter]=1
    else:
        dict1[letter]+=1

for letter in list2:
    if letter not in dict2.keys():
        dict2[letter]=1
    else:
        dict2[letter]+=1

print(dict1)
print(dict2)

if sorted(list(dict1.keys())) == sorted(list(dict2.keys())):
    for key in sorted(list(dict1.keys())):
        if dict1[key] == dict2[key]:
            pass
        else:
            print('Not an anagram')
            break
    print('Two strings are anagrams')
else:
    print('Not an anagram')
# print(sorted(list(dict1.keys())))
# print(sorted(list(dict2.keys())))

# list1=sorted(list(dict1.keys()))
# list2=sorted(list(dict2.keys()))

# print(list1==list2)
