items = ["Apple", "Banana", "orange", "apple", "mango"]

uniqe_item = set()


for item in items:
    if item in uniqe_item:
        print("Dublicte: ", item)
        break
    uniqe_item.add(item)