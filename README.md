# ImageRenamer
Script que verifica a integridade da imagem, renomeia a imagem e a move para outra pasta

# Como utilizar
1. Reuna as imagens em uma pasta
2. Execute o arquivo ImageRenamer.exe
3. Informe o caminho para a pasta de origem
4. Informe o caminho para a pasta de destino (se não houver, o script irá criar)
5. Informe um numero para ser adicionado ao final do nome da imagem
6. Aguarde o processamento das imagens finalizar
7. Pronto, imagens renomeadas estarão na nova pasta.

# Como funciona
1. Usuario informa o diretório onde as imagens estão alocadas
2. Usuario informa o diretório onde as imagens renomeadas serão alocadas
3. Usuario informa o numero que será adicionado ao final do nome da imagem
4. Script utiliza a biblioteca Pillow para analisar cada imagem e verificar se é um imagem ou se o arquivo está corrompido
5. Imagens com formato de cores CMYK são convertidas para RGB
6. Script separa o nome da extensão, adiciona o numeral e salva o arquivo na pasta de saída
7. A cada imagem processada, o script retorna *"Imagem {arquivo} renomeada e movida para {pasta_destino}"*
8. Após analisar todas as imagens, o script retorna *"Processamento concluído!"*
9. Caso um arquivo esteja corrompido, ou não seja imagem, o script retorna *"Arquivo {arquivo} não é uma imagem válida ou está corrompido."*

# Exemplo
1. 1º Caminho: C:\Users\usuario\Desktop\Images
2. 2º Caminho: C:\Users\usuario\Desktop\ImagesNomeadas
3. Numero: 42
4. Imagem original: Fotocomamigos.jpeg
5. Imagem de saida: Fotocomamigos42.jpeg
