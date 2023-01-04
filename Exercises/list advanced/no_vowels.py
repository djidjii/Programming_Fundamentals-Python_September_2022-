# text = input()
#
# vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'U', 'E', 'I', 'O']
# no_vowels = ''.join([x for x in text if x not in vowels])
# print(no_vowels)
#

text = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'U', 'E', 'I', 'O']
result = [ch for ch in text if ch.lower() not in vowels]
print(''.join(result))
