if __name__=="__main__":
         n=int(input())
         def factorial(n):
             while n==1:
                 return 1
             else:
                 return n*factorial(n-1) 
         print(factorial(n))

