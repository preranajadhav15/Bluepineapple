import heapq

def largest_number(num):
    heapq.heapify(num)   
    largest = heapq.nlargest(1, num)
    return largest[0]

num = [40,20,50,70,10]
print(largest_number(num))
