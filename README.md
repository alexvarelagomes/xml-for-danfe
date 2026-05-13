XML for DANFE

Visão Geral:

Este projeto é uma aplicação web desenvolvida para simplificar e automatizar a geração do Documento Auxiliar da Nota Fiscal Eletrônica (DANFE) em formato PDF a partir de arquivos XML de Notas Fiscais Eletrônicas (NF-e). A ferramenta oferece uma interface amigável onde o usuário pode fazer o upload de um ou múltiplos arquivos XML e obter os DANFEs correspondentes de forma rápida e eficiente.

Objetivo Principal:

Facilitar a vida de usuários que precisam visualizar ou imprimir DANFEs, eliminando a necessidade de softwares complexos ou processos manuais. A aplicação é especialmente útil para departamentos fiscais, contadores ou qualquer profissional que lide com um grande volume de notas fiscais.

Tecnologias e Ferramentas Utilizadas:

Python 3.13
UV – Gerenciador e instalador de pacotes
Docker – Gerenciar aplicação garantindo que funcionem exatamente igual em qualquer ambiente
pyproject.toml – Gerenciamento de dependências

Como Rodar o Projeto:

# Instalar dependências
uv install

# Rodar a aplicação
python main.py