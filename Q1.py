print("**************************************************************************")
print("*                         MUDY   SUPER   SHOP                            *")
print("**************************************************************************")
n=0
t=str("--")
time=str("--")
profit=200000
nazi=0
by=0
sal=0
ch=input("You need to choice? (Y/N):")
while(ch=="Y" or ch=="y"):
      print("______________________________")
      print("*    P---PURCHASED           *")
      print("*    S---SALES               *")
      print("*    C---CHECK BALANCE       *")
      print("_____________________________*")
      ab=input("Enter your transaction:")
      if(ab=="P" or ab=="p"):
          buy=int(input("Enter Tsh used to purchase:"))
          from datetime import datetime
          t=datetime.now()
          print("**************************************************************************************************")
          print("**MUDY SUPER SHOP umefamya manunuzi ya Tsh",buy," at ",t,"*")
          profit=profit-buy
          by=by+buy
          print("**************************************************************************************************")
          print("***Thank you for purchase*******you can made other transaction bellow******")
      elif(ab=="s" or ab=="S"):
          from datetime import datetime
          time=datetime.now()
          n=n+1
          print("MTEJA NO:",n)
          name=input("Jila la mteja:")
          nazi=int(input("NAZI NO:"))
          sale=1000*nazi
          profit=profit+sale
          sal=sal+sale
          print("NAZI ",nazi," ni Tsh ",sale)
          print("******************************************************************************************************************")
          print("** Umefanikiwa kuuza NAZI ",nazi," kwa Tsh ",sale,"/= kwa mteja ",name," tarehe ***** ",time)
          print("******************************************************************************************************************")
          print("***Thank yuo for sale*******you can choice other transaction bellow******")
      elif(ab=="c" or ab=="C"):
          print("__________________________________________________________________________________________________________________")
          print("*******Your remaining balance is Tsh:",profit,"/=")
          print("***After made the following transaction")
          print("***Purchase of Tsh:",by,"/=ON LAST DATE:",t)
          print("***Sales on retail Tsh:",sal,"/=ON LAST DATE:",time)
          print("___________________________________________________________________________________________________________________")
          print("******Thank you for chech your balance*******************")
          print("******Made other trnsaction*********")
      else:
          print("**You have error***please try again**")      
if(ch=="N" or ch=="n"):
    print("****************Ok thank you good bye******************")
    
      
      
          
          
          
          
        
        
                  
            
            
                  
                  
            
                  
                  
                  
                  
            
            
      

          
          
          
             
             
      
                           
      
      
      
      