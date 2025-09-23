Gerador de DANFE a partir de XML:

📜 Visão Geral:

Este projeto é uma aplicação web desenvolvida para simplificar e automatizar a geração do Documento Auxiliar da Nota Fiscal Eletrônica (DANFE) em formato PDF a partir de arquivos XML de Notas Fiscais Eletrônicas (NF-e). A ferramenta oferece uma interface amigável onde o usuário pode fazer o upload de um ou múltiplos arquivos XML e obter os DANFEs correspondentes de forma rápida e eficiente.

O objetivo principal é facilitar a vida de usuários que precisam visualizar ou imprimir DANFEs, eliminando a necessidade de softwares complexos ou processos manuais. A aplicação é especialmente útil para departamentos fiscais, contadores ou qualquer profissional que lide com um grande volume de notas fiscais.

✨ Funcionalidades Principais:

Geração a partir de um único XML: O usuário pode carregar um único arquivo .xml e obter o DANFE em PDF instantaneamente.

Processamento em Lote via ZIP: É possível carregar um arquivo .zip contendo múltiplos arquivos XML.   O sistema processa todos eles e disponibiliza um único arquivo .zip para download com todos os DANFEs gerados.

Interface Intuitiva: A interface foi construída com o Streamlit, proporcionando uma experiência de usuário limpa e direta.

Nomeação Automática: Os arquivos PDF gerados são nomeados utilizando o número da nota fiscal extraído do próprio XML, facilitando a organização.

Containerização com Docker: O projeto está totalmente containerizado, permitindo que a aplicação seja executada em qualquer ambiente de forma consistente e sem a necessidade de instalar as dependências manualmente.

🛠️ Tecnologias e Bibliotecas Utilizadas:

A aplicação foi construída utilizando Python e um ecossistema de bibliotecas para garantir eficiência e robustez.

Bibliotecas e suas	Finalidades:  
Streamlit -	Framework principal para a construção da interface web interativa;  
BrazilFiscalReport - Biblioteca especializada na geração de DANFEs em PDF a partir de dados de XML fiscal;  
lxml -	Utilizada para o parsing eficiente do XML, permitindo a extração de dados como o número e a chave da NF-e;  
Pandas e NumPy - Dependências da biblioteca BrazilFiscalReport, utilizadas para a manipulação de dados em memória;  
Docker - Ferramenta de containerização utilizada para empacotar a aplicação e suas dependências em uma imagem;  
Docker Compose - Orquestrador para simplificar a execução do container da aplicação.
