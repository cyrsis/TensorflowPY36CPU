char_count = {'a': 5, 'b': 7, 'A': 5, 't': 8, 'B': 10}

char_freq = dict()

for key, value in char_count.items():
    if key.lower() in char_freq:
        char_freq[key.lower()] += value
    else:
        char_freq[key.lower()] = value

# print(char_freq)

# var_name = {
#     key : value
#     for loop_var in collection
#
# }


char_freq2 = {
    key.lower():char_count.get(key.lower(),0) + char_count.get(key.upper(),0)

    for key in char_count.keys()

}

print(char_freq2 == char_freq)
