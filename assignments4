#1.
def sum_numbers(num_list):
    total = 0
    for num in num_list:
        total = total + num
    return total
sum_result = sum_numbers([10, 10, 10])
print(sum_result)

#2.
def avg_numbers(num1, num2):
    average = (num1 + num2) / 2
    return average
avg_result = avg_numbers(10, 2)
print(avg_result)

#3.
def biggest_numbers(num_list):
    biggest = num_list[0]
    for num in num_list:
        if num > biggest:
            biggest = num
    return biggest
biggest = biggest_numbers([10, 1, 9, -1, 20])
print(biggest)

#4.
import random
print("Hello! What is your name?")
name = input()
number = random.randint(1, 20)
chances = 6
print("Well,", name, ", I am thinking of a number between 1 and 20.")
while chances > 0:
    print("Take a guess. You have", chances, "chances left.")
    guess = int(input())

    if guess > number:
        print("Your guess is too high.")
    elif guess < number:
        print("Your guess is too low.")
    else:
        print("Good job,", name, "! You guessed my number!")
        break
    chances = chances - 1
if chances == 0:
    print("Sorry! The number was", number)