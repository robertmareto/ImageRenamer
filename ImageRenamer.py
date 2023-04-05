import os
from PIL import Image

pasta_origem = input("Digite o caminho para a pasta de origem: ")
pasta_destino = input("Digite o caminho para a pasta de destino: ")
numero = input("Digite o número a ser adicionado ao final do nome: ")

# Cria a pasta de destino se ela ainda não existir
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Percorre todos os arquivos da pasta de origem
for arquivo in os.listdir(pasta_origem):
    # Verifica se o arquivo é uma imagem e não está corrompido
    try:
        imagem = Image.open(os.path.join(pasta_origem, arquivo))
        imagem.verify()
    except:
        print(f"Arquivo {arquivo} não é uma imagem válida ou está corrompido.")
        continue

    # Divide o nome do arquivo e a extensão
    nome, extensao = os.path.splitext(arquivo)

    # Renomeia o arquivo adicionando o número ao final do nome e move para a pasta de destino
    novo_nome = nome + numero + extensao
    os.rename(os.path.join(pasta_origem, arquivo), os.path.join(pasta_destino, novo_nome))
    print(f"Imagem {arquivo} renomeada e movida para {pasta_destino}")
print("============================================")
print("Processamento concluído!")
input("Pressione Enter para sair...")