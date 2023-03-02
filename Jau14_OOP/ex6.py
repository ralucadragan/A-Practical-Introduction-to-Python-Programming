'''
6. Write a class called Converter. The user will pass a length and a unit when declaring an
object from the class—for example, c = Converter(9,'inches'). The possible units are
inches, feet, yards, miles, kilometers, meters, centimeters, and millimeters. For each of these
units there should be a method that returns the length converted into those units. For example,
using the Converter object created above, the user could call c.feet() and should get
0.75 as the result.
'''

class Convert:
    def __init__(self, lenght, unit):
        self.lenght = lenght
        self.unit = unit

    def inches(self):
        if self.unit == in_:
            return self.lenght
        elif self.unit == ft:
            return self.lenght * 12
        elif self.unit == yd:
            return self.lenght * 36
        elif self.unit == mi:
            return self.lenght * 63360
        elif self.unit == km:
            return self.lenght * 39370.1
        elif self.unit == m:
            return self.lenght * 39.3701
        elif self.unit == cm:
            return self.lenght * 0.3937
        elif self.unit == mm:
            return self.lenght * 0.03937

    def feet(self):
        if self.unit == ft:
            return self.lenght
        elif self.unit == in_:
            return self.lenght * 0.0833
        elif self.unit == yd:
            return self.lenght * 3
        elif self.unit == mi:
            return self.lenght * 5280
        elif self.unit == km:
            return self.lenght * 3280.84
        elif self.unit == m:
            return self.lenght * 3.28084
        elif self.unit == cm:
            return self.lenght * 0.0328
        elif self.unit == mm:
            return self.lenght * 0.00328

    def yards(self):
        if self.unit == yd:
            return self.lenght
        elif self.unit == in_:
            return self.lenght * 0.0278
        elif self.unit == ft:
            return self.lenght * 0.333
        elif self.unit == mi:
            return self.lenght * 1760
        elif self.unit == km:
            return self.lenght * 1093.61
        elif self.unit == m:
            return self.lenght * 1.09361
        elif self.unit == cm:
            return self.lenght * 0.0109361
        elif self.unit == mm:
            return self.lenght * 0.00109361

    def miles(self):
        if self.unit == mi:
            return self.lenght
        elif self.unit == in_:
            return self.lenght * 0.000016
        elif self.unit == ft:
            return self.lenght * 0.00019
        elif self.unit == yd:
            return self.lenght * 0.00057
        elif self.unit == km:
            return self.lenght * 0.6214
        elif self.unit == m:
            return self.lenght * 0.0006214
        elif self.unit == cm:
            return self.lenght * 0.000006214
        elif self.unit == mm:
            return self.lenght * 0.00000006214


    def kilometers(self):
        if self.unit == km:
            return self.lenght
        elif self.unit == in_:
            return self.lenght * 0.0000254
        elif self.unit == ft:
            return self.lenght * 0.000305
        elif self.unit == yd:
            return self.lenght * 0.00091
        elif self.unit == mi:
            return self.lenght * 1.60934
        elif self.unit == m:
            return self.lenght * 0.001
        elif self.unit == cm:
            return self.lenght * 0.00001
        elif self.unit == mm:
            return self.lenght * 0.000001

    def meters(self):
        if self.unit == m:
            return self.lenght
        elif self.unit == in_:
            return self.lenght * 0.0254
        elif self.unit == ft:
            return self.lenght * 0.3048
        elif self.unit == yd:
            return self.lenght * 0.9144
        elif self.unit == mi:
            return self.lenght * 1609.34
        elif self.unit == km:
            return self.lenght * 1000
        elif self.unit == cm:
            return self.lenght * 0.01
        elif self.unit == mm:
            return self.lenght * 0.001

    def centimeters(self):
        if self.unit == cm:
            return self.lenght
        elif self.unit == in_:
            return self.lenght * 2.54
        elif self.unit == ft:
            return self.lenght * 30.48
        elif self.unit == yd:
            return self.lenght * 91.44
        elif self.unit == mi:
            return self.lenght * 160934
        elif self.unit == km:
            return self.lenght * 100000
        elif self.unit == m:
            return self.lenght * 100
        elif self.unit == mm:
            return self.lenght * 0.1

    def milimetters(self):
        if self.unit == mm:
            return self.lenght
        elif self.unit == in_:
            return self.lenght * 25.4
        elif self.unit == ft:
            return self.lenght * 304.8
        elif self.unit == yd:
            return self.lenght * 914.4
        elif self.unit == mi:
            return self.lenght * 1609344
        elif self.unit == km:
            return self.lenght * 1000000
        elif self.unit == m:
            return self.lenght * 1000
        elif self.unit == cm:
            return self.lenght * 10

in_ = 'inches'
ft = 'feet'
yd = 'yards'
mi = 'miles'
km = 'kilometers'
m = 'm'
cm = 'centimeters'
mm = 'milimetters'


nr_to_convert = 9
c= Convert(nr_to_convert, in_)
print(f'You want to convert {nr_to_convert} {in_} in to {in_}. Rezult: {c.inches()} {in_}')
print(f'You want to convert {nr_to_convert} {in_} in to {ft}. Rezult: {c.feet()} {ft}')
print(f'You want to convert {nr_to_convert} {in_} in to {yd}. Rezult: {c.yards()} {yd}')
print(f'You want to convert {nr_to_convert} {in_} in to {mi}. Rezult: {c.miles()} {mi}')
print(f'You want to convert {nr_to_convert} {in_} in to {km}. Rezult: {c.kilometers()} {km}')
print(f'You want to convert {nr_to_convert} {in_} in to {m}. Rezult: {c.meters()} {m}')
print(f'You want to convert {nr_to_convert} {in_} in to {cm}. Rezult: {c.centimeters()} {cm}')
print(f'You want to convert {nr_to_convert} {in_} in to {mm}. Rezult: {c.milimetters()} {mm}')

print('--------------')
nr_to_convert = 2748
c= Convert(nr_to_convert, m)
print(c.kilometers())

print('--------------')
nr_to_convert = 647896345
c= Convert(nr_to_convert, mm)
print(c.meters())


print('--------------')
nr_to_convert = 123456789
c= Convert(nr_to_convert, mm)
print(c.miles())
print(c.kilometers())