class shopping():
    shop_name='Abc_Electronics'
    location='chennai'
    items='{Product:[Quantity,Price]}'
    shopcart={'mobile':13,'camera':15,'tablet':12,'laptop':25}
    usercart={}

    def items_details():
        print("{'Mobile':[13,20000],'Camera':[15,50000],'Tablet':[12,35000],'Laptop':[25,60000]}")
    def __init__(self,Name,Phone_no,Address,Cart):
        self.Name=Name
        self.Phone_no=Phone_no
        self.Address=Address
        self.Cart=Cart

    def Customer_details(self):
        print(f'Customer Name :{self.Name}')
        print(f'Customer Phone_no :{self.Phone_no}')
        print(f'Customer Address :{self.Address}')
        print(f'Customer Cart  :{self.Cart}')
 
    def change_Cart(self,new):
         self.Cart=new
    
        

    def display():
        user=['Dinesh',6385373705,'chennai']
        
        product=['mobile','camera','tablet','laptop']
        quantity={'mobile':13,'camera':15,'tablet':12,'laptop':25}
        price={'mobile':20000,'camera':50000,'tablet':35000,'laptop':60000}
        shopcart={'mobile':13,'camera':15,'tablet':12,'laptop':25}
     
        print("~~~~~*~~~~~~~~~~~*~~~~~~~~~~~~*~~~~~~~~~~~*~~~~~~~~~*~~~~~~~~")
        print("Enter 1 To display all the product available in the shop")
        print("Enter 2 To display your details ")
        print("Enter 3 To add the product into your cart")
        print("Enter 4 To remove the product from the cart")
        print("Enter 5 To exit the page")
        n=int(input())
        if n==1:
            print("Product           Quantity        Price")
            print("********************************************")
            for i in shopping.shopcart:
                print(f'{i}              {shopping.shopcart.get(i)}            {price.get(i)}')
            
                
                
            
            
           
            shopping.display()
        elif n==2:
             
            print(f'Customer Name : {user[0]}')
            print(f'Customer Name : {user[1]}')
            print(f'Customer Name : {user[2]}')
            if shopping.usercart=={}:
                print(f"Your Cart is Empty")
            else:
                print(f'Product      Quantity         sub-Total')
                print("********************************************")
                for i in shopping.usercart:
                    print(f"{i}       {shopping.usercart.get(i)}                {price.get(i)*shopping.usercart.get(i)}")

                    
                   
            shopping.display()
    

    
        elif n==3:
            
            print("What Product do you Want?")
            p=input()
            if p in product:
               print('how Many item you want?')
               q=int(input())
               if q<quantity.get(p):
                   print("Available,If you want add this to your cart ***Enter 1 ***or Don't want means ***Enter 2***")
                  
                   a=int(input())
                   if a==1:
                       if shopping.usercart=={}:
                           shopping.usercart[p]=q
                           shopping.shopcart[p]-=q
                           print("Product Added Sucessfully")
                           #print(shopping.shopcart)
                           #print(shopping.usercart)
                           
                       else:
                           if p not in shopping.usercart:
                               shopping.usercart[p]=q
                               shopping.shopcart[p]-=q
                               print("Product Added Sucessfully")

                           else:
                               shopping.usercart[p]+=q
                               shopping.shopcart[p]-=q
                               print("Product Added Sucessfully")
                           
                           
                   else:
                         print("Thank You,Product is Not Added in Your Cart")
                    
               else:
                   print(f"Sorry!,only {shopping.shocart[p]} left ")
            else:
               print("Sorry!-Product its not Available, Once again see shopcart again!")

            shopping.display()





        elif n==4: 
           if shopping.usercart!={}:
              print("Product Available,If you want remove Any product from your cart ***Enter 1 *** or Don't want means ***Enter 2***")
              b=int(input())
              if b==1:
                   print("What product You want to remove ?")
                   p1=str(input())
                   if p1 in shopping.usercart:
                       print("How many number You want to remove")
                       c=int(input())
                       if c<=shopping.usercart[p1]:
                           shopping.usercart[p1]-=c
                           shopping.shopcart[p1]+=c
                           print("Product removed Sucessfully")

                           if shopping.usercart[p1]==0:
                               shopping.usercart.pop(p1,0)
                               #print("Product removed Sucessfully")
                           
                           
                           
                       else:
                           print(f"Only {shopping.usercart[p1]} are in your Cart ")
                      
                   else:
                      print("Sorry,This product is not in your Cart,Check your cart")
           else:
               print("No Product are in the Cart")
                  
           shopping.display()
     
        elif n==5:
            print("Thanks for visiting!")

        else:
          print("Your Number beyond The Range")
   
     
shopping.display()
c1=shopping('Dinesh',6385373705,'chennai',0)
c2=shopping('suriya',9941203861,'chengalpet',0)
