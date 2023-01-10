import re

n = int(input())

for num in range(n):
    barcode = input()
    pattern = r'\@\#+[A-Z][A-Za-z0-9]{4,}[A-Z]\@\#+'
    result = re.findall(pattern, barcode)

    if result:
        barcode = ''.join(result)
        product_group = ''.join([x for x in barcode if x.isdigit()])
        if not product_group:
            product_group = '00'
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
