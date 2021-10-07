nama = ""
letter = input("result :")
s = len(letter)
s2 = nama.count("letter")

#Find input 
if letter:
    print("tidak ada data :", nama.find(letter) != -1, "Jumlah huruf", s , s2)
#function title() same type capitalize()
nama = "sil na nasi"
print(nama.title())
#function zip

# list of tuples containing products and prices
products_and_prices = [('table', 50), ('chair', 20), ('sofa', 200), ('bed', 150), ('lamp', 10)]

# unzip the list of tuples into two tuples with the zip function and the unpacking operator *
products, prices = zip(*products_and_prices)

# tuple of products
print(products)
# ('table', 'chair', 'sofa', 'bed', 'lamp')

# tuple of prices
print(prices)
# (50, 20, 200, 150, 10)