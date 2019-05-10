# def bigsize(arr):
#     newarr = []
#     for item in arr:
#         if item > 0:
#             newarr.append("big")
#         else:
#             newarr.append(item)
#     print(newarr)

# bigsize([-1, 3, 5, -5])

# def countpos(arr):
#     newarr = []
#     count = 0
#     maxlen = len(arr)-1
#     for item in range(len(arr)):
#         if item == maxlen:
#             newarr.append(count)
#         elif arr[item] > 0:
#                 newarr.append(arr[item])
#                 count = count + 1
#         else:
#             newarr.append(arr[item])
#     print(newarr)

# countpos([5,-2,-7,-2])

# def sumtotal(arr):
#     count = 0
#     for item in range(len(arr)):
#         count = arr[item] + count
#     print(count)

# sumtotal([1,2,3,4])

# def avg(arr):
#     avgnum = 0;
#     count = 0
#     for item in range(len(arr)):
#         count = arr[item] + count
#     avgnum = count / len(arr)
#     print(avgnum)

# avg([1,2,3,4])

# def length(arr):
#     print(len(arr))

# length([37,2,1,-9])

# def min(arr):
#     min = 0
#     if len(arr) == 0:
#         return False
#     else:
#         for item in range(len(arr)):
#             if arr[item] < min:
#                 min = arr[item]

#     print(min)

# min([1,2,-3,4])

# def max(arr):
#     max = 0
#     if len(arr) == 0:
#         return False
#     else:
#         for item in range(len(arr)):
#             if arr[item] > max:
#                 max = arr[item]

#     print(max)

# max([1,6,-3,4])

# def ult_anal(arr):
#     dict = {
#         'Total': 0,
#         'avg': 0,
#         'min': 0,
#         'max': 0,
#         }
#     for item in range(len(arr)):
#         dict['Total'] = arr[item] + dict['Total']
#         if arr[item] < dict['min']:
#             dict['min'] = arr[item]
#         if arr[item] > dict['max']:
#             dict['max'] = arr[item]
#     dict['avg'] = dict['Total'] / len(arr)
#     print(dict)

# ult_anal([37,2,1,-9])

def reverselist(arr):
        arr.reverse()
        print(arr)        

reverselist([1,2,3,4,5,10,19,7,3,8])