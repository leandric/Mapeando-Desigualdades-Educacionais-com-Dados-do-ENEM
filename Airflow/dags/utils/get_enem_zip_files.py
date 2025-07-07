import requests
from bs4 import BeautifulSoup
import re
import os

def baixar_microdados_enem(ano: int, pasta_destino: str = "data/raw", **kwargs) -> str:
    """
    Baixa o arquivo .zip de microdados do ENEM disponível no site do INEP para o ano especificado.

    Parâmetros:
    - ano (int): Ano desejado (ex: 2020)
    - pasta_destino (str): Caminho da pasta onde o arquivo será salvo (default: "data/raw")
    """
    # Cria a pasta de destino se não existir
    os.makedirs(pasta_destino, exist_ok=True)

    # URL da página do INEP
    url = "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem"
    headers = {"User-Agent": "Mozilla/5.0"}

    print(f"🔎 Acessando a página do INEP...")
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Faz o parsing do HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Coleta todos os links e busca o ano exato
    links = soup.find_all("a", href=True)
    link_encontrado = None

    for link in links:
        href = link['href']
        match = re.search(rf"microdados_enem_{ano}\.zip", href)
        if match:
            if not href.startswith("http"):
                href = "https://www.gov.br" + href
            if "download.inep.gov.br" in href and not href.startswith("http"):
                href = "https://" + href
            link_encontrado = href
            break

    if not link_encontrado:
        print(f"❌ Nenhum arquivo encontrado para o ano {ano}.")
        return

    # Baixa o arquivo
    nome_arquivo = os.path.join(pasta_destino, f"microdados_enem_{ano}.zip")
    print(f"⬇ Baixando {ano} de {link_encontrado}")
    with requests.get(link_encontrado, stream=True) as r:
        r.raise_for_status()
        with open(nome_arquivo, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"✔ Arquivo {ano} salvo em {nome_arquivo}\n")



if __name__ == '__main__':
    pass
