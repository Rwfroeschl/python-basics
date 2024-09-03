from collections import deque
# first solution. Oof. 
def threeinOne(arr):
    stack1, stack2, stack3 = deque(), deque(), deque()
    interval = len(arr) // 3
    remainder = len(arr) % 3
    for i in range(0, interval):
        stack1.appendleft(arr[i])
    for j in range(interval, interval*2):
        stack2.appendleft(arr[j])
    for k in range(interval*2, interval*3):
        stack3.appendleft(arr[k])
    if remainder > 0:
        if remainder == 1:
            stack1.appendleft(arr[len(arr)-1])
        else:
            stack1.appendleft(arr[interval*3])
            stack2.appendleft(arr[len(arr)-1])
    print(stack1) 
    print(stack2)
    print(stack3)

def threeStack(arr):
    stack1, stack2, stack3 = deque(), deque(), deque()
    interval = len(arr) // 3
    remainder = len(arr) % 3
    for i in range(len(arr)):
        if i == interval:
            print("first index: ",i)
            firstIndex = i
            addStack(stack1, 0, i, arr)
        elif i == interval*2:
            print("second index: ",i)
            secondIndex = i
            addStack(stack2, firstIndex, i, arr)
        elif i == interval*3:
            print("third index: ",i)
            addStack(stack3, secondIndex, i, arr)
    if remainder > 0:
        if remainder == 1:
            stack1.appendleft(arr[len(arr)-1])
        else:
            stack1.appendleft(arr[len(arr)-2])
            stack2.appendleft(arr[len(arr)-1])

    print(stack1) 
    print(stack2)
    print(stack3)

def addStack(stack, start, end, arr):
    for i in range(start, end):
        stack.appendleft(arr[i])


# time: O(N) 
# space: O(N) deques take up space

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arr2 =[1, 2, 3, 4, 5, 6, 7, 8, 9]

threeinOne(arr)
print('\n')
threeinOne(arr1)
print('\n')
threeinOne(arr2)
print('\n')
print("second solution: ")
print('\n')
threeStack(arr)
print('\n')
threeStack(arr1)
print('\n')
threeStack(arr2)