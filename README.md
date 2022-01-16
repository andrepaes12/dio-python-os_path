# dio-python-os_path

Objetivo:
Comparar se os arquivos de uma pasta estão em outra pasta.

Contexto da Problemática:
1. Compactar arquivos do diretório Original através de software específico.
2. Este software, após compactar os arquivos, cria um novo diretório (chamado Zip)
3. Os arquivos do diretório Zip possuem o mesmo nome do diretório Original, com adição do sufixo _zip.
    Exemplo: Nome de um arquivo no diretório Original: picture.jpg  => após ser compactado, o arquivo tem o nome
    picture_zip.jpg
4. Para conferir se todos os arquivos da pasta realmente foram compactados, foi desenvolvida a lógica no arquivo listdir.py.

Solução proposta:
1. Utilizar o módulo OS PATH para verificar quais arquivos existentes nas pastas
2. Extrair os nomes dos arquivos de cada pasta e inseri-los em listas (uma para cada diretório).
2.1 Neste caso, diretório Original e diretório Zip
3. Verificar se todos os nomes constantes no diretório Original estão no diretório Zip.
