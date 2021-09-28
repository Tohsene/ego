# T1 = (False,True, 100)
# del T1
# print(T1)

# a = {"True", "Born", 45, "Water"}
# b = {"a", "d", "r", 90}
# u = a.union(b)
# print(u)
# a.update(b)
# print(a)

# print(a.difference(b))
# print(b.difference(a))
# print(a.symmetric_difference(b))

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set2.difference_update(set1)
print(set2)
# #print(set1.intersection(set2))
# # print(set1.union(set2))
# #print(set1.symmetric_difference(set2))
# set1.intersection_update(set2)
# print(set1)


# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# set1.difference_update(set2)
# print(set1)

# set1 = {10, 20, 30, 40, 50}
# set1.difference_update({10, 20, 30})
# print(set1)


# import timeit
# import decimal import Decimal
# arr  = [-4, 3, -9, 0, 4, 1]
# pos = []
# neg = []
# zero = []

# for i in arr:
#     if i > 0:
#         pos.append(i) #pos+=1
#     elif i < 0:
#         neg.append(i)
#     else:
#         zero.append(i)
    
# pos_ratio = len(pos)/len(arr)
# neg_ratio = len(neg)/len(arr)
# zero_ratio = len(zero)/len(arr)

# print(round(pos_ratio, 6))
# print(round(neg_ratio, 6))
# print(round(zero_ratio, 6))
#print(timeit.timeit())