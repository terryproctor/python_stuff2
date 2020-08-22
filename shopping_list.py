shopping_list=['milk', 'bananas', 'bread', 'bread', 'books']
new_item = input('What would you like to add to your shopping list?')
shopping_list.append(new_item)
shopping_list.insert(0,'impulse buy')
print("Items in your shopping list:\t",shopping_list)
del shopping_list[0]
print(shopping_list)
shopping_list.pop(1)
print(shopping_list)
lost_item=shopping_list.pop(1)
print('You lost:',lost_item)
print(shopping_list)
removed="books"
shopping_list.remove(removed)
print(shopping_list)