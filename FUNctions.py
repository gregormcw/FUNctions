def reverse(word):
    rev_word = ""
    for i in range(len(word) -1, -1, -1):
        rev_word += word[i]
        print(str(i) + word[i])
    return rev_word

def bubble_sort(nums):
    for i in range(len(nums) - 1):
        if nums[i+1] < nums[i]:
            nums[i+1], nums[i] = nums[i], nums[i+1]
            bubble_sort(nums)
    return nums

def factorial(num):
    result = 1
    for i in range(num, 1, -1):
        result = result * i
    return result

def sum_of_digits(num):
    result = 0
    if num < 10:
        return result + num
    while num > 9:
        digit = num % 10
        result = result + digit + sum_of_digits(num // 10)
    return result

def cipher(map_from, map_to, code):
    key_code = {}
    decoded = ""
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]
    for letter in code:
        decoded += key_code[letter]
    return key_Code, decoded
