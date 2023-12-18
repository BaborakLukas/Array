#you have a roof thats 200m2 and a two different colours. Green colour costs 45 and can cover 0,4 meters of the roof and the Red one costs 53
#and can cover 0,7 meters of the roof. Wich one is the more cost efficient 

roof= 200
color1 = 45
colorcoverage1 = 0.4
color2 = 53
colorcoverage2 = 0.7

x= color1*colorcoverage1*roof
y= color2*colorcoverage2*roof




if(x>y): 
    print("The green is more cost efficient",x-y)
else: print("The red colour is less expensive",y-x)