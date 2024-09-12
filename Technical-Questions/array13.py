
def URLify(word,length):
    newWord = ''
    for i in range(len(word)):
        print(word[i])
        if length <= i:
            print (len(newWord))
            return newWord
        if word[i] == ' ':
            newWord += '%20'
        else:
            newWord += word[i]
# Time: O(l) where L is the length given
# Space: O(1)


example = "Mr John Smith  "
length = 13
print(URLify(example, length))