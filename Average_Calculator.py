list = []
number_input = True

print("Input numbers to find the average and type done when your finished: ")

while number_input == True:
    input_ = input()
    if input_ == "done":
        number_input = False
    elif input_ == "Done":
        number_input = False
    else:
        try:
            number = float(input_)
            list.append(number)
        except:
            print("You have not input a number!")

print("This is the list: ", list)

if len(list) == 0:
    print("You have not input a number into the list. Try again!")
    exit()

def average(list):
    sum_ = sum(list)
    num_values = len(list)
    average = sum_/num_values
    return average

average_ = average(list)
print("This is the average:", average_)
print("Thank you")