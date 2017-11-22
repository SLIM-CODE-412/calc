import re
print ("Our super calculator")
print("Type 'quit' to exit\n")


previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    # if this is first equation
    if previous == 0:
        equation = input("Enter Equation:")
    else:
        equation = input(str(previous))

    #Option to quit out of application
    if equation == 'quit':
        print("Goodbye thanks for using my calulator")
        run = False
    else:
        #limiting eval func to only accept numbers and operators with Regex(keeping it safe).
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        #evaluation input equation
        if previous == 0:
            previous = eval(equation)
        else:
            #displaying previous equiation eval when adding more calculations
            previous = eval(str(previous) + equation)





while run:
    performMath()