while True :
    print(' ********** Welcome to ITI calculator ********** \n choose user option ')
    user = input(' 1- scientific \n 2- programmable \n 3- exit \n your choose : ')
    while user == '1' :
            op = input(' enter operation : \n1- + \n2- - \n3- * \n4- / \n5- % \n6- exit \nyour choose : ')
            if op == '1' :
                        num1= float(input(' your first number : '))
                        num2= float(input(' your second number : '))
                        print(" Their sum = ",num1+num2)
            if op == '2' : 
                        num1= float(input(' your first number : '))
                        num2= float(input(' your second number : '))
                        print(" Their subtraction = ",num1-num2)     
            if op == '3' :
                        num1= float(input(' your first number : '))
                        num2= float(input(' your second number : '))
                        print(" Their multiplication = ",num1*num2)
            if op == '4' :
                        num1= float(input(' your first number : '))
                        num2= float(input(' your second number : '))
                        print(" Their division = ",num1 / num2)
            if op == '5' : 
                        num1= float(input(' your first number : '))
                        num2= float(input(' your second number : '))
                        print(" Their modulus = ",num1%num2)
            if op == '6' :
                break
                        
    while user == '2' :
            op = input(' enter operation : \n1- hex \n2- bin \n3- oct \n4- dec \n5- << \n6- >> \n7- & \n8- | \n9- ~ \n10- ^ \n11- exit \nyour choose : ')
            
            if op == '1' : 
                                num1 =input(' Enter your value : ')
                                print(" hex conversion : ",hex(int(num1)))
            if op == '2' :
                                num1 = input(' Enter your value : ')
                                print(" bin conversion : ",bin(int(num1)))    
            if op == '3' :
                                num1 = input(' Enter your value : ')
                                print(" oct conversion : ",oct(int(num1)))
            if op == '4' : 
                                num1 = input(' Enter your value : ')
                                print(" dec conversion : ",int(num1))
            if op == '5' :
                                num1 = input(' Enter your value : ')
                                num2 = input(' shift iteration : ')
                                print(" Result: ",int(num1)<<int(num2))
            if op == '6' : 
                                num1 = input(' Enter your value : ')
                                num2 = input(' shift iteration : ')
                                print(" Result: ",int(num1)>>int(num2))
            if op == '7' : 
                                num1 = input(' Enter your first value : ')
                                num2 = input(' Enter your second value : ')
                                print(" Their AND : ",int(num1)&int(num2))
                        
            if op == '8' : 
                                num1 = input(' Enter your first value : ')
                                num2 = input(' Enter your second value : ')
                                print(" Their OR : ",int(num1)|int(num2))
            if op == '9' :
                                num1 = int(input(' Enter your value : '))
                                print(" complement conversion : ",~(num1-1))
            if op == '10' : 
                                num1 = input(' Enter your first value : ')
                                num2 = input(' Enter your second value : ')
                                print(" Their XOR : ",int(num1)^int(num2))
            if op == '11' :
                break
                
    if user == '3' :
        print('\n       ********** Good bye :) **********')
        break