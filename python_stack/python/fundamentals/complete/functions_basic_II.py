# print("#1")
# def countdown(num):
#     for x in range(num, 0, -1):
#         print(x)

# countdown(10)

# print("#2")
# def prntrtn(num1, num2):
#     print(num1)
#     return(num2)
# prntrtn(1,2)

# print("#3")
# def firstlen(arr):
#     a = (arr[0] + (len(arr)))
#     print(a)

# firstlen([1,2,3,4,5])

#4
# def values(arr):
#     newarr = []
#     num = arr[1]
#     for item in arr:
#         if item > num:
#             newarr.append(item)
#     print(newarr)

# values([5,2,3,2,1,4])

#5
def lenval(val1, val2):
    arr = []
    for a in range(0, val1):
        arr.append(val2)
    print(arr)

lenval(6,2)