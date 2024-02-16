def even_genrator(limit):
    # li = []
    for i in range(2, limit + 1, 2):
        # li.append(i)
        # return li
        yield i
        
for num in even_genrator(10):
    print(num)
# print(even_genrator(10))