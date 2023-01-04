string = list(map(int, input().split(", ")))

found_indicate_or_no = map(lambda x: x if string[x] % 2 == 0 else "no", range(len(string)))
even_indicate = list(filter(lambda a: a != 'no', found_indicate_or_no))
print(even_indicate)
