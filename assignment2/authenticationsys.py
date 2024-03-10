username=input("Enter Name:")
passwd=input("Enter password:")
lastpasswd=[]
for i in range(3):
    a=input("Enter the previously set password:")
    lastpasswd.append(a)
print(lastpasswd)
def passvalidation(u,p,lp):
    def lencheck(p):
     if (len(p)>=10):
        pass
     else:
        print("Password should be 10 characters long.")
    def varietycheck(p):
      smallcase=0
      uppercase=0
      specialchar=0
      for i in (p):
         if p[i].isupper:
            uppercase+=1
         if p[i].islower:
            smallcase+=1
      if uppercase<2:
         print("Password should have atleast  2 uppercase character")
      if smallcase<2:
         print("Password should have atleast  2 smallcase character")
    def spcharcheck(p):
       spchar="`~!@#$%^&*()_+{}=-[]"":;''/|\<>.,₹"
       count=0
       for i in p:
          if p[i] in spchar:
             count+=1
          else:
             pass
       if(count<2):
          print("Password should have atleast  2 character")

       else:
          pass
    def digitcheck(p):
       digit="0987654321"
       count=0
       for i in p:
          if p[i] in digit:
             count+=1
          else:
             pass
       if(count<2):
          print("Password should have atleast  2 character")

       else:
          pass
             

    def seqrep(p,lp):
       i=0
       s=[]
       while(i<(len-4)):
          k=p[i:3]
          s.append[k]
          print(s)
          for i in s:
             for j in lp:
                if s[i] in lp[j]:
                   print("Sequence of letter should not match the last password.")
                   break
                else:
                   pass
          for i in s:
             if s[i][0]==s[i][1]==s[i][2]:
                print("Repetition of character is not allowed.")
                break
             else:
                pass
    def lpcheck(lp,p):
       for i in lp:
          if lp[i]==p:
             print("Password cannot be similar to the previously set password.")
             break
          else:
             pass

passvalidation(username,passwd,lastpasswd)
          
             
             
          
       

        
         
    