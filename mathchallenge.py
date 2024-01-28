import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    # expr = str(left) + " "+ operator + str(right)
    expr= str(left) +" "+ operator +" "+ str(right)
    #eval evalues the string as python expression
    answer = eval(expr)
    # Example variable

    # Check if the variable is a string



    # determine the data type
    data_type = type(answer)

  
   


    return expr, answer

expr, answer = generate_problem()

# print(expr)
# print(answer)



# IN ORDER TO SHOW WHAT RETURNS THOSE STEPS BELOW NEED TO BE DONE
# expr, answer = generate_problem()
# print(f"Expression: {expr} - Answer: {answer}")


# Example variable


wrong = 0
input("press enter to start")
print("------------------------")

start_time = time.time()
 

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1)+ ": " + expr + " = ")
        if guess.strip() == str(answer):
           break
        wrong += 1

end_time = time.time()
total_time = round(end_time -start_time, 2)

print("------------------------")
print("Nice word")
print("Nice job! your time is , ", total_time / 60, "minutes!")
    