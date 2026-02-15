# 💰 FINTrack - CLI de Gestão Financeira Inteligente

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Concluído-success)

> **FINTrack** é uma aplicação de linha de comando (CLI) desenvolvida para automatizar a ingestão, categorização e análise de transações financeiras. O projeto substitui o trabalho manual de planilhas por um fluxo de dados (ETL) robusto e automatizado.

---

## 📸 Demonstração

<img width="600" height="550" alt="Image" src="https://github.com/user-attachments/assets/ace68fad-66a4-47e1-acc0-d8d2b0857dde" />

---

## 🏗️ Arquitetura de Software

Diferente de scripts de automação comuns, o **FINTrack** foi construído seguindo princípios de Engenharia de Software, utilizando uma **Arquitetura em Camadas (Layered Architecture)** para garantir desacoplamento, testabilidade e escalabilidade.

```bash
graph TD
    User((Usuário))
    CLI[Interface CLI (Typer/Rich)]
    Service[Service Layer (Regras de Negócio)]
    Repo[Repository Layer (Acesso a Dados)]
    DB[(SQLite / SQLAlchemy)]
    
    User -->|Comandos| CLI
    CLI -->|Orquestração| Service
    Service -->|Lógica & ETL| Service
    Service -->|Persistência| Repo
    Repo -->|SQL| DB
```

## 🧩 Padrões Utilizados:

- **Repository Pattern:** A camada de acesso a dados (repositories.py) abstrai todas as queries SQL. O restante da aplicação desconhece a existência do banco de dados.
- **Service Pattern:** A camada de serviço (services.py) encapsula as regras de negócio (categorização automática, prevenção de duplicatas, cálculos de saldo).
- **Dependency Injection:** Os repositórios são injetados nos serviços, facilitando a criação de testes unitários.

## ✨ Funcionalidades Principais

- **CLI Profissional:** Interface interativa com cores, tabelas formatadas e barras de progresso (via Typer e Rich).
- **ETL Automatizado:** Processamento de arquivos .csv bancários com Pandas, incluindo limpeza e normalização de dados.
- **Categorização Inteligente:** Sistema de regras baseado em palavras-chave para classificar transações automaticamente (ex: "Uber" -> "Transporte").
- **Idempotência:** O sistema previne duplicidade. Você pode importar o mesmo arquivo 10 vezes; as transações já existentes serão ignoradas.
- **Relatórios Dinâmicos:**
    - Extrato detalhado com formatação condicional (Verde/Vermelho).
    - Agrupamento de gastos por categoria.
    - Cálculo automático de balanço e saldo.
- **Automação Web (RPA):** Módulo demonstrativo (automation.py) utilizando PyAutoGUI para simular a navegação e download de extratos em sites bancários.

## 🛠️ Tech Stack

- **Linguagem:** Python 3.13+
- **Interface (CLI):** Typer & Rich
- **Banco de Dados (ORM):** SQLAlchemy
- **Processamento de Dados:** Pandas
- **Automação (RPA):** PyAutoGUI
- **Testes:** Pytest

## 🚀 Instalação e Configuração
Siga os passos abaixo para rodar o projeto localmente.

1. **Clone o Repositório**
```bash
git clone https://github.com/EnioJr18/FINTrack.git
cd fintrack
```

2. **Crie e ative o ambiente virtual**
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Inicialize o banco de dados**
```bash
python main.py setup
```

## 💻 Como Usar

O FINTrack funciona através de comandos no terminal.

📥1. **Importar Extrato**
Importe um arquivo CSV. O sistema irá ler, verificar duplicatas e categorizar automaticamente.
```bash
python main.py importar extrato_exemplo.csv
```
📊2. **Ver Extrato Geral**
```bash
python main.py extrato
```
📈3. **Analisar Por Categoria**
```bash
python main.py categorias
```

## 🧪 Testes Automatizados

O projeto inclui testes unitários para garantir a integridade das regras financeiras (cálculo de saldo, receitas e despesas) sem impactar o banco de dados real (usando SQLite in-memory).

Para rodar os testes:
```bash
pytest
```

## 📂 Estrutura do Projeto
```bash
/fintrack
│
├── main.py              # Entry Point: Interface CLI e Comandos
├── services.py          # Camada de Serviço (Regras de Negócio)
├── repositories.py      # Camada de Repositório (Queries SQL)
├── models.py            # Modelos do Banco de Dados (ORM)
├── database.py          # Configuração da Conexão DB
├── settings.py          # Configurações e Mapa de Categorias
├── automation.py        # Script de Automação RPA (Demo)
│
├── tests/               # Testes Unitários
│   └── test_financeiro.py
│
├── extrato_exemplo.csv  # Arquivo para teste
└── requirements.txt     # Dependências do projeto
```


## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
Desenvolvido por **Enio Jr** para fins de estudo de Backend e portfólio 💻.

📧 Entre em contato: eniojr100@gmail.com <br>
🔗 LinkedIn: https://www.linkedin.com/in/enioeduardojr/ <br>
📷 Instagram: https://www.instagram.com/enio_juniorrr/ <br>
