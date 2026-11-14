smallest_num = int(input())
middle_num = int(input())
large_num = int(input())

min_val = smallest_num

if middle_num < min_val:
    min_val = middle_num

if large_num < min_val:
    min_val = large_num

print(min_val)