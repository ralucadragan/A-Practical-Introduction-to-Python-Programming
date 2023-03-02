'''
2. Write a class called Product. The class should have fields called name, amount, and price,
holding the product’s name, the number of items of that product in stock, and the regular
price of the product. There should be a method get_price that receives the number of
items to be bought and returns a the cost of buying that many items, where the regular price
is charged for orders of less than 10 items, a 10% discount is applied for orders of between
10 and 99 items, and a 20% discount is applied for orders of 100 or more items. There should
also be a method called make_purchase that receives the number of items to be bought and
decreases amount by that much.
'''

class Product:
    def __init__(self, name, amount, price):
        self.name = name # holding the product’s name
        self.amount = amount # the number of items of that product in stock
        self.price = price # and the regular price of the product

    def get_price(self, product):
    # There should be a method get_price that receives the number of
    # items to be bought and returns a the cost of buying that many items, where the regular price
    # is charged for orders of less than 10 items, a 10% discount is applied for orders of between
    # 10 and 99 items, and a 20% discount is applied for orders of 100 or more items.
        if product < self.amount:
            if 0 < product <= 9:
                print(f'We do not offer a discount for this quantity!')
                total1 = product * self.price
                return total1

            elif 10 <= product <= 99:
                print(f'At this quantity {product} we offer a 10% discount!')
                total2 = product * self.price
                total3 = int(total2 * 0.9)
                return total3

            elif product >= 100:
                print(f'At this quantity {product} we offer a 20% discount!')
                total4 = product * self.price
                total5 = int(total4 * 0.8)
                return total5
        else:
            print('We dont have enough products in stock !')


    def make_purchase(self,product):
        return self.amount - product


nume_produs = 'Apple'
cantitate_stok = 200
pret_buc = 5
cantitate_cumparata = 175

p1 = Product(nume_produs, cantitate_stok, pret_buc)
print(f'Pentru cantitatea cumparata de {cantitate_cumparata} buc, pretul final de achizitie este: {p1.get_price(cantitate_cumparata)} lei.')
print(f'Au mai ramas {p1.make_purchase(cantitate_cumparata)} buc in stok !')