import requests
import sys
import time

if len(sys.argv) != 3:
    print("Uso: python3 fuzzer.py <URL_ALVO> <WORDLIST_ARQUIVO>")
    print("Exemplo: python3 fuzzer.py https://meualvo.com wordlist.txt")
    sys.exit()

url_base = sys.argv[1]
wordlist_file = sys.argv[2]

print(f"Utilizando {url_base} como URL e {wordlist_file} como a wordlist:")

try:
    with open(wordlist_file, 'r') as arquivo:
        for linha in arquivo:

            caminho = linha.strip()
            url_completa = url_base.rstrip('/') + '/' + caminho

            try:
                requisicao = requests.get(url_completa)
                if requisicao.status_code == 200:
                    print(f"[Descoberto] {url_completa}")
                time.sleep(0.01)

            except requests.exceptions.ConnectionError:

                print(f"[Erro] Não foi possível se conectar a {url_base}")
                sys.exit(1)

except FileNotFoundError:

    print("Erro em encontrar o arquivo 'wordlist.txt'")
    sys.exit(1)

print("Scan finalizado!")