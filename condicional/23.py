v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))
v3 = int(input("Digite o terceiro valor: "))
v4 = int(input("Digite o quarto valor: "))

if(v4 < v1):
    print(v4, ",", v1, ",", v2,",", v3)
elif(v4 < v2):
    print(v1, ",", v4, ",", v2,",", v3)
elif(v4 < v3):
    print(v1, ",", v2,",",v4, "," ,v3)   
else:
    print(v1, ",", v2,",", v3 , ",", v4)