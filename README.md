#README
## Projeto: Agentes de Criação de Texto para LinkedIn
Este projeto é uma ferramenta automatizada para gerar a seção "Sobre" do LinkedIn a partir de um arquivo PDF de currículo. Utiliza agentes baseados em modelos de linguagem para extrair e compilar informações relevantes, como resumo, habilidades, conquistas e palavras-chave, gerando um texto final para o perfil do LinkedIn.

## Estrutura dos Arquivos
**agents.py**: Define a classe Agent, responsável por carregar os prompts e configurar os agentes que realizam as diferentes tarefas de extração e processamento de informações.

**start.py**: Script principal que configura e executa os agentes definidos em agents.py, carregando o arquivo PDF e utilizando os agentes para gerar o texto final para o LinkedIn.

**read_pdf.py**: Script carrega o currículo em PDF e retorna em forma de string.

**prompts.yml**: Arquivo YAML contendo os templates de prompts utilizados pelos agentes para gerar os diferentes componentes do texto.


## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

## Contato

Para mais informações, entre em contato através de renatosramiro@gmail.com.
