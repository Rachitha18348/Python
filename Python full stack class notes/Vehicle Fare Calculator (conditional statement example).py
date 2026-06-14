vehicle = int(input("1.auto\n2.car\n:"))
if vehicle==1:
    km=int(input())
    if 0<km<=9:
        cost=km*10
        print(f"This {km} km ride costs {cost}.")
    elif 9<km<=20:
        cost=9*10+((km-9)*15)
        print(f"This {km} km ride costs {cost}.")
    elif 20<km<=30:
        cost=5*10+11*15+((km-(5+11))*20)
        print(f"This {km} km ride costs {cost}.")
    elif 30<km<=50:
        cost=5*10+11*15+10*20+((km-(5+11+10))*25)
        print(f"This {km} km ride costs {cost}.")
    else:
        print("Ride not available")
    
elif vehicle==2:
    km=int(input())
    
    if 0<km<=50:
        cost=km*17
        Total_cost=cost+200
        print(f"This ride {km} km ride costs {cost} but extra 200 for driver so total cost is:{Total_cost}.")
    elif 50<km<=100:
        cost=50*17+((km-50)*21)
        Total_cost=cost+300
        print(f"This ride {km} km ride costs {cost} but extra 300 and food for driver so total cost is:{Total_cost} + food.")
    elif 100<km<=160:
        cost=50*17+50*21+((km-(50+50))*30)
        Total_cost=cost+300+300
        print(f"This ride {km} km ride costs {cost} but extra 300 for tollfree, extra 300 and food for driver so total cost is:{Total_cost} + food.")
    elif 160<km<=200:
        cost=50*17+50*21+60*30+((km-(50+50+60))*33)
        Total_cost=cost+1000
        print(f"This ride {km} km ride costs {cost} but extra 1000 for driver so total cost is:{Total_cost}.")
    else:
        print("Ride not available")
else:
    print("Wrong choice of Vehicle:")
    
