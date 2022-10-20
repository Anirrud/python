def isIsomorphic(str1, str2):          
    dict_str1 = {}
    dict_str2 = {}
    
    for i, value in enumerate(str1):
        dict_str1[value] = dict_str1.get(value, []) + [i]
    print(dict_str1)      
    for j, value in enumerate(str2):
        dict_str2[value] = dict_str2.get(value, []) + [j]
    print(dict_str2)
    if sorted(dict_str1.values()) == sorted(dict_str2.values()):
        return True
    else:
        return False
s1=input("enter the first string=")
s2=input("enter the second string=")
print(isIsomorphic(s1,s2))        
