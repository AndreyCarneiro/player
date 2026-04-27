global_var = "Esta variável é global e pode ser acessada de qualquer lugar."
def minha_funcao():
    print("Olá, esta é a minha função!")
    local = "Esta variável é local à função."

# chamando minha função
minha_funcao()

nome = "Andrey" # Variável global

def saudacao():
    sobrenome = "G. Carneiro" # Variável local
    print(f"{nome} {sobrenome}! Bem-vindo ao curso de Python.")

saudacao()

def soma(n1, n2):#n1 e n2 são parâmetros da função
    print(f"A soma é {n1 + n2}")

soma(6, 20)

def formatar_real(valor):
    return f"R$ {valor:.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

#Uso:
preco_hospedagem = 49.99
print(formatar_real(preco_hospedagem))#49,99