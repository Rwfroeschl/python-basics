# brute force
def uniqueChar(s):
    for char in range(len(s)):
        for checkChar in range(char+1,len(s)):
            if s[char] == s[checkChar]:
                return False
    return True

print(uniqueChar("acfgebcid"))
print(uniqueChar("abcdefghijkl"))

# space: O(n^2) time: O(1)

# optimized solution
# suggesting that the character set is not fixed 

def uniqueDictChar(s):
    charSet = {}
    for value in s:
        charSet[value] = charSet.get(value, 0) + 1
        if charSet.get(value) > 1:
            return False
    return True

# space: O(n) / worst case, it loops through the whole char
# time: O(n) / stores each char in the string
print(uniqueDictChar("acfgebcid"))
print(uniqueDictChar("abcdefghijkl"))

# more optimized solution

# ask if the string is in ASCII or unicode. ASCII has 128 unique characters
# assume its ASCII
# assuming we can use more than one data structure

def uniqueASCIIChar(s):
    charSet = [False] * 128

    for char in charSet:
        val = ord[s[char]]
        if charSet[val]:
            return False
        charSet[val] = True
    return True

# Time: O(n) 
# Space: O(1) / using a fixed array with up to 128 elements
print(uniqueASCIIChar("acfgebcid"))
print(uniqueASCIIChar("abcdefghijkl"))


