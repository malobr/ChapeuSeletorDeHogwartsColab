import random # Adicionado para a função iniciarDuelo
from IPython.display import clear_output # Adicionando para o Limpa Tela...


alunosCadastrados = [# Adicionando alguns alunos ja cadastrados para Melhor visualizacao do sistema
    {
        "matricula": 1,
        "nome": "Harry Potter",
        "idade": 11,
        "sexo": "Masculino",
        "statusSangue": "Mestiço",
        "casaId": "Grifinoria"
    },
    {
        "matricula": 2,
        "nome": "Hermione Granger",
        "idade": 11,
        "sexo": "Feminino",
        "statusSangue": "Nascida Trouxa",
        "casaId": "Grifinoria"
    },
    {
        "matricula": 3,
        "nome": "Ron Weasley",
        "idade": 11,
        "sexo": "Masculino",
        "statusSangue": "Puro",
        "casaId": "Grifinoria"
    },
    {
        "matricula": 4,
        "nome": "Draco Malfoy",
        "idade": 11,
        "sexo": "Masculino",
        "statusSangue": "Puro",
        "casaId": "Sonserina"
    },
    {
        "matricula": 5,
        "nome": "Pansy Parkinson",
        "idade": 11,
        "sexo": "Feminino",
        "statusSangue": "Puro",
        "casaId": "Sonserina"
    },
    {
        "matricula": 6,
        "nome": "Luna Lovegood",
        "idade": 11,
        "sexo": "Feminino",
        "statusSangue": "Puro",
        "casaId": "Corvinal"
    },
    {
        "matricula": 7,
        "nome": "Cho Chang",
        "idade": 12,
        "sexo": "Feminino",
        "statusSangue": "Mestiço",
        "casaId": "Corvinal"
    },
    {
        "matricula": 8,
        "nome": "Cedrico Diggory",
        "idade": 15,
        "sexo": "Masculino",
        "statusSangue": "Puro",
        "casaId": "Lufalufa"
    },
    {
        "matricula": 9,
        "nome": "Susana Bones",
        "idade": 11,
        "sexo": "Feminino",
        "statusSangue": "Mestiço",
        "casaId": "Lufalufa"
    },
    {
        "matricula": 10,
        "nome": "Neville Longbottom",
        "idade": 11,
        "sexo": "Masculino",
        "statusSangue": "Puro",
        "casaId": "Grifinoria"
    }
]

CASAS = {#Pre-definindo as casas e suas caracteristicas
    "Grifinoria": {
        "nome": "Grifinória",
        "senha": "Caput Draconis",
        "fundador": "Godric Gryffindor",
        "arte": "                  \n"
                "───▄▀▀▀▀▀───▄█▀▀▀█▄\n"
                "──▐▄▄▄▄▄▄▄▄██▌▀▄▀▐██\n"
                "──▐▒▒▒▒▒▒▒▒███▌▀▐███\n"
                "───▌▒▓▒▒▒▒▓▒██▌▀▐██\n"
                "────▌▓▐▀▀▀▀▌▓─▀▀"
    },
    "Sonserina": {
        "nome": "Sonserina",
        "senha": "Sangue Puro",
        "fundador": "Salazar Slytherin",
        "arte":  "                  \n"
                 "▄▄▀█▄───▄───────▄\n"
                 "▀▀▀██──███─────███\n"
                 "░▄██▀░█████░░░█████░░\n"
                 "███▀▄███░███░███░███░▄\n"
                 "▀█████▀░░░▀███▀░░░▀██▀\n"
    },
    "Corvinal": {
        "nome": "Corvinal",
        "senha": "Sabedoria",
        "fundador": "Rowena Ravenclaw",
        "arte":   "         __\n"
                  "        /'{>\n"
                  "    ____) (____\n"
                  "  //'--;   ;--'\\\\\n"
                  " ///////\\_/\\\\\\\\\\\\\n"
                  "        m m"
              },
    "Lufalufa": {
        "nome": "Lufa-Lufa",
        "senha": "Lealdade",
        "fundador": "Helga Hufflepuff",
        "arte": "                  \n"
                "    (`-()_.-=-. \n"
                "    /00  ,     , \\  \n"
                "   =(o_/= //_  (  /======`  \n"
                "     n`` n`  nn` \n"
    }
}

