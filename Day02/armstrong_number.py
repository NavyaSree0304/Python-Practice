class Solution:
    def armstrongNumber (self, n):
        res=0
        for i in str(n):
            res+=int(i)**len(str(n))
        if res == n:
            return True
        else:
            return False
        # code here 
        
