
def palinPerm(word):
    bagOfLetters = {}
    for letter in word:
        lowercase = letter.lower()
        if not lowercase.isalnum():
            continue
        elif lowercase in bagOfLetters:
            bagOfLetters[lowercase] += 1
        else:
            bagOfLetters[lowercase] = 1
    number = 0
    for letter in bagOfLetters:
        print ("letter and count: ", letter, bagOfLetters[letter])
        if bagOfLetters[letter]%2 != 0:
            number += 1
            if number > 1:
                return False
    return True

    # time: O(l) 
    # space: O(l)

firstTest = "Tact Coa"
secondTest = "22/02/2022"
thirdTest = "A man, a plan, a canal - Panama"
print(palinPerm(firstTest))
print(palinPerm(secondTest))
print(palinPerm(thirdTest))