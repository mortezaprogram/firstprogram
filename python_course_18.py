def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    num1=float(input("Please input your first number: "))
    for symbol in operations:
        print(symbol)
    should_continue=True
    while should_continue:
        selected_operator=input("Please input your selected operation: ")
        num2=float(input("Please input your next number: "))
        selected_calculation=operations[selected_operator]
        answer=selected_calculation(num1,num2)
        print(f" {num1} {selected_operator} {num2} = {answer}")
        if input(f"Please insert y if you want to continue calculation with {answer} or intert n for new calculation:")=="y":
            num1=answer
        else:
            should_continue=False
            calculator()
calculator()