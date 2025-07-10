import secrets
import string

def gerar_hash_aleatorio(tamanho=24):
    caracteres = string.ascii_letters + string.digits
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))

# Exemplo de uso
hash_aleatorio = gerar_hash_aleatorio()
print(f'Hash gerado: {hash_aleatorio}')
