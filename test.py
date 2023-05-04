a ="""Created: Mar 1, 2023 10:52 PM  Updated: Apr 29, 2023 02:06 AM"""
                                    
    
if(a.find("Updated")>1  and a.find("Created")>=0):                                                             
    b=a.split("   ")[-1].split("Updated: ")[1]                          
    print(b)                       
    
else:
    print("Not Working")    
    
    
    

    