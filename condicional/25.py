h1 = int(input("Hora início: "))
m1 = int(input("Min início: "))
h2 = int(input("Hora fim: "))
m2 = int(input("Min fim: "))

inicio = h1*60 + m1
fim = h2*60 + m2

if fim < inicio:
    fim += 24*60

tempo = fim - inicio

print("Horas:", tempo//60)
print("Minutos:", tempo%60)