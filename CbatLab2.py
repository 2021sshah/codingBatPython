# Siddharth Shah Gabor Pd.2
# Warmup 2


def string_times(str, n):
    return str*n


def front_times(str, n):
    return str[:3]*n


def string_bits(str):
    return str[::2]


def string_splosion(str):
    return "".join([str[:i] for i in range(len(str)+1)])


def last2(str):
    return len([i for i in range(len(str)-2) if str[i:i+2] == str[-2:]])


def array_count9(nums):
    return nums.count(9)


def array_front9(nums):
    return nums[0:4].count(9) > 0


def array123(nums):
    return len([i for i in range(len(nums)-2) if nums[i:i+3] == [1, 2, 3]]) > 0


def string_match(a, b):
    return len([i for i in range(len(a)-1) if a[i:i+2] == b[i:i+2]])


# String 2


def double_char(str):
    return "".join([str[i]*2 for i in range(len(str))])


def count_hi(str):
    return str.count("hi")


def cat_dog(str):
    return str.count("cat") == str.count("dog")


def count_code(str):
    return len([i for i in range(len(str)-3) if str[i:i+2] == "co" and str[i+3] == 'e'])


def end_other(a, b):
    return b[-len(a)-1+1:].lower() == a.lower() or a[-len(b)-1+1:].lower() == b.lower()


def xyz_there(str):
    return len([i for i in range(len(str)-2) if str[i:i+3] == "xyz" and (str[i-1] != '.' or i == 0)]) > 0


# List 2


def count_evens(nums):
    return len([i for i in nums if i % 2 == 0])


def big_diff(nums):
    return max(nums)-min(nums)


def centered_average(nums):
    return (sum(nums)-max(nums)-min(nums))//(len(nums)-2)


def sum13(nums):
    return sum([0 if nums[i] == 13 or (nums[i-1] == 13 and i != 0) else nums[i] for i in range(len(nums))])


def sum67(nums):
    return sum([x for index, x in enumerate(nums) if (((nums[(index - nums[index::-1].index(6))+0:].index(7) + (index - nums[index::-1].index(6))) < index) if (6 in nums[:index+1]) else True)])


def has22(nums):
    return len([i for i in range(1, len(nums)) if nums[i] == nums[i-1] == 2]) > 0


# Logic 2


def make_bricks(small, big, goal):
    return (goal // 5 <= big or goal - 5*big <= small) and goal % 5 <= small


def lone_sum(a, b, c):
    return 0 if a == b == c else c if a == b else a if b == c else b if a == c else a+b+c


def lucky_sum(a, b, c):
    return sum([a, b, c, 13][:[a, b, c, 13].index(13)])


def no_teen_sum(a, b, c):
    return sum([i for i in [a, b, c] if not (12 < i < 15 or 16 < i < 20)])


def round_sum(a, b, c):
    return sum(i + 10 - i % 10 if i % 10 >= 5 else i - i % 10 for i in [a, b, c])


def close_far(a, b, c):
    return abs(a-c) >= 2 and abs(b-c) >= 2 if abs(a-b) <= 1 else abs(a-b) >= 2 and abs(c-b) >= 2 if abs(a-c) <= 1 else False


def make_chocolate(small, big, goal):
    return goal % 5 if goal // 5 <= big and goal % 5 <= small else goal - 5*big if goal - 5*big <= small and goal % 5 <= small else -1
