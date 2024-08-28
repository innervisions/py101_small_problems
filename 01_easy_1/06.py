# 06 - Sum or Product of Consecutive Integers

# number = int(input("Please enter an integer greater than 0: "))
# operation = input('Enter "s" to compute the sum, or "p" to compute the product: ')

# if operation == "s":
#     sum = 0
#     for index in range(1, number + 1):
#         sum += index

#     print(f"The sum of the integers between 1 and {number} is {sum}.")
# elif operation == "p":
#     product = 1
#     for index in range(1, number + 1):
#         product *= index

#     print(f"The product of the integers between 1 and {number} is {product}.")
# else:
#     print("Not a valid operation.")


def compute_sum(target_num):
    return sum(range(1, target_num + 1))


def compute_product(target_num):
    result = 1
    for num in range(1, target_num + 1):
        result *= num
    return result


prompt1 = "Please enter an integer greater than 0: "
prompt2 = 'Enter "s" to compute the sum, ' 'or "p" to compute the product: '

number = int(input(prompt1))
operation = input(prompt2)
print()

if operation == "s":
    print(
        "The sum of the integers between 1 and " f"{number} is {compute_sum(number)}."
    )
elif operation == "p":
    print(
        "The product of the integers between 1 and "
        f"{number} is {compute_product(number)}."
    )
else:
    print("Oops. Unknown operation.")
