idade = 18
altura = 1.69

# altura = (float(input("Qual sua altura: ")))

if idade >= 18:
    print("Você é maior de idade.")
    
    if altura >= 1.70:
        print("Você também tem uma altura considerável.")
    else:
        print("Sua altura não atinge o critério.")
else:
    print("Você é menor de idade.")
