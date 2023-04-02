import math

user_input = input('MiniCalculator V1.0.0'
                   ' Say hello! ')

if "hello" in user_input.lower():
    print("Hello there!")
else:
    print("404")


user_input = input('Enter a command:'
                   '(subtraction,addition,multiplication,division,to the power of,radical...) ')
#checks for the command you just entered.
if "subtraction" in user_input.lower():
    subtraction1 = input('Give me number: ')
    subtraction2 = input('Give me another number: ')
    result = int(subtraction1) - int(subtraction2)
    print(subtraction1 + ' minus ' + subtraction2 + ' is ')
    print(result)

if "addition" in user_input.lower():
    subtraction1 = input('Give me number: ')
    subtraction2 = input('Give me another number: ')
    result = int(subtraction1) + int(subtraction2)
    print(subtraction1 + ' plus ' + subtraction2 + ' is ')
    print(result)

if "multiplication" in user_input.lower():
    subtraction1 = input('Give me number: ')
    subtraction2 = input('Give me another number: ')
    result = int(subtraction1) * int(subtraction2)
    print(subtraction1 + ' times ' + subtraction2 + ' is ')
    print(result)

if "division" in user_input.lower():
    subtraction1 = input('Give me number: ')
    subtraction2 = input('Give me another number: ')
    result = int(subtraction1) / int(subtraction2)
    print(subtraction1 + ' divided by ' + subtraction2 + ' is ')
    print(result)

if "radical" in user_input.lower():

    num = float(input("Give me number: "))

    sqrt = math.sqrt(num)

    print("The square root of", num, "is", sqrt)


if "to the power of" in user_input.lower():
    subtraction1 = input('Give me number: ')
    subtraction2 = input('Give me another number: ')
    result = int(subtraction1) ** int(subtraction2)
    print(subtraction1 + ' to the power of ' + subtraction2 + ' is ')
    print(result)
else:
    input('You need to enter one of the commands mentioned above (subtraction,addition etc...)'
          ' If you want to go back Go ahead and restart the app!If not,simply press enter to proceed.')

input('Thanks for using MiniCalc by $YS! <3 Now lets play a little game.You will tell me when you were born(year),'
      'and I will tell you how old you are! ')
byear = input('What year were you born in? ')
agg = 2023 - int(byear)
print('You are ' + str(agg) + ' years old!')

answer = input('Is that right? ')
if 'yes' in answer.lower():
    input('Very Well!You can close me by simply pressing Enter or clicking on the X on the top of the screen!')
else:
    input('Looks like an error may have occured with the calculation!or you just could not type yes properly.'
          ' You can close the application by simply pressing ENTER on your keyboard. ')
#all of the variables for the numbers that are entered by the user,are written as subtraction1 and subtraction2.expect the variables of radical because
#radical's code was completely different from the others.
