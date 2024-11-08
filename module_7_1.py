class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category


    def __str__(self):
        text = f'{self.name}, {self.weight}, {self.category}'
        return text


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'


    def get_products(self):
        file = open(self.__file_name, 'r')
        result = file.read()
        file.close()

        return result

    def add(self, *product):
        file = open(self.__file_name, 'a')
        for i_prod in product:
            temp_str = f'{str(i_prod)}\n'
            prod_name = temp_str.split(',')[0]
            if prod_name not in self.get_products():
                file.write(temp_str)
            else:
                print(f'Продукт {prod_name} уже есть в магазине')


        file.close()



        #print(product)



if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())