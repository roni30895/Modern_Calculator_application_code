class Calculator:

    # constructor
    def __init__(self,num1=0,num2=0):
        self.num1=num1
        self.num2 =num2
        
    # 1) Method for addition of two numbers
    def addition(self):
        
        result=self.num1+self.num2
        print("\n\t Addition of {} and {} is = {} ".format(self.num1,self.num2,result))
        flag=True
        while flag:
            print("\n\t 1. To add next number","")
            add_input=int(input("\n\tSelect Option :",))
            
            if add_input==1:
                next_number=int(input("\n\t Enter the Next Number : "))
                new_result= result + next_number
                print("\n\t Addition of {} and {} is = {} ".format(result,next_number,new_result) )
            
            else:
                Flag=False
    
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
                    print("\n\t subtraction of {} and {} is = {} ".format(result,next_number,new_result))
                else:
                    new_result= next_number - result
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
                print("\n\t Multiplication of {} and {} is = {} ".format(result,next_number,new_result) )
            
            else:
                Flag=False
    
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
                print("\n\t Division of {} and {} is = {} ".format(result,next_number,new_result) )
            
            else:
                Flag=False
    
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
    
    # 11) Method for converting currency INR to USD
    def inr_to_usd(self):
        print("\n\t Conversion of Rs.{} into USD is = {} ".format(self.num1,self.num1 * 0.0122107589))
    
    # 12) Method for converting currency USD to INR
    def usd_to_inr(self):
        print("\n\t Conversion of {} USD into INR is = Rs.{} ".format(self.num1,self.num1 * 81.894992))
    
    # 13) Method for finding the area of triangle
    def area_of_triangle(self):
        print("\nt\t Area of Triangle with base {} and height {} is = {} ".format(self.num1,self.num2,0.5 * self.num1 * self.num2))
    
    # 14) Method for finding the area of circle
    def area_of_circle(self):
        print("\n\t Area of circle of radius {} is = {} ".format(self.num1,3.14 * self.num1 * self.num1))

    # 15) Method for finding the area of rectangle
    def area_of_rectangle(self):
        print("\n\t Area of Rectangle with breadth {} and height {} is = {} ".format(self.num1,self.num2, self.num1 * self.num2))
    
    # 16) Method for finding the area of square
    def area_of_square(self):
        print("\n\t Area of square with side {} is = {} ".format(self.num1,self.num2,self.num1 * self.num1))
    
    # 17) Method for finding the percentage
    def find_percentage(self):
        print("\n\t The percentage is = {} % ".format((self.num1/self.num2) * 100))
    
    # 18) Method for finding the Nth degree
    def nth_degree(self):
        print("\n\t The {} degree of {} is = {}".format(self.num2,self.num1,self.num1 ** self.num2))
    
    # 19) Method for finding the Nth root of a number
    def nth_root(self):
        print("\n\t The {} root of {} is = {}".format(self.num2,self.num1,self.num1 **(1/self.num2)))


    # 20) Method for spliiting expenses amongst friends
    def split_expense(self):
        return self.num1 / self.num2


# Driver Code

if __name__=="__main__":

    # For printing the choices

    print(" \n1.  Addition","\n 2.  Substraction","\n 3.  Multiplication","\n 4.  Division","\n 5.  Find Remainder","\n 6.  Floor Division","\n 7.  Find Square","\n 8.  Find Square Root","\n 9.  Find Cube","\n 10. Find Cube Root","\n 11. INR to USD Conversion","\n 12. USD to INR Conversion","\n 13. Find Area of Triangle","\n 14. Find Area of Circle","\n 15. Find Area of Rectangle","\n 16. Find Area of Square""\n 17. Find Percentage","\n 18. Nth Degree of a number","\n 19. Nth root of number","\n 20. Split Expenses","\n")
    
    flag= True
    while flag:
        user_input=int(input("\n Enter your Choice : "))

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
            num=int(input("\n Enter the amount in Rupees which you want to convert into USD : "))
            obj=Calculator(num)
            obj.inr_to_usd()

         # calling conversion of USD to INR function

        elif user_input==12:
            num=int(input("\n Enter the amount in USD which you want to convert into INR : "))
            obj=Calculator(num)
            obj.usd_to_inr()
        
        # calling area of triangle function
        elif user_input==13:
            base=int(input("\n Enter the base of triangle : "))
            height=int(input("\n Enter the height of triangle : "))
            obj=Calculator(base,height)
            obj.area_of_triangle()
        
        # calling area of circle function
        elif user_input==14:
            rad=int(input("\n Enter the radius of circle : "))
            obj=Calculator(rad)
            obj.usd_to_inr()
        
        # calling area of rectangle function
        elif user_input==15:
            breadth=int(input("\n Enter the breadth of rectangle : "))
            height=int(input("\n Enter the height of rectangle : "))
            obj=Calculator(breadth,height)
            obj.area_of_rectangle()

        # calling area of square function
        elif user_input==16:
            side=int(input("\n Enter the side of square: "))
            obj=Calculator(side)
            obj.area_of_square()
        
        # calling finding percentage

        elif user_input==17:
            maximum=int(input("\n Enter the Maximum Marks : "))
            Total=int(input("\n Enter the Total Marks : "))
            obj=Calculator(maximum,Total)
            obj.find_percentage()
        
        # calling nth degree function

        elif user_input==18:
            number=int(input("\n Enter the number : "))
            degree=int(input("\n Enter the Nth degree of a number : "))
            obj=Calculator(number,degree)
            obj.nth_degree()
        
        # calling nth root function

        elif user_input==19:
            number=int(input("\n Enter the number : "))
            root=int(input("\n Enter the Nth root of a number : "))
            obj=Calculator(number,root)
            obj.nth_root()
        
        # calling split expense function
        elif user_input==20:
            expense = float(input("\n Enter the total expense: "))
            num_of_friends = int(input("\n Enter the number of friends: "))
            obj=Calculator(expense, num_of_friends)
            amount_per_friend = obj.split_expense()
            print("\n Each friend needs to pay Rs.%.2f" % amount_per_friend)
        
        # repeatation code
        repeat = input("\n Do you want to go with other choices, if yes then type Y or type N : ")
        if repeat=='N'or repeat=='n':
            flag = False 