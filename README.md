XML for DANFE 📄

📋 Visão Geral:

Este projeto é uma ferramenta web robusta projetada para automatizar a conversão de arquivos XML de Notas Fiscais Eletrônicas (NF-e) em seus respectivos Documentos Auxiliares (DANFE) em formato PDF.

O foco principal é a eficiência operacional e a experiência do usuário, permitindo que contadores e departamentos fiscais processem volumes significativos de documentos sem a necessidade de softwares complexos ou instalações locais pesadas.

✨ Funcionalidades Principais:

Upload Flexível: Suporte para arquivos XML individuais ou múltiplos arquivos compactados em formato .zip.
Extração Inteligente: Identificação automática do número da NF-e e da chave de acesso via XPath para nomeação organizada dos arquivos gerados.
Processamento em Memória: A geração dos PDFs ocorre em buffers de memória (io.BytesIO), garantindo velocidade e evitando o acúmulo de arquivos temporários no servidor.  
Interface Intuitiva: Dashboard desenvolvido em Streamlit com feedback visual em tempo real e botões de download direto.

🛠️ Stack Tecnológica e Decisões Arquiteturais:

Linguagem: Python
Interface: Streamlit, escolhido pela agilidade no desenvolvimento de ferramentas de dados.
Geração de Relatórios: brazilfiscalreport, biblioteca especializada no padrão fiscal brasileiro.  
Parsing de XML: lxml, utilizada pela sua alta performance em processamento de grandes estruturas XML.
Gerenciamento de Ambiente: uv. Optei pelo uv por ser o gerenciador de pacotes mais rápido do ecossistema Python atual, garantindo builds determinísticos via uv.lock.
Containerização: Docker, garantindo que a aplicação rode de forma idêntica em qualquer ambiente (dev/prod), com otimização de camadas para redução de peso da imagem.

🚀 Como Executar o Projeto:

Pré-requisitos:
Possuir o UV instalado ou Docker.

Execução Local (com UV):

# Clone o repositório
git clone https://github.com/seu-usuario/xml-for-danfe.git
cd xml-for-danfe

# Instale as dependências
uv sync

# Rode a aplicação
uv run streamlit run main.py

Execução via Docker:
O projeto conta com um Dockerfile otimizado para produção:

# Build da imagem
docker build -t xml-for-danfe .

# Execução do container
docker run -p 8501:8501 xml-for-danfe
Acesse em: http://localhost:8501

🏗️ Estrutura do Projeto:

main.py: Ponto de entrada da aplicação e lógica da interface Streamlit.
danfegerador.py: Classe encapsulada responsável pela lógica de negócio e geração do PDF.  
pyproject.toml / uv.lock: Definição rigorosa de dependências e versões.
Dockerfile: Configuração de infraestrutura como código para deployment.

Desenvolvido por Alex Varela