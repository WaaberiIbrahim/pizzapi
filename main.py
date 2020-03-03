from pizzapy import *


print('Bienvenue au DPPD')
print('Nous avons besoin de quelques informations avant de vous livrer')
name = input('Entrer votre nom (Premom et nom de famille seulement)')
email = input('Entrer votre email: ')
phone = input('Entrer votre numero de telephone')
addresse = input('Entrer votre adresse dans cette forme:  addresse, ville, province, code postal')
postal = addresse.split(', ')[3]
n = name.split()

customer = Customer(n[0], n[1], email, phone, addresse)

my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)

menu = my_local_dominos.get_menu()

stuff_to_add = []
while True:
    stuff = input('Entrer votre item (Q pour finir)')
    if stuff.upper == 'Q':
        break
    menu.search(Name=stuff)
    code = input("Entrer le code")
    stuff_to_add.append(code.upper())
order = Order.begin_customer_order(customer, my_local_dominos)
for item in stuff_to_add:
    order.add_item(item)
code = input('Entrez le code de votre carte')
exp = input('Entrer la date dexpiration sans slash')
cvv2 = input('Entrer le coed de securite a larriere de votre carte')
card = CreditCard(code, exp, cvv2, postal)

order.place(card)
my_local_dominos.place_order(order, card)
