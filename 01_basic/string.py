# chai = "Masala chai"

# first_char = chai[0]
# print(first_char)

# slice_chai = chai[0:6]
# print(slice_chai)

# num_list = '0123456789'
# even_numbers = num_list[::2]  # start from index 0, step 2 (jump over one number)
# odd_numbers = num_list[1::2]   # start from index 1, step 2 (start at the next odd number)

# multiple_of_3 = num_list[::3]  # numbers that are divisible by 3
# print(multiple_of_3)

# print(num_list[0:7:3])

# print(chai.lower())
# print(chai.upper())
# print(chai.title())
# print(chai.capitalize())

# chai = "  ginger chai  "

# print(chai.strip())
# print(chai.strip().capitalize())


# chai = "Ginger Chai"

# print(chai.replace("Ginger", "Lemon"))
# print(chai.replace("i", "I"))
# print(chai.replace(chai[0], "g"))

# chai = "Lemon, Ginger, Masala, Mint"
# chaiList = chai.split(", ")
# print(chaiList)

# chai = "masala chai"
# print(chai.find("Chai"))     # returns -1 if not found
# print(chai.find("chai"))    # returns position of substring in string   

# chai = "Masala Chai Chai Chai"
# print(chai.count("Chai"))
# print(chai.count("a"))


# chai_type = "Masala"
# quantity = 2
# order = "I ordered {quantity} cups of {chai_type} Chai"
# print(order.format(chai_type=chai_type, quantity=quantity))

# order = "I ordered {} cups of {} Chai".format(quantity, chai_type)
# print(order)

# chai_variety = ["lemon", "Masala", "Ginger"]
# chai_str = "".join([v + ", " for v in chai_variety])
# print(chai_str[:-2])   # removes the last

# chai_str = ", ".join(chai_variety)
# chai_str = "-".join(chai_variety)
# print(chai_str)


# chai = "Masala Chai"
# print(len(chai))
# for letter in chai:
#     print(letter)

# chai = "He said, \"Masala chai is awesome\" "
# chai = '"He said, "Masala chai is awesome"'
# print(chai)

# chai = "Masala\nChai"
# chai = r"Masala\nChai"
# print(chai)

# path = r"c:\user\pwd"
# path = "c:\\user\\pwd"
# print(path)

# chai = "Masala Chai"
# print("Masala" in chai)
# print("a" in chai)