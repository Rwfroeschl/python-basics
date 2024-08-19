import heapq

unsorted_array = [100, 230, 74, 1, 44, 84, 12013]

heapq.heapify(unsorted_array)
# [1, 74, 44, 230, 100, 12013, 84]
# ---------------------------------
#                 1
#       74                44
#   230    100      12013    84
#

# sorting
sorted_array = []
for _ in range(len(unsorted_array)):
    sorted_array.append(heapq.heappop(unsorted_array))
print (sorted_array)
# [1, 44, 74, 84, 100, 230, 12013]