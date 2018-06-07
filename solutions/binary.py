if __name__=="__main__":
    n=int(input())
    a=list(bin(n)[2:])               
    count=0               
    for i in a:          
        if i=='1':       
            count=count+1
        else:            
            break        
print(count)     
                 

