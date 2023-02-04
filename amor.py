print("Calculadora do amor")
print("<3 "*7)

nomes = input("Digite o nome de 2 pessoas: ").strip().lower()

placar = 0

for letra in nomes:
    if letra in "aeiou":
        placar += 5   
    if letra in "amor":
        placar += 10

print(f"Seu placar de compatibilidade : {placar}")

if placar < 10:
    print("Esqueça esta pessoas! Nunca vai dar certo!")
else:
    print("Vocês terão um relacionamento muito intenso! <3")
