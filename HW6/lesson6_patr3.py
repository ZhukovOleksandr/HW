print("Введите международный размер, который нужно перевести:")
size = str(input().upper())


def size_func(size1):
    return table_size.get(size1)


table_size = {'XXS': 'Russia - 42, Germany - 36, USA - 8, France - 38, UK - 24',
              'XS': 'Russia - 44, Germany - 38, USA - 10, France - 40, UK - 26',
              'S': 'Russia - 46, Germany - 40, USA - 12, France - 42, UK - 28',
              'M': 'Russia - 50, Germany - 42, USA - 14, France - 44, UK - 30',
              'L': 'Russia - 52, Germany - 44, USA - 16, France - 46, UK - 32',
              'XL': 'Russia - 54, Germany - 46, USA - 18, France - 48, UK - 34',
              'XXL': 'Russia - 56, Germany - 48, USA - 20, France - 50, UK - 36',
              'XXXL': 'Russia - 58, Germany - 50, USA - 22, France - 52, UK - 38'}
my_size = size_func(size)
print(my_size)
