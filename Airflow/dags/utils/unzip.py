import os
import zipfile

def extrair_zips(diretorio_origem, diretorio_destino):
    """
    Extrai todos os arquivos .zip encontrados no diretório de origem
    para o diretório de destino especificado.

    Parâmetros:
    - diretorio_origem: caminho onde estão os arquivos .zip
    - diretorio_destino: caminho onde os arquivos serão extraídos
    """
    # Garante que o diretório de destino existe
    os.makedirs(diretorio_destino, exist_ok=True)

    # Percorre todos os arquivos no diretório de origem
    for nome_arquivo in os.listdir(diretorio_origem):
        if nome_arquivo.endswith('.zip'):
            caminho_zip = os.path.join(diretorio_origem, nome_arquivo)
            print(f'Extraindo: {caminho_zip}')

            with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                zip_ref.extractall(diretorio_destino)

    print('Extração concluída.')