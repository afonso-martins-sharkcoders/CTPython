# teste.txt

#teste.txt

# escrever no ficheiro
#ficheiro = open("teste.txt", "w")
#ficheiro.write("Olá...")
#ficheiro.close()
nome = input("Insira o seu nome: ")
nif = input("Insira o seu nif: ")
telemovel = input("Insira o seu telemóvel: ")

# escrever no ficheiro, sem overwrite
ficheiro = open(nome_ficheiro, "a")
ficheiro.write("Nome: {nome} | Nif: {nif} | Telemóvel: {telemóvel}\n")
ficheiro.close()

# lêr o ficheiro
ficheiro = open(nome_ficheiro, "r")
conteudo = ficheiro.read()
print(conteudo)
ficheiro.close()
