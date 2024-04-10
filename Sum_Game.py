class Solution:
    def sumGame(self, num: str) -> bool:#new Approach
        #T(C(N)==O(N)) and S(C(N)=O(1)) as it requires nn additional space iteratively
        q, s, n = 0, 0, len(num)#varibales declare and initilaize 
        for i in range(n):#iterating theough nums length
            if num[i]=='?':#nums's ? found
                q = q+1 if i<n//2 else q-1#increment first odd half difference nd decrement even half difference
            else:s = s+int(num[i]) if i<n//2 else s-int(num[i])#increment integer charcter 
        return not(q%2==0 and q//2*9+s==0)#printing alice or bob first Odd's game win  
        
        #old Approach
# class Solution:
#     def sumGame(self, num: str) -> bool:
 
        # a=b=0;r=l=0;n=len(num)
        # for c in num[: n//2]:
        #     if c=="?":a+=1
        #     else:l+=int(c)
        # for c in num[n//2 :]:
        #     if c=="?":b+=1
        #     else:r+=int(c)

        #     if (a+b)%2==1:return True

        #     if l-r==9*(b-a)//2:return False
        # return True
