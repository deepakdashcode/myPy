def sum(ls,start,end):
    s=0
    for i in range(start,end+1):
        s=s+ls[i]
    return s


specificHeatOfIce=specificHeatOfSteam=0.5
specificHeatOfWater=1.0
LatentHeatOfFusion=80.0
LatentHeatOfVapourisation=540.0
massOfIce=float(input('Enter the mass of ice\n'))
tempOfIce=float(input('Enter the temperature of ice (<0)\n'))

massOfSteam=float(input('Enter the mass of Steam\n'))
tempOfSteam=float(input('Enter the temperature of Steam (>100)\n'))

conversionOfIce=[]
conversionOfIce.append(massOfIce*specificHeatOfIce*(-tempOfIce))
conversionOfIce.append(massOfIce*LatentHeatOfFusion)
conversionOfIce.append(massOfIce*specificHeatOfWater*100)
conversionOfIce.append(massOfIce*LatentHeatOfVapourisation)
conversionOfIce.append(massOfIce*specificHeatOfSteam*(tempOfSteam-100))

conversionOfSteam=[]
conversionOfSteam.append(massOfSteam*specificHeatOfIce*(-tempOfIce))
conversionOfSteam.append(massOfSteam*LatentHeatOfFusion)
conversionOfSteam.append(massOfSteam*specificHeatOfWater*100)
conversionOfSteam.append(massOfSteam*LatentHeatOfVapourisation)
conversionOfSteam.append(massOfSteam*specificHeatOfSteam*(tempOfSteam-100))

ind=0
for i in range(0,5):
    sumOfIce=sum(conversionOfIce,0,i)
    sumOFSteam=sum(conversionOfSteam,i+1,4)
    if ( sumOfIce > sumOFSteam):
        ind=i
        break

print(ind)
if ind==0:
    num=sum(conversionOfSteam,1,4)+(massOfIce*specificHeatOfIce*tempOfIce)
    dino=massOfIce*specificHeatOfIce+massOfSteam*specificHeatOfIce
    T=num/dino
    print('Mass of Ice left = ',(massOfIce+massOfSteam),'All are at {} degree celsius'.format(T))

elif ind==1:
    m=(sum(conversionOfSteam,2,4)-(sum(conversionOfIce,0,0)))/LatentHeatOfFusion
    print("Mass of ice melted = ",abs(m))
    print("Water present is {} and mass of ice present is {} All are at 0 degree celsius".format(massOfSteam+m,massOfIce-m))

elif ind==2:
    num=sum(conversionOfSteam,3,4)-sum(conversionOfIce,0,1)+(100*massOfSteam*specificHeatOfWater)
    dino=massOfIce*specificHeatOfWater+massOfSteam*specificHeatOfWater
    T=num/dino
    print('Mass of Water left = ', (massOfIce + massOfSteam), 'All are at {} degree celsius'.format(T))

elif ind==3:
    m=(sum(conversionOfSteam,4,4)-sum(conversionOfIce,0,2))/LatentHeatOfVapourisation
    print("Mass of ice evaporated to steam  = ", abs(m))
    print("Steam present is {} and mass of water present is {} All are at 100 degree celsius".format(massOfSteam + m, massOfIce - m))

elif ind==4:
    num=massOfSteam*specificHeatOfSteam*tempOfSteam-sum(conversionOfIce,0,3)+(100*massOfIce*specificHeatOfSteam)
    dino=massOfIce*specificHeatOfSteam + massOfSteam*specificHeatOfSteam
    T=num/dino
    print('Mass of steam present is {} all are at {} degree celsius'.format(massOfSteam+massOfIce,T))



