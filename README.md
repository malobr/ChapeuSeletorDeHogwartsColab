
# Hogwarts: Chapéu Seletor e Clube de Duelos

> **Curso:** Lógica de Programação Senac – Python
> **Desenvolvedor:** Marcelo Tomás Cavalheiro

Este projeto é um sistema interativo desenvolvido em Python (otimizado para o Google Colab) que simula a experiência de um aluno recém-chegado a Hogwarts. O sistema realiza uma triagem interativa (Quiz) para definir a Casa do usuário e permite a interação na Sala Comunal, culminando em um sistema de duelos por turnos.



## Objetivo do Sistema

Definir uma Casa (Grifinória, Sonserina, Corvinal ou Lufa-Lufa) para o usuário recém-cadastrado através de um quiz de personalidade. Após a seleção, o aluno recebe acesso à sua respectiva Sala Comunal, onde pode visualizar colegas de casa e participar de duelos de feitiços contra adversários controlados pelo sistema (PC) ou simulados.

## Funcionalidades Principais

* **Cadastro e Triagem:** Registro de novos alunos e definição automática da Casa com base em um sistema de pontuação (Quiz).
* **Controle de Acesso (Sala Comunal):** Autenticação simples via ID/Matrícula e senha específica da Casa.
* **Clube de Duelos:** Sistema de combate em turnos (Jogador vs PC) utilizando uma seleção de feitiços clássicos.
* **Painel de Informações:** Consulta de dados do próprio aluno e listagem de outros usuários pertencentes à mesma Casa.



## Estrutura do Menu

O sistema é guiado por um menu principal em loop contínuo:

1. **Cadastrar novo Aluno** (Inicia o Quiz do Chapéu Seletor)
2. **Sala Comunal**
* *Requer Matrícula e Senha da Casa*
* Submenu da Sala:
1. Ver Minhas Informações
2. Duelar (Estupefaça, Expelliarmus, Petrificus Totalus, Confundo)
3. Ver Colegas da Casa
4. Voltar aos Corredores de Hogwarts




3. **Cadastrar Professor** *(Em desenvolvimento)*
4. **Área do Professor** *(Em desenvolvimento)*
5. **Sair** (Opção `0` para encerrar o loop)



## Estrutura de Dados

Como o projeto foi adaptado para rodar no Google Colab de forma procedimental, a persistência em memória é feita utilizando Listas e Dicionários (Arrays) em vez de Objetos/Classes.

* **Lista de Alunos Cadastrados:** Armazena `Matricula`, `Nome`, `Idade`, `Sexo`, `Status do Sangue` e `ID da Casa`.
* **Casas de Hogwarts:** Armazena `Nome`, `Senha`, `Fundador` e `Arte`.
* **Feitiços:** Armazena `Nome`, `Descrição`, `Dano Mínimo` e `Dano Máximo`.



## Mapeamento de Funções

Abaixo estão as principais funções implementadas para modularizar a lógica do sistema, atendendo aos requisitos de diversidade de retornos e parâmetros:

| Nome da Função | Descrição | Parâmetros? | Retorno? |
| --- | --- | --- | --- |
| `sistema()` | Gerencia o Loop `while` principal e renderiza o menu de opções. | Não | Não |
| `cadastrarAluno()` | Executa o quiz, contabiliza as respostas e cadastra o aluno na Casa vencedora. | Não | Não |
| `salaComunal()` | Valida a entrada do usuário e abre o submenu interativo da casa. | Não | Não |
| `iniciarDuelo()` | Controla o loop de combate por turnos (HP, dano aleatório e seleção de feitiços). | Sim | Sim |
| `computarPonto()` | Centraliza a lógica de pontuação do quiz para evitar repetição de código nas perguntas. | Sim | Não |

### Requisitos de Funções Contemplados

* [x] Função com parâmetro e com retorno (`iniciarDuelo`)
* [x] Função com parâmetro e sem retorno (`computarPonto`)
* [x] Função sem parâmetro e com retorno *(a ser definida/utilizada nas validações)*
* [x] Função sem parâmetro e sem retorno (`sistema`, `cadastrarAluno`, `salaComunal`)



## Lógica e Regras de Negócio

1. **Navegação (Loop Principal):** O sistema roda sobre um laço `while (opcao != 0)`. Cada escolha do usuário invoca a função correspondente.
2. **Sistema de Pontuação (Triagem):** Durante o `cadastrarAluno()`, variáveis inteiras representando as casas iniciam em `0`. A função `computarPonto(resposta)` é chamada a cada pergunta do quiz para somar `+1` na casa correspondente à resposta.
* *Desempate:* O quiz possui um número ímpar de perguntas. Utiliza-se a função nativa `max()` do Python. Em caso de distribuição como (2, 2, 1), a função pega a primeira casa a atingir a pontuação máxima, garantindo que não haja empates impeditivos.


3. **Sistema de Duelos:**
A função `iniciarDuelo()` resgata a lista de alunos, filtra por matrículas diferentes da atual para escolher o adversário (PC). O HP (Vida) de ambos é setado em `100`. Um loop `while (hp > 0)` controla os turnos. O jogador escolhe o feitiço pelo menu; se escolher uma opção inválida, perde o turno.
4. **Sala Comunal:**
Atua como uma área restrita. O aluno deve inserir sua matrícula para o sistema identificar seu `casaId`, e em seguida, inserir a senha da casa (revelada no final do cadastro).



## Organização e Desenvolvimento

O escopo inicial previa a modelagem utilizando Orientação a Objetos. No entanto, para garantir compatibilidade e fluidez na execução via **Google Colab**, a arquitetura foi refatorada. A lógica principal foi mantida intacta, mas a manipulação de dados foi transicionada para uma abordagem baseada em Listas e Arrays, garantindo um código leve, funcional e focado na aplicação direta da lógica de programação em Python.
