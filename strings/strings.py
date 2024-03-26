# formatted strings
firstname = "Arthur"
lastname = "Dent"
# first way
# print("hello, "+ firstname)

# second way (Using %)
# print("Welcome, %s %s"%(firstname, lastname))

#third way (Using .format)
# print("Welcome, {0} {1}".format(firstname, lastname))

# fourth way (Using f-string)
# print(f"Welcome, {firstname} {lastname}")

# Sum of numbers
num1=10
num2=20
# print("Sum of {0} and {1} is {2}".format(num1,num2,(num1+num2)))
# print("Sum of %s and %s is %s"%(num1,num2,(num1+num2)))
# print(f"Sum of {num1} and {num2} is {num1+num2}")

s1="geeks"
s2="geeksforgeeks"

# .index will throw a ValueError if the substring is not found
# print(s2.index(s1)) # 0
# print(s2.rindex(s1)) # 8
# print(s2.rindex(s1, 1,len(s2))) #can also take starting position and ending position 

# reverse of a string
# print(s1[::-1]) #skeeg

# if string is rotated
'''
s1="ABCD"
s2="ABCD"
temp=''
temp=s1+s1
if len(s1)!=len(s2):
    print("False")
else:
    print(temp.find(s2)!=-1) 
'''

# Palindrome
'''
s1="ABGBA"
s2=s1[::-1]
if s1==s2:
    print("Palindrome")
else:
    print("Not a Palindrome")
'''

# subsequences of a string
# the total number of subsequences of a string of length n is 2^n
s1="GEEKSFORGEEKS"
s2="GRGES"
# def substring(s1,s2):
#     i,j=0,0
#     isSubstring=True
#     while(i<len(s1) or j<len(s2)):
#         if s1[i]==s2[j]:
#             i+=1
#             j+=1
#         else:
#             i+=1
#     if(j<len(s2)):
#         isSubstring=False
#     return isSubstring
# print(substring(s1,s2))

# finding substrings using recursion
# def substring(s1,s2,m,n):
#     if(m==0 and n!=0):
#         return False
#     if(n==0):
#         return True
#     if(s1[m-1]==s2[n-1]):
#         m=m-1
#         n=n-1
#         return substring(s1,s2,m,n)
#     else:
#         m=m-1
#         return substring(s1,s2,m,n)

# print(substring(s1,s2,len(s1),len(s2)))

# finding anagram

# naive solution
# s1=sorted("spring") #sorting the strings
# s2=sorted("sring") #sorting the strings
# print(s1==s2)

# efficient solution
# def areAnagrams(s1,s2):
#     if(len(s1)!=len(s2)):
#         return False
#     new_arr=[0]*256
#     for i in range(len(s1)):
#         new_arr[ord(s1[i])]+=1
#         new_arr[ord(s2[i])]-=1
#     for i in new_arr:
#         if i!=0:
#             return False
#         else:
#             continue
#     return True
# print(areAnagrams("spring","sringp"))


# Left most repeating character
def repeat():
    s1="abbca"
    for i in range(len(s1)):
        temp=s1[i]
        result = s1.find(temp,i+1,len(s1))
        if(result!=-1):
            return temp
        else:
            continue
    return -1
print(repeat())

