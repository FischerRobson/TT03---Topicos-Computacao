def less_than_or_equal_to_zero(num):
    return num <= 0

def is_even_or_odd(num):
    if (num % 2 == 0) :
      return "odd"
    else :
      return "even"

def find_smallest_numbers(lst):
    lst.sort()
    return lst[:2]

def get_last_item(lst):
    return lst.pop()

def find_largest_num(nums):
    return max(nums)

def compute_abs_sum(nums):
    sum = 0
    for i in nums:
      sum += i
    return sum

def find_largest_nums(num_list):
    maxList = list()
    for lst in num_list:
      maxList.append(max(lst))
    return maxList

def get_word_count(txt) :
    return len(txt.split())
