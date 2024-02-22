# tea_varieties = ["Black", "Green", "White", "Oolong"]
# tea_varieties[3] = "Herbal"
# print(tea_varieties)
# # tea_varieties[1:2] = "Grey"
# tea_varieties[1:2] = ["Grey"]
# print(tea_varieties)

# tea_varieties[1:3]=[ "Yellow","Blue"]
# print(tea_varieties)

# insertion
# fruit_list=["apple","banana","orange"]
# fruit_list[1:1] = ["mango", "mango"]
# print(fruit_list)

# # deletion
# fruit_list[1:3] = []
# print(fruit_list)

tea_varieties = ["Masala", "Ginger", "Elaichi"]
# tea_varieties.append("Chamomile")  # add to the end of list
# print(tea_varieties)
# tea_varieties.insert(2, "Green")
# print(tea_varieties)

# del tea_varieties[2]  # remove from beginning of list
# print(tea_varieties)
# tea_varieties.pop(1)
# print(tea_varieties)

# tea_varieties_copy = tea_varieties.copy()
# tea_varieties_copy.append("Green")
# print(tea_varieties)
# print(tea_varieties_copy)

sqaured_num = [x**2 for x in range(10)]  #list comprehension
print(sqaured_num)

even_numbers = [x for x in sqaured_num if x % 2 == 0]   #filtering using list comprehension
print(even_numbers)




