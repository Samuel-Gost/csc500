# Step 1
class ItemToPurchase:
    item_name = 'none'
    item_description = 'desc'
    item_price = 0.0
    item_quantity = 0

    def __init__(self, name, description, price, quantity):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, '@ $', self.item_price, '= $', self.item_price * self.item_quantity)


# Step 2
print('Item 1')
item1_name = str(input('Enter the item name: '))
item1_price = int(input('Enter the item price: '))
item1_quantity = int(input('Enter the item quantity: '))
print('Item 2')
item2_name = str(input('Enter the item name: '))
item2_price = int(input('Enter the item price: '))
item2_quantity = int(input('Enter the item quantity: '))


class ShoppingCart:
    # Step 4
    customer_name = 'none'
    current_date = 'January 1, 2020'
    cart_items = []

    def __init__(self, customer_name, current_date):
        self.customer_name = customer_name
        self.current_date = current_date

    # Step 7
    def print_customer_info(self):
        print('Customer name: ', self.customer_name, '\nToday\'s date: ', self.current_date, '\n')

    def add_item(self, ItemToPurchase):
        item_list = [ItemToPurchase.item_name, ItemToPurchase.item_description, ItemToPurchase.item_price,
                     ItemToPurchase.item_quantity]
        self.cart_items.append(item_list)

    def remove_item(self, itemToRemove):
        for i in range(len(self.cart_items)):
            if self.cart_items[i][0] == itemToRemove:
                del self.cart_items[i]
                break

    def modify_item(self, item_name, item_quantity):
        for item in self.cart_items:
            if item_name == item[0]:
                item[3] = item_quantity
            else:
                print('Item not found in cart.')

    def get_num_items_in_cart(self):
        return len(self.cart_items)

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost = total_cost + (item[2] * item[3])
        print('Total: $' + str(total_cost))
        return total_cost

    def print_total(self):
        if not self.cart_items:
            print('SHOPPING CART IS EMPTY')
        else:
            total_cost = 0
            total_items = 0
            print('\n****************************************')
            print(self.customer_name + '\'s Shopping Cart - ' + self.current_date)
            for _ in self.cart_items:
                total_items = total_items + 1
            print('Number of Items ' + str(total_items))
            for item in self.cart_items:
                print(item[0] + ' ' + str(item[3]) + ' @ $' + str(item[2]) + ' = $' + str(item[2] * item[3]))
                total_cost = total_cost + (item[2] * item[3])
            print('Total: $' + str(total_cost))
            print('****************************************')

    def print_descriptions(self):
        if not self.cart_items:
            print('SHOPPING CART IS EMPTY')
        else:
            print('\n++++++++++++++++++++++++++++++++++++++++')
            print(self.customer_name + '\'s Shopping Cart - ' + self.current_date)
            print('Item Descriptions')
            for item in self.cart_items:
                print(item[0] + ': ' + item[1])
            print('++++++++++++++++++++++++++++++++++++++++')


# Step 7
customer_name = str(input('Enter customer\'s name: '))
today_date = str(input('Enter today\'s date: '))
obj_customer = ShoppingCart(customer_name, today_date)
obj_customer.print_customer_info()

print('TOTAL COST')
obj1 = ItemToPurchase(item1_name, 'desc', item1_price, item1_quantity)
obj1.print_item_cost()
obj1_item = ItemToPurchase(item1_name, 'desc', item1_price, item1_quantity)
obj_customer.add_item(obj1_item)

obj2 = ItemToPurchase(item2_name, 'desc', item2_price, item2_quantity)
obj2.print_item_cost()
obj2_item = ItemToPurchase(item2_name, 'desc', item2_price, item2_quantity)
obj_customer.add_item(obj2_item)

print('TOTAL: $', (obj1.item_price * obj1.item_quantity) + (obj2.item_price * obj2.item_quantity))


def print_menu(shoppingCart):
    # Step 6
    print_options = '\n\nMENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output ' \
                    'items\' descriptions\no - Output shopping cart\nq - Quit\nChoose an option: '
    while True:
        answer = str(input(print_options))
        match answer:
            case 'a':
                print('ADD ITEM TO CART')
                item_name = str(input('Enter the item name: '))
                item_description = str(input('Enter the item description: '))
                item_price = int(input('Enter the item price: '))
                item_quantity = int(input('Enter the item quantity: '))
                obj_item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
                shoppingCart.add_item(obj_item)
            case 'r':
                print('REMOVE ITEM FROM CART')
                item_name = str(input('Enter name of item to remove: '))
                shoppingCart.remove_item(item_name)
            case 'c':
                print('CHANGE ITEM QUANTITY')
                item_name = str(input('Enter the item name: '))
                item_quantity = int(input('Enter the new quantity: '))
                shoppingCart.modify_item(item_name, item_quantity)
            case 'i':
                shoppingCart.print_descriptions()
            case 'o':
                shoppingCart.print_total()
            case 'q':
                break
            case _:
                print('Wrong input, please choose from the following!')
                str(input(print_options))
        if answer == 'q':
            break


print_menu(obj_customer)
