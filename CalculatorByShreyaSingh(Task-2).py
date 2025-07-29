class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def summation(self):
        summation=self.num1+self.num2
        return summation
    
    def subs(self):
        subs=self.num1-self.num2
        return subs
    
    def multiply(self):
        multiply=self.num1*self.num2
        return multiply
    
    def devide(self):
        devide=self.num1/self.num2
        return devide

num1=int(input("Enter the First Number: "))
num2=int(input("Enter the Second Number: "))
answer=Calculator(num1,num2)
Enter="0"
while Enter!="5":
    print("What you want to choose:")
    print("1. Sum") 
    print("2. Substraction")   
    print("3. Multiply")
    print("4. Division")
    Enter=input("")

    if Enter=="1":
        FinalAnswer=answer.summation()
        print("The sum =",FinalAnswer)
    
    if Enter=="2":
        FinalAnswer=answer.subs()
        print("The substration =",FinalAnswer)

    if Enter=="3":
        FinalAnswer=answer.multiply()
        print("The multiplication =",FinalAnswer)
    
    if Enter=="4":
        FinalAnswer=answer.devide()
        print("The devision =",FinalAnswer)

print("Your program has ended")
    


    




