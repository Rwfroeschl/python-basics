# Question: Check Permutation
# my first solution to checkPerm
def checkPerm(s1, s2):
    if len(s1) != len(s2): return False

    count = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1
    
    for char in s2:
        if count[char] < 1:
            return False
        else:
            count[char] = count.get(char, 0) - 1

    return True

str1 = 'abdfc'
str2 = 'cdaab'
# false
val1 = 'abdac'
val2 = 'cdaab'
# true
print(checkPerm(str1, str2))
print(checkPerm(val1, val2))

# Time complexity O(n)
# Space complexity O(n)


# After hints, I came up with this solution which uses no space
def checkPermCount(s1, s2):
    if len(s1) != len(s2): return False
    val1,val2 = 0,0

    for char in s1:
        val1 += ord(char)
    for char in s2:
        val2 += ord(char)
    
    if val1 != val2:
        return False
    return True

str1 = 'abdaf'
str2 = 'cdaab'
# False
val1 = 'abdac'
val2 = 'cdaab'
# True
print(checkPermCount(str1, str2))
print(checkPermCount(val1, val1))

# Time Complexity: O(n)
# Space Complexity: O(1)