# FINTrack - Seu Assistente Financeiro Pessoal Automatizado

### FINTrack é um aplicativo de linha de comando construído em Python que automatiza o processo tedioso de baixar, processar e categorizar transações financeiras de extratos bancários. O projeto foi desenvolvido para transformar a tarefa manual de organizar finanças em planilhas em um fluxo de trabalho automatizado e eficiente.

#### 🚀 Demonstração em Ação
Abaixo, um GIF demonstra a capacidade de automação do projeto em um ambiente real, interagindo com a interface de um site para realizar o download do extrato. (Com dados sensíveis devidamente borrados).

#### ✨ Principais Funcionalidades
Banco de Dados Robusto: Utiliza SQLAlchemy e um banco de dados SQLite para persistir todas as transações, categorias e contas de forma estruturada.

* Processamento Inteligente de Extratos: Lê arquivos de extrato no formato .csv usando a biblioteca Pandas para limpar e padronizar os dados.
* Categorização Automática: Implementa um sistema de regras simples para categorizar transações automaticamente com base em palavras-chave encontradas na descrição (ex: "IFOOD" -> "Alimentação").
* Prevenção de Duplicatas: Verifica se uma transação já existe no banco de dados antes de inseri-la, garantindo a integridade dos dados.
* Relatórios por Linha de Comando: Gera relatórios claros e informativos diretamente no terminal, incluindo um extrato geral e um resumo de gastos por categoria.
* Automação de Download (Modo Demo): Inclui um módulo com PyAutoGUI que simula a interação humana com uma página web para automatizar o processo de login e download de extratos.

#### 🛠️ Tecnologias Utilizadas
O projeto foi construído utilizando as seguintes tecnologias:

* Python: Linguagem principal do projeto.
* SQLAlchemy: ORM para interação com o banco de dados e definição dos modelos.
* Pandas: Para leitura e manipulação eficiente dos dados do arquivo CSV.
* PyAutoGUI: Para automação de interface gráfica (GUI), simulando cliques e digitação.
* SQLite: Banco de dados relacional embarcado, ideal para aplicações locais.

#### 📂 Estrutura do Projeto
/fintrack/ <br>
| <br>
|-- main.py             # Ponto de entrada, orquestra os outros módulos <br>
|-- database.py         # Configuração da conexão e sessão do SQLAlchemy <br>
|-- models.py           # Definição das tabelas do banco de dados (ORM) <br>
|-- processing.py       # Lógica para processar o CSV e popular o banco <br>
|-- reports.py          # Funções para gerar relatórios a partir do banco <br>
| <br>
|-- extrato_exemplo.csv # Arquivo de exemplo usado pelo programa <br>
|-- fintrack.db         # Arquivo do banco de dados SQLite (gerado na execução) <br>
|-- requirements.txt    # Lista de dependências do projeto <br>
|-- README.md           # Este arquivo <br>

#### ⚙️ Configuração e Instalação
Siga os passos abaixo para executar o projeto em sua máquina local.

##### 1. Crie o arquivo requirements.txt:
Antes de tudo, se você ainda não tem esse arquivo, gere-o com o seu ambiente virtual ativado:

pip freeze > requirements.txt

##### 2. Clone o Repositório:

git clone https://github.com/EnioJr18/FINTrack.git <br>
cd fintrack

##### 3. Crie e Ative um Ambiente Virtual:

#### Criar o ambiente:
python -m venv venv

#### Ativar no Windows
.\venv\Scripts\activate

#### Ativar no macOS/Linux
source venv/bin/activate

##### 4. Instale as Dependências:

pip install -r requirements.txt

#### ▶️ Como Usar
Com tudo instalado, basta executar o script principal. O programa irá limpar a tela, criar o banco de dados (se não existir), processar o arquivo extrato_exemplo.csv e, finalmente, exibir os relatórios.

python main.py

#### 🛡️ Estratégia de Portfólio: Automação e Segurança
Para demonstrar a funcionalidade de automação sem expor credenciais reais, este projeto adota uma estratégia de Modo de Demonstração.

* O que está no repositório: A automação com PyAutoGUI está configurada para interagir com uma página HTML local (que ainda será criada, como login_demonstracao.html) ou para ser demonstrada através do GIF acima.
* Como funcionaria na vida real: Para uso pessoal, o script seria apontado para o site de um banco real e as credenciais seriam carregadas de forma segura através de variáveis de ambiente, nunca escritas diretamente no código.

Exemplo de como as credenciais seriam lidas de forma segura:

Python
import os

##### As credenciais nunca ficam no código!
usuario = os.getenv('FINTRACK_USER')
senha = os.getenv('FINTRACK_PASSWORD')
Essa abordagem garante a segurança e, ao mesmo tempo, permite demonstrar de forma eficaz uma poderosa capacidade de automação.

#### 📄 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE] para mais detalhes.

#### 👨‍💻 Contato
##### Enio Eduardo Junior

LinkedIn: https://www.linkedin.com/in/enioeduardojr

Email: eniojr100@gmail.com.com

GitHub: https://github.com/EnioJr18

