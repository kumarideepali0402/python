print("type of coach:3ac,2ac,1ac,sleeper")
tc=(input())
print("type of joourney:monthlypass,onetime")
tj=(input())
cost=0
if(tc=="3ac"):
    cost=400
elif(tc=="2ac"):
    cost=300
elif(tc=="1ac"):
    cost=200
elif(tc=="sleeper"):
    cost=100
print("disc:")
d=float(input())
if(tj=="monthlypass"):
    cost=(cost*30)*(1-d*0.01)
    print(cost)
