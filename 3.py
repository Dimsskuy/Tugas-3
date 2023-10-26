random_list = [3.1, 'Hello', 2.7, 'Python', 5.5, 'world', 17, 'AI']

# Filter untuk memisahkan nilai float, int, dan string
float_data = list(filter(lambda x: isinstance(x, float), random_list))
int_data = list(filter(lambda x: isinstance(x, int), random_list))
string_data = list(filter(lambda x: isinstance(x, str), random_list))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_int_to_dict(n):
    return {'ratusan': n // 100, 'puluhan': (n % 100) // 10, 'satuan': n % 10}

int_mapped = [map_int_to_dict(n) for n in int_data]

# Output
print("Data Float:", float_data)
print("Data Int:")
for item in int_mapped:
    print(item)
print("Data String:", string_data)
