# Meu primeiro projeto python!!!
#
#print() = comando de saida
print("Alo mundo!")

# Quando quiserguardar uma string!(frase)
nome = "Gabriel Ferreira"
# Quando quiser guardar um numero inteiro
idade = 20

# Exibir o meu nome (que está dentro da variável nome)
print(nome)
# Quando quiser exibir a frase "Minha idade é " completando com o conteudo da variavel idade
#print("Minha idade é "+idade)
print("Minha idade é "+str(idade))
print(f"Minha idade é {idade} anos\n")
print("Minha idade é {} anos".format(idade))

# Quando quiser exiber "Meu nome é... e tenho... anos..." trocando pelas variáveis nome e idade
print ( "Meu nome é {} e tenho {} anos" . format ( nome , idade ))