# Adicionado para a função iniciarDuelo
FEITICOS = [
    {"nome": "Estupefaça", "descricao": "Atordoa o oponente", "danoMin": 10, "danoMax": 20},
    {"nome": "Expelliarmus", "descricao": "Desarma o oponente", "danoMin": 15, "danoMax": 25},
    {"nome": "Petrificus Totalus", "descricao": "Petrifica temporariamente", "danoMin": 5, "danoMax": 15},
    {"nome": "Confundo", "descricao": "Confunde o oponente", "danoMin": 8, "danoMax": 18}
]

# --- FUNÇÕES DO SISTEMA ---

def chapeuSeletorArte():
    print("")
    print("--──────--▄▀▀▄")
    print("---──────▄▀▄░▀▄")
    print("--──────▄▀▄░░░░▀▄")
    print("--──────▄▀▄░░░░░░▀▄")
    print("--─────▄█░░░░░░░░░█▄")
    print("--─▄▄──█░░░░░░░░░░░█──▄▄")
    print("--█▄▄██░░▀░░░░░░░░▀░░██▄▄█")
    print("-- Chapéu Seletor de Hogwarts --\n")

def cadastrarAluno():
    grifinoria = 0
    sonserina = 0
    corvinal = 0
    lufalufa = 0

    print("\nHmmm, interessante... Me diga mais sobre voce.\nBem-vindo ao Chapéu Seletor de Hogwarts!")

    nome = input("\nInforme seu nome:\n")

    try:
        idade = int(input("\nInforme sua idade:\n"))
    except ValueError:
        print("\nErro: Idade deve ser um número inteiro.")
        return

    sexo = input("\nInforme seu sexo:\n")
    statusSangue = input("\nInforme seu Status de Sangue (Puro, Mestico ou Trouxa):\n")

    numeroMatricula = len(alunosCadastrados) + 1#Criando matricula do aluno, adicionando + 1 no numero de alunos ja cadastrados..

    print("\nResponda às seguintes perguntas para descobrir sua casa.")

    def computarPonto(resposta):# Criando uma funcao para nao ter que repetir a logica em cada pergunta... Porem As respostas ficam fixas em cada opcao\numero..
        nonlocal grifinoria, sonserina, corvinal, lufalufa
        if resposta == 1:
            grifinoria += 1
        elif resposta == 2:
            sonserina += 1
        elif resposta == 3:
            corvinal += 1
        elif resposta == 4:
            lufalufa += 1
        else:
            print("Resposta inválida!")

    # Pergunta 1
    #print(f"\n" + "-=-" * 25)
    print("Pergunta 1: Qual dessas qualidades você mais valoriza?")
    print("\n1. Coragem\n2. Ambição\n3. Inteligência\n4. Lealdade")
    computarPonto(int(input("\nDigite o número da sua resposta: ")))

    # Pergunta 2
    print("\nPergunta 2: Qual dessas criaturas mágicas você prefere?")
    print("\n1. Fênix\n2. Serpente\n3. Coruja\n4. Texugo")
    computarPonto(int(input("\nDigite o número da sua resposta: ")))

    # Pergunta 3
    print("\nPergunta 3: Qual dessas matérias você mais gosta?")
    print("\n1. Defesa Contra as Artes das Trevas\n2. Poções\n3. Feitiços\n4. Herbologia")
    computarPonto(int(input("\nDigite o número da sua resposta: ")))

    # Pergunta 4
    print("\nPergunta 4: Qual desses lugares você preferiria explorar?")
    print("\n1. A Floresta Proibida\n2. As Masmorras\n3. A Torre da Corvinal\n4. A cozinha dos elfos domésticos")
    computarPonto(int(input("\nDigite o número da sua resposta: ")))

    # Pergunta 5
    print("\nPergunta 5: Qual dessas palavras melhor descreve você?")
    print("\n1. Destemido\n2. Astuto\n3. Sábio\n4. Trabalhador")
    computarPonto(int(input("\nDigite o número da sua resposta: ")))
    print(f"\n-=-" * 25)

    pontuacoes = {
        "Grifinoria": grifinoria,
        "Sonserina": sonserina,
        "Corvinal": corvinal,
        "Lufalufa": lufalufa
    }

    # Descobre a chave do dicionário com a maior pontuação
    nomeCasa = max(pontuacoes, key=pontuacoes.get)
    dadosDaCasa = CASAS[nomeCasa]

    clear_output()
    print(f"\nO Chapéu Seletor grita: {dadosDaCasa['nome'].upper()}!")

    novoAluno = {
        "matricula": numeroMatricula,
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
        "statusSangue": statusSangue,
        "casaId": nomeCasa # Salvamos apenas a chave do dicionário
    }

    alunosCadastrados.append(novoAluno)

    print(f"\nAluno {nome} cadastrado com sucesso! Sua matrícula é: {numeroMatricula:06}")
    print("-" * 40)
    print(dadosDaCasa['arte'])
    print(f"\nBem-vindo à {dadosDaCasa['nome']}!")
    print(f"A senha da sua Sala Comunal é: ** {dadosDaCasa['senha']} **")
    print("-" * 40)

