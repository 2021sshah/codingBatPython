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
    return nums[:4].count(9) > 0


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
    return str.replace(".x", "a").find("xyz") >= 0
    # return len([i for i in range(len(str)-2) if str[i:i+3] == "xyz" and (str[i-1] != '.' or i == 0)]) > 0


# List 2


def count_evens(nums):
    return len([i for i in nums if i % 2 == 0])


def big_diff(nums):
    return max(nums)-min(nums)


def centered_average(nums):
    return (sum(nums)-max(nums)-min(nums))//(len(nums)-2)


def sum13(nums):
    return sum([nums[i] for i in range(len(nums)) if nums[i] != 13 and (nums[i-1] != 13 or i == 0)])


def sum67(nums):
    return sum(n for i,n in enumerate(nums) for bn in [nums[:i][::-1] + [7,6]] if n!=6 and bn.index(7) < bn.index(6))
    # while 6 in nums: del nums[nums.index(6)+0:nums.index(7,nums.index(6))+1]
    # return sum(nums)


def has22(nums):
    return len([i for i in range(1, len(nums)) if nums[i] == nums[i-1] == 2]) > 0


# Logic 2


def make_bricks(small, big, goal):
    return (goal // 5 <= big or goal - 5*big <= small) and goal % 5 <= small


def lone_sum(a, b, c):
    return sum([i for i in [a,b,c] if list([a,b,c]).count(i) == 1])


def lucky_sum(a, b, c):
    return sum([a, b, c, 13][:[a, b, c, 13].index(13)])


def no_teen_sum(a, b, c):
    return sum([i for i in [a, b, c] if not (12 < i < 15 or 16 < i < 20)])


def round_sum(a, b, c):
    return sum([(i+5)//10*10 for i in [a,b,c]])


def close_far(a, b, c):
    return (abs(a-b) < 2 and abs(a-c) > 1 and abs(b-c) > 1) or (abs(a-c) < 2 and abs(a-b) > 1 and abs(b-c) > 1) 


def make_chocolate(small, big, goal):
    return [-1, max(goal - 5*big, goal%5)][(goal // 5 <= big or goal - 5*big <= small) and goal % 5 <= small]
