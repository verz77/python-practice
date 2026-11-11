#задача 1
#  def square(x):
#     return x * x 
# result = square(7)
# print(result)
# print(square(3) + 1)
# вывод: 
# 49 10 


# задача 2 
# def is_even(n):
#     return n % 2 == 0 

# print(is_even(4))
# print(is_even(7))
# вывод:
# True
# False

def find_max(numbers):
    biggest = numbers[0]
    for number in numbers:
        if number > biggest:
            biggest = number
    return(biggest)

print(find_max([3, 9, 2]))
print(find_max([-5, -1, -8]))