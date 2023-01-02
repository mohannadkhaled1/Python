#not complete yet
import json as js

print('\n ********** welcome to Asab shop ********** \n')
chart = []
total = []
sum = 0
tot = 0

cupPrice={'small ': 5,'medium': 7,'large ': 9}

with open('asab.json','r') as shop:
    db = js.load(shop)

while True :    
    print('- Choose user option \n')
    user = input(' 1- Shop \n 2- Exit \n\n Your choose : ')

    while user == '1' :
        cust = input('\n 1- Show size \n 2- Choose size \n 3- Your chart \n 4- exit \n\n your choose :')

        if cust == '1' :  
            for x, y in cupPrice.items():  
                print(' Size ',x ,' = ',y) 
                
        if cust == '2' : 
            size=input('\n 1- Large \n 2- Medium \n 3- Small \n\n Your choose : ')
            
            if size == '1' :
                qu  = int(input("\n quantity =  "))
                db["large"] = (db["large"][0]+qu, 9)
                tot = cupPrice['large ']*qu
                total.append(tot)
                ch='Large '
                chart.append(ch)
                sum += tot
                
            if size == '2' :
                qu  = int(input(" quantity =  "))
                db["medium"] = (db["medium"][0]+qu, 7)
                tot = cupPrice['medium']*qu
                total.append(tot)
                ch='Medium'
                chart.append(ch)
                sum += tot
                
            if size == '3' :               
                qu  = int(input(" quantity =  "))
                db["small"] = (db["small"][0]+qu, 5)
                tot = cupPrice['small ']*qu
                total.append(tot)
                ch='Small '
                chart.append(ch)
                sum += tot               
                 
        if cust == '3' : 
            print('\n Here is ur pill \n')
            z = len(chart)
            for n in range(z) :  
                print(' Item ',n+1,' ',chart[n],' = ',total[n]) ;

            print('\n Total = ', sum) ;
            db["total"] = (db["total"]+sum)
            
        if cust == '4' : 
            with open('asab.json','w') as shop:
                js.dump(db,shop)
            break

    if user == '2' :
        print('\n       ********** have a nice day :) **********')
        break



# cupPrice.keys()[0] print first key