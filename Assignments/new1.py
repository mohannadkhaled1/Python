# chart = []
# total = []
# sum = 0
# tot = 0
# items =['banana','Apple','kiwi','potato']
# price =[15 , 20 , 25 , 10]
# quantity=[50,80,70,30]
# print("What should we buy from the shops")
# print("Enter '0' to stop adding items")

# while True:

    # new_item = int(input("iten no. : "))
    # ch=items[new_item-1]
    
    # if new_item == 0:
        # break
 
    # qu= int(input("quantiti =  "))
    # tot = price[new_item-1]*qu
    # sum += price[new_item-1]*qu
    # total.append(tot)
    # chart.append(ch)
    # x = len(chart)
# print("Here's your list:")

# for n in range(x) :  
        # print('item ',n+1,' ',chart[n],' = ',total[n]) ;

# print('total = ', sum) ;
    
        # owner = input('enter username : ')
    # password = input('enter passowrd : ')
    # ow='moha'
    # ps=1111
    # if((owner==ow)&(password==ps)):
    
    
print('\n ********** welcome to ITI grocerry shop ********** \n')
chart = []
total = []
sum = 0
tot = 0
items =['banana','Apple','kiwi','potato']
price =[15 , 20 , 25 , 10]
quantity=[50,80,70,30]

x = len(items)
     
print('- choose user option ')
user = input(' 1- customer \n 2- adiministrator \n 3- exit \n your choose : ')

while user == '1' :
    cust = input(' 1- show products \n 2- buy products \n 3- your chart \n your choose : ')

    if cust == '1' :
                       for n in range(x) :  
                            print('item ',n+1,' ',items[n],' = ',price[n]) ;
    if cust == '2' : 
        print("Enter '0' to stop adding items")

        while True:
            new_item = int(input("iten no. : "))
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