def iniciarDuelo(jogador):
    print("\n" + "="*40)
    print("X - CLUBE DE DUELOS - X")
    print("="*40)

    # Criamos uma lista de oponentes possiveis, pegando os alunos cadastrados, (menos nos mesmos \ a matricula que entrou na sala comunal)
    oponentesPossiveis = [a for a in alunosCadastrados if a["matricula"] != jogador["matricula"]]

    if not oponentesPossiveis:
        print("A arena está vazia... Não há outros alunos cadastrados para duelar!")
        return

    # Sorteia um oponente aleatorio da lista de oponentes possiveis e adiciona ele a oponente...
    oponente = random.choice(oponentesPossiveis)
    casaOponente = CASAS[oponente['casaId']]['nome']

    print(f"\nSeu oponente entra na arena: {oponente['nome']} da {casaOponente}!")

    # Iniciando o hp para o duelo..
    hpJogador = 100
    hpOponente = 100

    # Loop da batalha: continua enquanto ambos estiverem com vida acima de 0
    while hpJogador > 0 and hpOponente > 0:
        print(f"\nSeu HP: {hpJogador} | HP de {oponente['nome']}: {hpOponente}")
        print("-" * 40)
        print("Escolha seu feitiço:")

        for i, feitico in enumerate(FEITICOS):#listando os feiticos disponiveis
            print(f"{i+1} - {feitico['nome']} ({feitico['descricao']})")

        escolha = input("\nDigite o número do feitiço: ")

        try:# Se escolhermos dentro das opcoes mostradas ok
            indice = int(escolha) - 1
            feiticoEscolhido = FEITICOS[indice]
        except (ValueError, IndexError):# se digitarmos algo diferente das opcoes disponiveis(1, 2, 3, 4), perde o turno...
            print("\nVocê gaguejou o feitiço! O feitiço falhou e você perdeu o turno.")
            feiticoEscolhido = None

        # --- Nossa Jogada---
        if feiticoEscolhido:# randint vai rerar numeros inteiros aleatorios
            dano = random.randint(feiticoEscolhido["danoMin"], feiticoEscolhido["danoMax"])#Sorteia um valor aleatorio entre o dano minimo e maximo e adiciona o valor em (dano)
            hpOponente -= dano# Removemos o valor do dano do feitico da vida do oponente
            print(f"\n-> Você lançou {feiticoEscolhido['nome']}! Causou {dano} de dano em {oponente['nome']}!")

        if hpOponente <= 0:
            print(f"\nVITÓRIA! Você derrotou {oponente['nome']}!")
            print(f"10 pontos para a {CASAS[jogador['casaId']]['nome']}!")
            return hpOponente #Retornamos o Hp do Oponente assim ja encerrando a funcao do duelo..
            

        # --- Jogada pc - (BOT) ---
        feiticoOponente = random.choice(FEITICOS)# Escolhe um feitico aleatorio da lista de feiticos..
        danoOponente = random.randint(feiticoOponente["danoMin"], feiticoOponente["danoMax"])# Sorteia um valor aleatorio entre o dano minimo e maximo e adiciona o valor em (dano)
        hpJogador -= danoOponente# Removemod o valor do dano do feitico de nossa vida..

        print(f"{oponente['nome']} contra-atacou com {feiticoOponente['nome']}! Você sofreu {danoOponente} de dano!")

        if hpJogador <= 0:
            print(f"\nDERROTA! Você foi nocauteado por {oponente['nome']}... Vá para a Enfermaria!")
            return hpJogador #Retornamos o Hp do Jogador assim ja encerrando a funcao do duelo..
            


