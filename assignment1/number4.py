import itertools

my_dict ={
    "vowels":['a', 'e', 'i', 'o', 'u'],
    "consonants":['w', 'y', 'c', 'h', 'j']
}

combinations = list(itertools.product(*my_dict.values()))

for combo in combinations:
    print(''.join(combo).capitalize())