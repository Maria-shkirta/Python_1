from isOdd import isOdd

#задан список a=[5,9,4,2,7]. Создать список из нечетных чисел данного массива.

a=[5,9,4,2,7]
j=0

b=list(filter(lambda x:isOdd(x),a))
print(b)
