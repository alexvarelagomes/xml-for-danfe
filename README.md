# XML for DANFE

**Aplicação em Produção**: [Acesse o Gerador DANFE](https://xml-for-danfe.streamlit.app/)

## Visão Geral
Este projeto é uma ferramenta web projetada para automatizar a conversão de arquivos XML de Notas Fiscais Eletrônicas (NF-e) em seus respectivos Documentos Auxiliares (DANFE) em formato PDF.

O foco principal é a **eficiência operacional** e a **experiência do usuário**, permitindo que contadores e departamentos fiscais processem volumes significativos de documentos sem a necessidade de softwares complexos ou instalações locais pesadas.

---

## Funcionalidades Principais
* **Upload Flexível**: Suporte para arquivos XML individuais ou múltiplos arquivos compactados em formato `.zip`.
* **Extração Inteligente**: Identificação automática do número da NF-e e da chave de acesso via XPath para nomeação organizada dos arquivos gerados.
* **Processamento em Memória**: A geração dos PDFs ocorre em buffers de memória (`io.BytesIO`), garantindo velocidade e evitando o acúmulo de arquivos temporários no servidor.  
* **Interface Intuitiva**: Dashboard desenvolvido em Streamlit com feedback visual em tempo real e botões de download direto.

---

## Stack Tecnológica e Decisões Arquiteturais
* **Linguagem**: Python 3.13
* **Interface**: **Streamlit**, escolhido pela agilidade no desenvolvimento de ferramentas de dados.
* **Geração de Relatórios**: **brazilfiscalreport**, biblioteca especializada no padrão fiscal brasileiro.  
* **Parsing de XML**: **lxml**, utilizada pela sua alta performance em processamento de grandes estruturas XML.
* **Gerenciamento de Ambiente**: **uv**. Optei pelo `uv` por ser o gerenciador de pacotes mais rápido do ecossistema Python atual, garantindo builds determinísticos via `uv.lock`.
* **Containerização**: **Docker**, garantindo que a aplicação rode de forma idêntica em qualquer ambiente com otimização de camadas para redução de peso da imagem.
* **Automação e CI/CD**: **GitHub Actions**, configurado para executar a rotina automatizada de monitoramento e preventiva de hibernação.
* **Automação de Navegador**: **Playwright**, utilizado em modo *headless* para simular interação humana legítima e garantir a disponibilidade do ambiente de produção.

---

## Como Executar o Projeto

### Pré-requisitos
* Possuir o **[uv](https://github.com/astral-sh/uv)** ou **[Docker](https://www.docker.com/)** instalados.

### Execução Local (com uv)
```bash
# Clone o repositório
git clone https://github.com/alexvarelagomes/xml-for-danfe.git
cd xml-for-danfe

# Instale as dependências
uv sync

# Rode a aplicação
uv run streamlit run main.py
```

### Execução via Docker
```bash
# Cria a imagem
docker build -t xml-for-danfe .

# Inicia o container
docker run -p 8501:8501 xml-for-danfe
```

> **Acesso**: Abra `http://localhost:8501` no seu navegador.

--- 

## Estrutura do Projeto

* **main.py**: Entrada da aplicação e lógica da interface UI.
* **danfegerador.py**: Lógica de negócio e motor de geração do PDF.
* **extrairxml.py**: Leitura do XML de Nota Fiscal Eletrônica (NF-e) para extrair o número da NF-e e a chave de acesso.
* **pyproject.toml** / **uv.lock**: Gestão rigorosa de dependências.
* **Dockerfile**: Configuração de infraestrutura para deploy.
* **.github/workflows/keep_alive.yml**: Pipeline de CI/CD que gerencia o agendamento (cron job) do robô de reativação.
* **keep_alive.py**: Script de automação utilizando Playwright para contornar a hibernação do Streamlit Cloud.

--- 

## Sustentação e Disponibilidade

Para contornar a hibernação por inatividade do Streamlit Community Cloud, o projeto conta com um robô de monitoramento. A cada 12 horas, um workflow do GitHub Actions é disparado, executando o script `keep_alive.py`. Este script utiliza o Playwright para simular um acesso real à aplicação, identificando se o container está ativo ou se necessita do gatilho manual de restauração, garantindo total disponibilidade para a ferramenta.