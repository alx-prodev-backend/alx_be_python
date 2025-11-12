# multiplication_table.py

number = int(input("Enter a number to see its multiplication table:"))

# using for loop to generate and print the multiplication table
for i in range(1, 11):
    product = number*i
    print(f"{number} * {i} = {product}")