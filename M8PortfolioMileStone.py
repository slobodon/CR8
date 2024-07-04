class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    #define methods
    def add_items(self):
        print('ADD ITEM TO CART\n'.center(50))
        NumToAdd = int(input('Enter the number of items you want to add\n'))
        TempCartItem = []
        for i in range(NumToAdd):
            TempCartItem.append(input('Enter the item name.\n'.center(50)))
            TempCartItem.append(input('Enter the item description.\n'.center(50)))
            TempCartItem.append(float(input('Enter the item price.\n'.center(50))))
            TempCartItem.append(int(input('Enter the item quantity.\n'.center(50))))
            
            
            self.cart_items.append(TempCartItem )
            TempCartItem = []


    def remove_item(self):
        print('REMOVE ITEM FROM CART'.center(50))
        RemoveItem = input('Enter name of item to remove:\n'.center(50))
        index = next((i for i,item in enumerate(self.cart_items) if item[0]==RemoveItem), -1)
        if index == -1:
            print('Item Not found'.center(50))
        else:
            del self.cart_items[index]
            print('{} has been removed from the cart.'.center(50).format(RemoveItem))
    def modify_item(self):
        print('CHANGE ITEM QUANTITY'.center(50))
        changeItem = input('Enter the item name:\n'.center(50))
        index = next((i for i,item in enumerate(self.cart_items) if item[0]==changeItem), -1)
        if index == -1:
            print('Item Not found'.center(50))
        else:
            try:
                newQuantity = int(input('Enter the new quantity:\n'.center(50)))
            except:
                print('Invalid input of quantity'.center(50))
            else:
                self.cart_items[index][3]=newQuantity

    def get_num_items_in_cart(self):

        totalItems = 0
        for item in self.cart_items:
            totalItems += item[3]
        return totalItems 
        

    def get_cost_of_cart(self):
        #calculate the total cost of the cart
        totalCost = 0
        for item in self.cart_items:
            totalCost += item[3]*item[2] 
        return totalCost

    def print_total(self):
        print('{}\'s Shopping Cart - {}'.format(self.customer_name , self.current_date).center(50))

        numberofitems = self.get_num_items_in_cart()
        print('Number of items: {}'.format(numberofitems).center(50) )
         #print a summary of each item   
        for Item in self.cart_items:
            print('{} {} @ ${}'.format(Item[0], Item[3], Item[2], Item[3]*Item[2]).center(50))

        totalCost = self.get_cost_of_cart()    

        print('Total: ${}'.format(totalCost).center(50))

    def print_descriptions(self):
        print('{}\'s Shopping Cart - {}'.format(self.customer_name , self.current_date).center(50))
        for Item in self.cart_items:
            print('{}: {} '.format(Item[0], Item[1]).center(50))


#Main body of code

    
def print_menu():
    #invalid = 1
    option = 'none'
    while option == 'none'or option != 'q':
        print('MENU'.center(50))
        print('a - Add item to cart'.center(50))
        print('r - Remove item from cart'.center(50))
        print('c - Change item quantity'.center(50))
        print('i - Output items\' descriptions'.center(50))
        print('o - Output shopping cart'.center(50))
        print('q - Quit'.center(50))
        option = input('Choose an option: \n'.center(50))
        if option in ['a', 'r', 'c', 'i', 'o']:
            if option == 'i':
                print('OUTPUT ITEM\'S DESCRIPTIONS'.center(50))
                my_cart.print_descriptions()
            elif option=='o':
                print('OUTPUT SHOPPING CART'.center(50))
                my_cart.print_total()
            elif option=='a':
                my_cart.add_items()
            elif option =='r':
                my_cart.remove_item()
            elif option =='c':
                my_cart.modify_item()
            
        elif option=='q':
            print()
        else:
            print('Invalid Choice. Please Choose a Valid Option.'.center(50))





#option = print_menu()

#print(option)7

CustomerName = input('Enter customer\'s name\n'.center(50))
Date = input('Enter today\'s date\n'.center(50))

print('Customer name: {}'.center(50).format(CustomerName))
print('Today\'s date: {}'.center(50).format(Date))


#testShoppingCart = [['Nike Romaleos', 2, 189, 'Volt color, Weightlifting shoe'],
#                    ['Chocolate Chips', 5, 3, 'Semi-sweet'],
#                    ['Powerbeats 2 Headphones', 1, 128, 'Bluetooth headphones']]

my_cart = ShoppingCart(CustomerName, Date)



print_menu()




#my_cart.print_total()
#print()
#my_cart.print_descriptions()



















































