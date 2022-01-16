'''
Contexto:
1. Compactar arquivos do diretório Original através de software específico.
2. Este software, após compactar os arquivos, cria um novo diretório (chamado Zip)
3. Os arquivos do diretório Zip possuem o mesmo nome do diretório Original, com adição do sufixo _zip.
    Exemplo: Nome de um arquivo no diretório Original: picture.jpg  => após ser compactado, o arquivo tem o nome
    picture_zip.jpg
4. Para conferir se todos os arquivos da pasta realmente foram compactados, foi desenvolvida a lógica a seguir.
'''
from os import listdir  #pecorrer os arquivos do diretório
from os.path import isfile, join    #confirmar se é um arquivo

#simulando diretório Original e o diretório Zip
OriginalPath = 'localpath/Original'
ZipPath = 'localpath/Zip'

#ler cada item do diretório e se for um arquivo, adiciona à list[]
OriginalFiles = [f for f in listdir(OriginalPath) if isfile(join(OriginalPath, f))]
ZipFiles = [f for f in listdir(ZipPath) if isfile(join(ZipPath, f))]

#listar o nome dos arquivos (diretório Original) sem a extensão .py
#isto é necessário pois o arquivo compactado tem o nome alterado 
OriginalName = []
for file in OriginalFiles:
    OriginalName.append(file[:-3]) #removendo a extensão .py

#lógica de comparação entre os diretórios (Original X Zip)
filesZip = []
filesNoZip = OriginalName.copy() #Lista p/ identificar arquivos não compactados (cópia da lista Original para fazer 'engenharia reversa')
i = 0
for file in OriginalName:   #para cada arquivo no diretório Original
    for i in range(0, len(zipFiles)):    #percorrer cada arquivo no diretório Zip
        if file == zipFiles[i]:          #se nome do arquivo Original é igual ao nome do arquivo Zip
            filesZip.append(file)    #copiar o nome do arquivo para Lista de Arquivos Compactados (lista Zip)

for file in filesZip:    #para cada arquivo na lista recém criada de Arquivos Copiados
    filesNoZip.remove(file)  #engenharia reversa: remover da lista de não compactados o nome do arquivo que está na lista de compactados

print(f'Original Files: {OriginalFiles}')
print(f'Files copied: {filesZip}')
print(f'Files no copied: {filesNoZip}')
