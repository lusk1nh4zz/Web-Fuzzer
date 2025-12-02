# Web Directory Fuzzer (Content Discovery)

## ⚠️ Aviso Ético e Disclaimer

Esta ferramenta é estritamente para **fins educacionais e de teste de penetração autorizado**. Nunca use este script contra qualquer servidor que não seja de sua propriedade ou para o qual você não tenha permissão explícita por escrito. O uso indevido é ilegal e antiético.

## Visão Geral do Projeto

Este script Python foi desenvolvido para automatizar a **descoberta de conteúdo web** (Content Discovery) em alvos específicos. Ele funciona testando milhares de caminhos de diretório e arquivo fornecidos por uma wordlist, reportando apenas aqueles que retornam o código de status HTTP **200 (OK)**, indicando que o recurso existe.

O projeto é robusto, utilizando **argumentos de linha de comando (CLI)** e tratamento de erros aninhado para lidar com falhas de arquivo e conexões de rede.

---

## Tecnologias e Dependências

* **Linguagem:** Python 3
* **Bibliotecas:**
    * `requests`: Para requisições HTTP e tratamento de exceções de rede.
    * `sys`: Para leitura de argumentos de linha de comando (CLI).
    * `time`: Para implementar um pequeno atraso (rate-limiting) e manter a ética nos testes.
* **Instalação:** Certifique-se de que a biblioteca `requests` está instalada:
    ```bash
    pip install requests
    ```

---

## Uso (CLI - Command Line Interface)

O script requer que a URL alvo e o caminho para o arquivo da wordlist sejam fornecidos como argumentos.

```bash
python3 fuzzer.py <URL_ALVO> <CAMINHO_WORDLIST>