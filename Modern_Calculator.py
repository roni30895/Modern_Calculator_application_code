import requests
class Calculator:

    # constructor
    def __init__(self,num1=0,num2=0,):
        self.num1=num1
        self.num2 =num2
        
    # 1) Method for addition of two numbers
    def addition(self):
        
        result=self.num1+self.num2
        print("\n\t Addition of {} and {} is = {} ".format(self.num1,self.num2,result))
        flag=True
        while flag:
            print("\n\t 1. To add next number","\n\t 2. Exit")
            add_input=int(input("\n\tSelect Option :",))
            
            if add_input==1:
                next_number=int(input("\n\t Enter the Next Number : "))
                new_result= result + next_number
                result=new_result
                print("\n\t Addition of {} and {} is = {} ".format(result,next_number,new_result) )
            
            else:
                flag=False
    
    # 2) Method for Subtraction of two numbers
    def subtraction(self,):
        if self.num1 > self.num2:
            result= self.num1-self.num2
            print("\n\t subtraction of {} and {} is = {} ".format(self.num1,self.num2,result))
        else:
            result= self.num2-self.num1
            print("\n\t subtraction of {} and {} is = {} ".format(self.num2,self.num1,result))
        
        flag=True
        while flag:
            print("\n\t 1. To Substract next number","\n 2.Exit")
            sub_input=int(input("\n\tSelect Option :",))
            
            if sub_input==1:
                next_number=int(input("\n\t Enter the Next Number : "))
                if result > next_number:
                    new_result= result - next_number
                    result=new_result
                    print("\n\t subtraction of {} and {} is = {} ".format(result,next_number,new_result))
                else:
                    new_result= next_number - result
                    result=new_result
                    print("\n\t subtraction of {} and {} is = {} ".format(result,next_number,new_result))

            else:
                flag=False         
            
    
    # 3) Method for addition of two numbers
    def multiplication(self):
        result= self.num1 * self.num2
        print("\n\t Multiplication of {} and {} is = {} ".format(self.num1,self.num2,result))
        flag=True
        while flag:
            print("\n\t 1. To multiply with next number","")
            add_input=int(input("\n\tSelect Option :",))
            
            if add_input==1:
                next_number=int(input("\n\t Enter the Next Number : "))
                new_result= result + next_number
                result=new_result
                print("\n\t Multiplication of {} and {} is = {} ".format(result,next_number,new_result) )
            
            else:
                flag=False
    
    # 4) Method for Division of two numbers
    def division(self):
        result= self.num1 / self.num2
        print("\n\t Division of {} and {} is = {} ".format(self.num1,self.num2,result))
        flag=True
        while flag:
            print("\n\t 1. To divide with next number","")
            add_input=int(input("\n\tSelect Option :",))
            
            if add_input==1:
                next_number=int(input("\n\t Enter the Next Number : "))
                new_result= result + next_number
                result=new_result
                print("\n\t Division of {} and {} is = {} ".format(result,next_number,new_result) )
            
            else:
                flag=False
    
    # 5) Method for finding remainder of two numbers
    def find_remainder(self):
        if self.num1 > self.num2:
            print("\n\t Remainder of {} and {} is = {} ".format(self.num1,self.num2,self.num1 % self.num2))
        else:
            print("\n\t Remainder of {} and {} is = {} ".format(self.num2,self.num1,self.num2 % self.num1))
         
    # 6) Method for floor Division of two numbers
    def floor_division(self):
        print("\n\t Division of {} and {} is = {} ".format(self.num1,self.num2,self.num1 // self.num2))
    
    # 7) Method for finding square
    def find_square(self):
        print("\n\t Square of {} is = {} ".format(self.num1,self.num1 * self.num1))

    # 8) Method for finding square root
    def find_square_root(self):
        print("\n\t Square Root of {} is = {} ".format(self.num1,self.num1 ** 0.5))
    
    # 9) Method for finding cube
    def find_cube(self):
        print("\n\t Cube of {} is = {} ".format(self.num1,self.num1 ** 3))
    
    # 10) Method for finding cube root
    def find_cube_root(self):
        print("\n\t Cube of {} is = {} ".format(self.num1,self.num1 ** (1/3)))
    
    # 11) Method for currency converter
    def currency_converter(self,amount):
        response= requests.get(
            f"https://api.frankfurter.app/latest?amount={amount}&from={self.num1}&to={self.num2}"
        )
        #print(response.status_code)
        print(f"\n {amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")
        
    # 12) Method for finding the area of triangle
    
    def area_of_triangle(self):
        print("\nt\t Area of Triangle with base {} and height {} is = {} ".format(self.num1,self.num2,0.5 * self.num1 * self.num2))
    
    # 13) Method for finding the area of circle
    def area_of_circle(self):
        print("\n\t Area of circle of radius {} is = {} ".format(self.num1,3.14 * self.num1 * self.num1))

    # 14) Method for finding the area of rectangle
    def area_of_rectangle(self):
        print("\n\t Area of Rectangle with breadth {} and height {} is = {} ".format(self.num1,self.num2, self.num1 * self.num2))
    
    # 15) Method for finding the area of square
    def area_of_square(self):
        print("\n\t Area of square with side {} is = {} ".format(self.num1,self.num2,self.num1 * self.num1))
    
    # 16) Method for finding the percentage
    def find_percentage(self):
        print("\n\t The percentage is = {} % ".format((self.num1/self.num2) * 100))
    
    # 17) Method for finding the Nth degree
    def nth_degree(self):
        print("\n\t The {} degree of {} is = {}".format(self.num2,self.num1,self.num1 ** self.num2))
    
    # 18) Method for finding the Nth root of a number
    def nth_root(self):
        print("\n\t The {} root of {} is = {}".format(self.num2,self.num1,self.num1 **(1/self.num2)))


    # 19) Method for spliiting expenses amongst friends
    def split_expense(self,who_paid,split_with):
        split_amount= amount/len(split_with)
    
        for name in split_with:
            if name!=who_paid:
                print("\n\t{} you need to pay Rs.{} to {} for {}".format(name,split_amount,who_paid,for_what))
        


# Driver Code

if __name__=="__main__":

    # For printing the choices

    print("\n 1.  Addition","\n 2.  Substraction","\n 3.  Multiplication","\n 4.  Division",
    "\n 5.  Find Remainder","\n 6.  Floor Division","\n 7.  Find Square","\n 8.  Find Square Root",
    "\n 9.  Find Cube","\n 10. Find Cube Root","\n 11. Currency Converter",
    "\n 12. Find Area of Triangle","\n 13. Find Area of Circle","\n 14. Find Area of Rectangle",
    "\n 15. Find Area of Square""\n 16. Find Percentage","\n 17. Nth Degree of a number",
    "\n 18. Nth root of number","\n 19. Split Expenses","\n")
    
    flag= True
    while flag:
        user_input=int(input("\n Enter the number which functionality you want to use : "))

        # calling addition function
        if user_input==1:
            first_num=int(input("\n Enter the first Number : "))
            second_num=int(input("\n Enter the second Number : "))
            obj=Calculator(first_num,second_num)
            obj.addition()
        
        # calling Subtraction function
        elif user_input==2:
            first_num=int(input("\n Enter the first Number : "))
            second_num=int(input("\n Enter the second Number : "))
            obj=Calculator(first_num,second_num)
            obj.subtraction()

        # calling multiplication function

        elif user_input==3:
            first_num=int(input("\n Enter the first Number : "))
            second_num=int(input("\n Enter the second Number : "))
            obj=Calculator(first_num,second_num)
            obj.multiplication()
        
        # calling division function

        elif user_input==4:
            first_num=int(input("\n Enter the first Number : "))
            second_num=int(input("\n Enter the second Number : "))
            obj=Calculator(first_num,second_num)
            obj.division()
        
        # calling finding remainder function

        elif user_input==5:
            first_num=int(input("\n Enter the first Number : "))
            second_num=int(input("\n Enter the second Number : "))
            obj=Calculator(first_num,second_num)
            obj.find_remainder()
        
        # calling Floor division function

        elif user_input==6:
            first_num=int(input("\n Enter the first Number : "))
            second_num=int(input("\n Enter the second Number : "))
            obj=Calculator(first_num,second_num)
            obj.floor_division()
        
        # calling find square function

        elif user_input==7:
            num=int(input("\n Enter the Number : "))
            obj=Calculator(num)
            obj.find_square()
        
        # calling find square root function

        elif user_input==8:
            num=int(input("\n Enter the Number : "))
            obj=Calculator(num)
            obj.find_square_root()
        
        # calling find cube function

        elif user_input==9:
            num=int(input("\n Enter the Number : "))
            obj=Calculator(num)
            obj.find_cube()

        # calling find cube root function

        elif user_input==10:
            num=int(input("\n Enter the Number : "))
            obj=Calculator(num)
            obj.find_cube_root()

        # calling conversion of INR to USD function

        elif user_input==11:
            from_currency=str(input("\n Enter the currency you would like to convert from : ")).upper()
            to_currency=str(input("\n Enter the currency you would like to convert to : ")).upper()
            amount=int(input("\n Enter the amount of money = "))
            obj=Calculator(from_currency,to_currency)
            obj.currency_converter(amount)

       
        # calling area of triangle function
        elif user_input==12:
            base=int(input("\n Enter the base of triangle : "))
            height=int(input("\n Enter the height of triangle : "))
            obj=Calculator(base,height)
            obj.area_of_triangle()
        
        # calling area of circle function
        elif user_input==13:
            rad=int(input("\n Enter the radius of circle : "))
            obj=Calculator(rad)
            obj.usd_to_inr()
        
        # calling area of rectangle function
        elif user_input==14:
            breadth=int(input("\n Enter the breadth of rectangle : "))
            height=int(input("\n Enter the height of rectangle : "))
            obj=Calculator(breadth,height)
            obj.area_of_rectangle()

        # calling area of square function
        elif user_input==15:
            side=int(input("\n Enter the side of square: "))
            obj=Calculator(side)
            obj.area_of_square()
        
        # calling finding percentage

        elif user_input==16:
            maximum=int(input("\n Enter the Maximum Marks : "))
            Total=int(input("\n Enter the Total Marks : "))
            obj=Calculator(maximum,Total)
            obj.find_percentage()
        
        # calling nth degree function

        elif user_input==17:
            number=int(input("\n Enter the number : "))
            degree=int(input("\n Enter the Nth degree of a number : "))
            obj=Calculator(number,degree)
            obj.nth_degree()
        
        # calling nth root function

        elif user_input==18:
            number=int(input("\n Enter the number : "))
            root=int(input("\n Enter the Nth root of a number : "))
            obj=Calculator(number,root)
            obj.nth_root()
        
        # calling split expense function
        elif user_input==19:
            amount=int(input("\n Enter the amount : "))
            for_what=input("\n This is for what? : ").upper()
            who_paid=input("\n Paid By : ").upper()
            print("\n Choose with whom you want to split ")
            print("\n 1. Shubham", "\n 2. Palkesh", "\n 3. Anuj", "\n 4. Balaji",
            "\n 5. Virendra","\n 6. Rohan" )
            split_with=input("\n Enter the names : ").upper().split()
            obj=Calculator(amount,for_what)
            obj.split_expense(who_paid,split_with)
            
        
        # repeatation code
        repeat = input("\n Do you want to go with other choices, if yes then type Y or type N : ")
        if repeat=='N'or repeat=='n':
            flag = False 