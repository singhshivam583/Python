def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i


# print(even_generator(10))

# num = even_generator(10)
# print(next(num))
# print(num.__next__())

for num in even_generator(10):
    print(num)