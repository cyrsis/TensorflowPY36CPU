square = []
for n in range(11):
    square.append(n ** 2)

print(square)

# List comprehen

# [] list
# var_name = [out_exp for loop_var in collection cond]

square2 = [n ** 2 for n in range(11) if n%2 is 0  ]

print(square2)

square3 = [ n**3 for n in range(11) if n%2 is 0  ]
print(square3)
