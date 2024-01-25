# Calculate the multiplication and sum of two numbers

def multiplication_or_sum(num1, num2):
    # calculate product of the two numbers
    product = num1 * num2
    # check if product is less than 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 then calculate the sum
        return num1 + num2
    
# first condition
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = multiplication_or_sum(num1, num2)
print("The result of the first given is", result)