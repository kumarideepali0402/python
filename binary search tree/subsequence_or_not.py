s="abacbadc"
t="acd"
i=0
j=0
while(i<len(s)) and (j<len(t)):
    if(t[j]==s[i]):
        i+=1
        j+=1
    else:
        i+=1
if(j==len(t)):
    print(True)
else:
    print(False)






