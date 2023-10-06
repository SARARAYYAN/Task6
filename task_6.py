lst = [30, 75, 9, 97, 50, -4, 70, 59]
print("largest no is:", lst[3])
print("largest no is:",max(lst))
lst.remove(min(lst))
print(lst)
lst.sort(reverse=True)
print(lst)
print(lst[3:])
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python",1]]
x=("python")
print(main_lst.count(x))

my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
result = " ".join(word.capitalize() for word in my_lst)
print(result)
my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
copy1 = my_lst[:]
print(copy1)
my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
my_lst[4] = 19
my_lst[2] = "Omar"
print(my_lst)
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
print(sum(nums))
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple1.add ("9")
print(tuple1)
tuple2 = ('Java', 'C++', 7.8)
c = (tuple1 + tuple2)
print(c)
