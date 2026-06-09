product_info = ("SP001", "Ao polo nam", "Size L", 299000)

product_code = product_info[0]

product_name = product_info[1]

product_length = len(product_info)

temp_list = list(product_info)   
temp_list[3] = 279000           
product_info = tuple(temp_list)  

print("Ma san pham:", product_code)
print("Ten san pham:", product_name)
print("So luong thong tin san pham:", product_length)
print("Thong tin san pham sau cap nhat:", product_info)