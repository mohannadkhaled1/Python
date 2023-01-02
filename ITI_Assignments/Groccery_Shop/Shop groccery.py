print('\n ********** Welcome to ITI grocerry shop ********** \n')
chart = []
total = []
sum = 0
tot = 0
items =['banana','Apple ','kiwi  ','potato']
price =[15 , 20 , 25 , 10]
quantity=[50,80,70,30]
x = len(items)

while True :    
    print('- choose user option ')
    user = input(' 1- customer \n 2- adiministrator \n 3- exit \n your choose : ')

    while user == '1' :
        cust = input(' 1- show products \n 2- buy products \n 3- your chart \n 4- exit \n your choose :')

        if cust == '1' :
            for n in range(x) :  
                print('item ',n+1,' ',items[n],' = ',price[n]) ;
                
        if cust == '2' : 
            print("Enter '0' to stop adding items")

            while True:
                new_item = int(input("item no. : "))
                ch=items[new_item-1]
                
                if new_item == 0:
                    break
             
                qu= int(input("quantity =  "))
                tot = price[new_item-1]*qu
                sum += price[new_item-1]*qu
                total.append(tot)
                chart.append(ch)
                
        if cust == '3' : 
            print('here is ur pill')
            z = len(chart)
            for n in range(z) :  
                print('item ',n+1,' ',chart[n],' = ',total[n]) ;

            print('total = ', sum) ; 
            
        if cust == '4' :        
            break
            
    while user == '2' :
        admin = input(' 1- show products \n 2- add products \n 3- change cost \n 4- delete product \n 5- exit \n your choose :  ')
                
        if admin =='1' : 
            for n in range(x) :  
                print('item ',n+1,' ',items[n],' = ',price[n]) ; 
                        
        if admin =='2' :  
            new = input ("\n enter your item : ") ; 
            y = int(input (" enter its value : ")) ;
            q = int(input (" enter its quantity : "));
            items.append(new) ;price.append(y) ;quantity.append(q) ;
            print('\n list with new item \n')
            x = len(items)
            for n in range(x) :  
                print('item ',n+1,' ',items[n],' = ',price[n], 'quantity',quantity[n]) ; 
                                    
        if admin =='3' :  
                new = int(input ("\n enter your item no. : ")); 
                y = input (" enter new value : ") ;
                price[new-1]=y;
                print('\n list with new cost of item \n')
                x = len(items)
                for n in range(x) :  
                    print('item ',n+1,' ',items[n],' = ',price[n]) ;  
                                    
        if admin =='4' : 
                rem = int(input ("enter your item no. : "))
                items.pop(rem-1);
                price.pop(rem-1);
                quantity.pop(rem-1);
                x = len(items)
                for n in range(x) :  
                    print('item ',n+1,' ',items[n],' = ',price[n]) ;
        if admin == '5' :        
            break

    if user == '3' :
        print('\n       ********** have a nice day :) **********')
        break
