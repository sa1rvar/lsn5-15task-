
# lst = [1,2,3,4,5,6,7,8,9,10]
# # lst1 = [x ** 2  for x in lst if x % 2 != 1]
# # print(lst1)
# # lst.remove(9) -> element boyicha
# # lst2 = []
# # lst1 = [lst2.append(x) for x in lst if x not in lst2]
# # print(lst2)
# lst1 = [sum(lst)]
# print(lst1)


#task1
# def series_resistance(lst):
#     a = sum(lst)
#     if a > 1:
#         return f"{a} ohms"
#     else:
#         return f"{a} ohm"
#
#
# print(series_resistance([1, 5, 6, 3])) #➞ "15 ohms"
# print(series_resistance([16, 3.5, 6])) #➞ "25.5 ohms"
# print(series_resistance([0.5, 0.5])) #➞ "1.0 ohm"

#task2
# def asc_des_none(nums,str):
#     if str == "Asc":
#         return sorted(nums,reverse=True)
#     elif str == "Des":
#         return sorted(nums,reverse=True)
#     else:
#         return nums
# print(asc_des_none([4, 3, 2, 1], "Asc" )) #➞ [1, 2, 3, 4]
# print(asc_des_none([7, 8, 11, 66], "Des"))# ➞ [66, 11, 8, 7]
# print(asc_des_none([1, 2, 3, 4], "None")) #➞ [1, 2, 3, 4]
#task3
# def number_split(num):
#     a = num // 2
#     b = num - a
#     return a,b
# print(number_split(4))#➞ [2, 2]
# print(number_split(10))# ➞ [5, 5]
# print(number_split(11))# ➞ [5, 6]
# print(number_split(-9))# ➞ [-5, -4]

#task4
# def jazzify(num):
# 	lst = []
# 	for x in num:
# 		if x[-1] == "7":
# 			lst.append(x)
# 		else:
# 			lst.append(x + "7")
# 	return lst
#
# print(jazzify(["G", "F", "C"])) #➞ ["G7", "F7", "C7"]
# print(jazzify(["Dm", "G", "E", "A"])) #➞ ["Dm7", "G7", "E7", "A7"]
# print(jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"])) #➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
# print(jazzify([])) #➞ []

#task5
# def find_odd(num):
#     for x in num:
#         if num.count(x) % 2 != 0:
#             return x
# print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])) #➞ -1
# print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))# ➞ 5
# print(find_odd([10])) #➞ 10

#task6
# def filter_list(items):
#     ints = []
#     for x in items:
#         if type(x) == int:
#             return ints.append(x)
# print(filter_list([1, 2, "a", "b"])) #➞ [1, 2]
# print(filter_list([1, "a", "b", 0, 15])) #➞ [1, 0, 15]
# print(filter_list([1, 2, "aasf", "1", "123", 123])) #➞ [1, 2, 123]

#task7
# lst = [1, 2, 3, 4, 5, 6]
# first = lst[0]
# middle = lst[1:-1]
# last = lst[-1]
# print(first) #➞ outputs 1
# print(middle) #➞ outputs [2, 3, 4, 5]
# print(last) #➞ outputs 6

#task8
# def count_characters(elements):
#     return len("".join(elements))
# print(count_characters([
#   "###",
#   "###",
#   "###"
# ]))# ➞ 9
# print(count_characters([
#   "22222222",
#   "22222222"
# ]))# ➞ 16
# print(count_characters([
#   "------------------"
# ]))# ➞ 18
# print(count_characters([])) #➞ 0
# print(count_characters(["", ""])) #➞ 0

#task9
# def move_to_end(lst, num):
#     a = lst.pop(0)
#     lst.append(a)
#     return lst
# print(move_to_end([1, 3, 2, 4, 4, 1], 1)) #➞ [3, 2, 4, 4, 1, 1]
# # Move all the 1s to the end of the array.
# print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9)) #➞ [7, 8, 1, 2, 3, 4, 9]
# print(move_to_end(["a", "a", "a", "b"], "a"))# ➞ ["b", "a", "a", "a"]

#task10
# def find_even_nums(n):
#
# print(find_even_nums(8)) #➞ [2, 4, 6, 8]
# print(find_even_nums(4)) #➞ [2, 4]
# print(find_even_nums(2)) #➞ [2]
#task11
# def filter_list(lst):
#     lst1 = []
#     for x in lst:
#         if type(x) == int:
#             lst1.append(x)
#     return lst1
#
# print(filter_list([1, 2, 3, "a", "b", 4])) #➞ [1, 2, 3, 4]
# print(filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]))# ➞ [0, 1729]
# print(filter_list(["Nothing", "here"])) #➞ []

#task12
# def add_indexes(nums):
#     lst1 = []
#     for x in nums:
#         a = nums.index(x)
#         b = a + x
#         lst1.append(b)
#     return lst1
# print(add_indexes([0, 0, 0, 0, 0])) #➞ [0, 1, 2, 3, 4]
# print(add_indexes([1, 2, 3, 4, 5])) #➞ [1, 3, 5, 7, 9]
# print(add_indexes([5, 4, 3, 2, 1]))# ➞ [5, 5, 5, 5, 5]

#task13
# def probability(lst, num):
#     for x in lst:
#         if x >= num:
#             x / 1/10
#         return x
#
# print(probability([5, 1, 8, 9], 6)) #➞ 50.0
# print(probability([7, 4, 17, 14, 12, 3], 16))# ➞ 16.7
# print(probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6))# ➞ 70.0

#task14
# def next_in_line(lst1, nums):
#     lst1.pop(0)
#     lst1.append(nums)
#     if lst1 is None:
#         return "No list has been selected"
#     return lst1
#
# print(next_in_line([5, 6, 7, 8, 9], 1)) # ➞ [6, 7, 8, 9, 1]
# print(next_in_line([7, 6, 3, 23, 17], 10)) # ➞ [6, 3, 23, 17, 10]
# print(next_in_line([1, 10, 20, 42], 6)) #➞ [10, 20, 42, 6]
# print(next_in_line([], 6)) #➞ "No list has been selected"

#task15

# def get_budgets(dict):
#     lst = []
#     for x in dict:
#         budget = x.get("budget")
#         lst.append(budget)
#     return sum(lst)
# print(get_budgets([
#         {"name": "John", "age": 21, "budget": 23000},
#         {"name": "Steve", "age": 32, "budget": 40000},
#         {"name": "Martin", "age": 16, "budget": 2700}
#     ])) #➞ 65700
# print(get_budgets([
#         {"name": "John", "age": 21, "budget": 29000},
#         {"name": "Steve", "age": 32, "budget": 32000},
#         {"name": "Martin", "age": 16, "budget": 1600}
#     ])) #-> 62600