def salaComunal():
    print(f"\n----- Entrada da Sala Comunal -----\n")

    try:
        matriculaDigitada = int(input("Informe a sua matrícula:\n"))
    except ValueError:
        print("Matrícula inválida! Digite apenas números.")
        return

    alunoEncontrado = None
    for aluno in alunosCadastrados:
        if aluno["matricula"] == matriculaDigitada:
            alunoEncontrado = aluno
            break

    if alunoEncontrado != None:
        # Puxa os dados da casa usando a chave salva no aluno
        idCasa = alunoEncontrado["casaId"]
        casaDoAluno = CASAS[idCasa]

        print(f"\nVoce esta diante da porta da Sala Comunal de {casaDoAluno['nome']}!")
        print(casaDoAluno['arte'])
        senhaDigitada = input("\nInforme a senha da Sala Comunal:\n")

        if senhaDigitada == casaDoAluno['senha']:
                print("\n" + "="*40)
                print("A passagem se abre...")
                print("="*40)
                print(casaDoAluno['arte'])
                print(f"\nBem-vindo(a) de volta à {casaDoAluno['nome']}, {alunoEncontrado['nome']}!")

                # --- MENU INTERNO DA SALA COMUNAL ---
                while True:
                    print("\n1 - Ver minhas informações")
                    print("2 - Duelar")
                    print(f"3 - Ver colegas da {casaDoAluno['nome']}")
                    print("0 - Voltar aos corredores de Hogwarts")

                    opcaoSala = input(f"\nO que deseja fazer? ")

                    # Dentro da função salaComunal()...
                    if opcaoSala == "1":
                        print(f"\nNome: {alunoEncontrado['nome']}")
                        print(f"Idade: {alunoEncontrado['idade']}")
                        print(f"Sangue: {alunoEncontrado['statusSangue']}")
                        print(f"Casa: {casaDoAluno['nome']}")
                        print(f"Fundador: {casaDoAluno['fundador']}")
                    elif opcaoSala == "2":
                        # Chamamos a função passando o dicionário do aluno que está logado
                        iniciarDuelo(alunoEncontrado)
                    elif opcaoSala == "3":
                        # NOVA LÓGICA DE LISTAGEM DE ALUNOS
                        print(f"\n--- Alunos da {casaDoAluno['nome']} ---")
                        for aluno in alunosCadastrados:
                            if aluno["casaId"] == idCasa:
                                print(f"- {aluno['nome']} (Matrícula: {aluno['matricula']:03})")
                        print("-" * 40)
                    elif opcaoSala == "0":
                        break
                    else:
                        print("\nOpção inválida! Tente novamente.")
        else:
            print("\nSenha incorreta! A entrada permanece fechada.")
    else:
        print("\nMatrícula não encontrada. O Chapéu Seletor não lembra de você!")

def areaDoProfessor():#A parte dos Professores quero adicionar no poo, nao deu tempo aqui...
    print("\n[Aviso] Área do Professor ainda em desenvolvimento!")

def cadastrarProfessor():
    print("\n[Aviso] Cadastro de Professor ainda em desenvolvimento!")

#Loop do sisteam, chamando as funcoes...
def sistema():
    while True:
        chapeuSeletorArte()
        print("1 - Cadastrar Novo Aluno")
        print("2 - Sala Comunal")
        print("3 - Cadastrar Professor")
        print("4 - Area do Professor")
        print("0 - Sair")

        opcao = input("\nDigite uma opção: ")
        clear_output()

        if opcao == "1":
            cadastrarAluno()
        elif opcao == "2":
            salaComunal()
        elif opcao == "3":
            cadastrarProfessor()
        elif opcao == "4":
            areaDoProfessor()
        elif opcao == "0":
            print("\nMalfeito feito. Saindo do sistema...")
            print(f"O projeto original era feito em Python Poo, \nEsse e uma parte reaproveitada da logica, utilizando arraiz e matrizes para quardad os dados...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

# Executa o sistema
sistema()
