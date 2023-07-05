# 閏平年
# 依照Wikipedia的定義：
# 公元年分除以4不可整除，為平年
# 公元年分除以4可整除但除以100不可整除，為閏年
# 公元年分除以100可整除但除以400不可整除，為平年
# 公元年分除以400可整除但除以3200不可整除，為閏年

def is_leap(year):
	if year%4==0 and year%100!=0:
		return True
	elif year%400==0 and year%3200!=0:
		return True
	else:
		return False

print(is_leap(2000))
print(is_leap(2002))
print(is_leap(2006))
print(is_leap(2008))

# def is_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     elif year % 3200 != 0:
#         return True
#     else:
#         return False

# 也可用整除4且不整除100或整除4且整除100且整除400才是閏年
def is_leap(year):
	if year%4==0 and year%100!=0:
		return True
	elif year%4==0 and year%100==0 and year%400==0:
		return True
	else:
		return False

print(is_leap(2000))
print(is_leap(2002))
print(is_leap(2006))
print(is_leap(2008))


# 用sum做數字加總
def sum_of_list(num):
	return sum(num)

print(sum_of_list([1, 2, 3]))
print(sum_of_list([2, 3, 100]))

# 用for loop做數字加總
def sum_of_list(numbers):
    sum_number = 0
    for num in numbers:
        sum_number += num
    return sum_number

print(sum_of_list([1, 2, 3]))
print(sum_of_list([2, 3, 100]))