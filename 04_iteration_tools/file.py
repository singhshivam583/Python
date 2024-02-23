
# f = open('./chai.py')
# # Read the first line of the file
# print(f.readline())

# f.__next__()   # Move to the next line (equivalent to calling readline again)

# for line in open('chai.py'):
#     print(line, end='')

# while True:
#     line = f.readline()
#     if not line:  # If we've reached EOF, break out of the loop
#         break      # Otherwise, keep reading lines
#     else:         # Process each non-empty line here... 
#         print(line)

# mylist = [1, 2, 3, 4]

# I = iter(mylist)  # Create an iterator object from mylist
# print(type(I))    # <class 'iterator'>
# print(id(I)) 
# print(I)
# print(next(I))  # Output: 1
# print(I.__next__())  # Output: 2
# print(id(I))

# f = open('./chai.py')   # open() automaticaly iter the file in f
# print(iter(f) is f)  # True
# print(iter(f) is f.__iter__())

# D = {'a': 10, 'b': 20}

# for key in D.keys():
#     print(key)

# I = iter(D)
# print(next(I))
# print(next(I))

R = range(5)
# print(R)
I = iter(R)
print(next(I))
print(next(I))
print(next(I))