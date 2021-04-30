# Siddharth Shah Period 2 Gabor
# Warmup 1


def sleep_in(weekday, vacation):
    return not weekday or vacation


def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile


def sum_double(a, b):
    return 4*a if a == b else a + b


def diff21(n):
    return 2*abs(n-21) if n > 21 else abs(n-21)


def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)


def makes10(a, b):
    return a == 10 or b == 10 or a+b == 10


def near_hundred(n):
    return abs(n-100) <= 10 or abs(n-200) <= 10


def pos_neg(a, b, negative):
    return a < 0 and b < 0 if negative else a*b < 0

# String 1


def hello_name(name):
    return "Hello " + name + "!"


def make_abba(a, b):
    return a + 2*b + a


def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"


def make_out_word(out, word):
    return out[:len(out)//2] + word + out[len(out)//2:]


def extra_end(str):
    return str[-2:]*3


def first_two(str):
    return str[0:2]


def first_half(str):
    return str[0:len(str)//2]


def without_end(str):
    return str[1:-1]

# List 1


def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6 or nums[0] == "6" or nums[-1] == "6"


def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[-1]


def make_pi(n):
  return [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9][:n]


def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]


def sum3(nums):
    return sum(nums)


def rotate_left3(nums):
    return nums[1:] + nums[:1]


def reverse3(nums):
    return nums[::-1]


def max_end3(nums):
    return [max(nums[0], nums[-1])]*len(nums)

# Logic 1


def cigar_party(cigars, is_weekend):
    return cigars >= 40 and (cigars <= 60 or is_weekend)


def date_fashion(you, date):
    return 0 if you < 3 or date < 3 else 2 if you > 7 or date > 7 else 1


def squirrel_play(temp, is_summer):
    return temp >= 60 and (temp <= 90 or (is_summer and temp <= 100))


def caught_speeding(speed, is_birthday):
    return 0 if speed <= 60 or (is_birthday and speed <= 65) else 1 if speed <= 80 or (is_birthday and speed <= 85) else 2


def sorta_sum(a, b):
    return 20 if a+b >= 10 and a+b < 20 else a + b


def alarm_clock(day, vacation):
    return "off" if vacation and (day == 0 or day == 6) else "10:00" if vacation or (day == 0 or day == 6) else "7:00"


def love6(a, b):
    return a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6


def in1to10(n, outside_mode):
    return (outside_mode and (n <= 1 or n >= 10)) or (not outside_mode and n >= 1 and n <= 10)
