
def main():
    access()
    admin()
    user()

def access():
    access = int(input('Choose access: \n 1. Admin \n 2. User \n 3. Exit '))
    while access !=1 and access != 2 and access !=3:
        print('Please select from 1 - 3')
        access = int(input('Choose access: \n 1. Admin \n 2. User \n 3. Exit '))
    if access == 1:
        print('Welcome Admin!')
        admin()
    elif access == 2:
        print('User Welcome!')
        user()
    elif access == 3:
        print('Good bye!!!')

def admin():
    password = 'Admin'
    passcode = input('Enter password: ')
    if passcode == password:
        display_items()
        add_new_items()
        update_quantities()
        set_items_price()
        view_sales_record()
    else:
        print("Sorry, you're not the admin")
        access()

def display_items():
    print('-' * 50)
    print("Welcome to Adamu's Shop")
    print('This is what we have in stock:')
    print('-' * 50)
    item = open('data.csv', 'r')
    items = item.readlines()
    for item in items:
        print(item)


def add_new_items():
    new_items = []
    to_input = str(input('Add new Item, quantity, price per unit. \n '
                         'separate item, quantity and price with space '))
    new_items.append(to_input)
    while to_input != '':
        to_input = str(input('Add new Item, quantity, price per unit. \n '
                             'separate item, quantity and price with space '))
        new_items.append(to_input)
    new_items.pop(-1)
    print(new_items)
        
def user():
    #password = 'User'
    #passcode = input('Enter password: ')
    print('Welcome, Our dear customer!')
    display_items()
    bill()
    # buy_items()
    access()


def bill():
    import pandas as pa
    global receipt

    f = input("Please Enter Today's date: ")
    k = input('Enter Transaction ID: ')
    z = int(input('Please enter Number of Purchase items: '))
    count = 1
    total = 0
    Cart = []
    Bag = {}
    Cash = []
    while count <= z:
        name = input("Enter Product Description: ")
        qty = int(input("Please Enter Purchased Quantity: "))
        UnitPrice = int(input("Enter Unit Price: "))
        cost = UnitPrice*qty
        Cart = (f, 'PURCHASE', name, qty, UnitPrice, cost)
        c.execute('INSERT INTO SALES VALUES (?,?,?,?,?,?)', Cart)
        conn.commit()
        Bag[name] = list((qty, UnitPrice, cost))
        total += cost
        count +=1
    print("Total amount = ", total, "Naira")
    if z <= 5:
        VAT = 0.2*total
        NewTotal = total + VAT
        Cash = (f, k, total, VAT, NewTotal)
        c.execute('INSERT INTO CASH_rECORD VALUES (?,?,?,?,?,?)', Cash)
        conn.commit()
        print('VAT = ', VAT, 'Naira')
        print('Total Payment Due = ', NewTotal, 'Naira')
    elif z > 10:
        VAT = 0.3*total
        NewTotal = total + VAT
        Cash = (f, k, total, VAT, NewTotal)
        c.execute('INSERT INTO CASH_rECORD VALUES (?,?,?,?,?,?)', Cash)
        conn.commit()
        print('VAT = ', VAT, 'Naira')
        print('Total Payment Due = ', NewTotal, 'Naira')
    else:
        pass

    receipt = pa.DataFrame(Bag, index =['Quantity', 'Unit Price', 'Cost'])
    

if __name__ == '__main__':
    main()
