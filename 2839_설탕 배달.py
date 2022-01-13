kg = int(input())

bag = 0
while kg >= 0 :
    if kg % 5 == 0 :
        bag += (kg // 5)
        print(bag)
        break
    kg -= 3  
    bag += 1
else :
    print(-1)