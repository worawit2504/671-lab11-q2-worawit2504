# YOUR CODE HERE
n = int(input())
lst1 = []
lst2 = []

for i in range(n):
    while i != n:
        x = int(input())
        lst1.append(x)
        break

for i in range(n):
    y = int(input())
    lst2.append(y)

def summation(lst1,lst2):
    updated_list = [lst1[i] + lst2[i] for i in range(len(lst1))]
    return updated_list

def find_min_max(lst):
    return min(lst),max(lst)

updated_list = summation(lst1,lst2)
print(updated_list)

min,max = find_min_max(updated_list)
print((min,max))
