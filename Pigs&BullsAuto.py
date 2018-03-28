import random

cpu = []
jog = []
tentativas = {}

######################################################################################################
#
# list_to_string - recebe o input com a avaliação utilizador e converte para string a
#                  lista que contem o numero gerado atual pelo cpu
#
# Argumentos:
# lista - lista que contem o numero gerado atual pelo cpu
# digitos - variavel com os numeros que ainda podem ser gerados
#
# Retorno:
# Retorna uma lista que contem a avaliação do utilizador e a "lista" em string
#
######################################################################################################


def list_to_string(lista):
    str_c = ''
    resultados = []
    for k in lista:
        str_c += str(k)
    while True:
        output = input("Quantos touros/porcos tem o numero: " + str_c + "? (exemplo: 1T 1P)")
        if verifica_aval(output):
            touro = int(output[0])
            porco = int(output[3])
            break
        else:
            print("insire uma avaliação válida")
    resultados.append(touro)
    resultados.append(porco)
    resultados.append(str_c)
    return resultados


######################################################################################################
#
# verifica_aval - recebe o input do utilizador e verifica se está dentro do aceitável
#
# Argumentos:
# output - input do utilizador
#
# Retorno:
# Retorna true se o input for válido, false caso não seja
#
######################################################################################################


def verifica_aval(output):
    output = output.upper()
    if output == "0T 0P" or output == "1T 0P" or output == "2T 0P" or output == "3T 0P" or output == "4T 0P":
        return True
    elif output == "0T 1P" or output == "0T 2P" or output == "0T 3P" or output == "0T 4P" or output == "1T 1P":
        return True
    elif output == "1T 2P" or output == "1T 3P" or output == "2T 2P" or output == "3T 1P" or output == "2T 1P":
        return True
    else:
        return False

######################################################################################################
#
# permutacao - recebe a lista com o numero gerado pelo cpu e faz todas as permutações desse numero
#
# Argumentos:
# lst - lista com o numero gerado pelo cpu
#
# Retorno:
# Retorna todas as permutações do numero gerado
#
######################################################################################################


def permutacao(lst):
    # Se a lista estiver vazia não existem permutações possiveis
    if len(lst) == 0:
        return []

    # Se existe apenas um elemento na lista, apenas uma permutação é possivel
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []

    # Itera a lista e calcula o nº de permutações
    for i in range(len(lst)):
        m = lst[i]

        # Extrai lst[i] ou o m da lista, remLst é o resto da lista
        remLst = lst[:i] + lst[i + 1:]

        # Gera todas as permutações onde o m é o primeiro elemento
        for p in permutacao(remLst):
            l.append([m] + p)
    return l

######################################################################################################
#
# conta_tent - regista cada tentativa de advinhar feita pelo computador
#
# Argumentos:
# count - numero de tentativas
# touro - numero de touros obtidos neste tentativa
# porco - numero de porcos obtidos neste tentativa
# stri - numero gerado pelo computador nesta tentativa
#
# Retorno:
# Retorna o resultado da avaliação que o número gerado pelo computador obteve
#
######################################################################################################


def conta_tent(count, touro, porco, stri):
    if touro == 4:
        print("Acertou")
        tentativas[count + 1] = stri + ", " + str(touro) + "T"
    elif touro == 0 and porco != 0:
        print("o cpu gerou o numero: " + stri + " e obteve a seguinte avaliação: " + str(porco) + "P")
        tentativas[count + 1] = stri + ", " + str(porco) + "P"
    elif touro != 0 and porco == 0 and touro < 4:
        print("o cpu gerou o numero: " + stri + " e obteve a seguinte avaliação: " + str(touro) + "T")
        tentativas[count + 1] = stri + ", " + str(touro) + "T"
    else:
        print("o cpu gerou o numero: " + stri + " e obteve a seguinte avaliação: " + str(touro) + "T" + " " + str(porco) + "P")
        tentativas[count + 1] = stri + ", " + str(touro) + "T" + " " + str(porco) + "P"

######################################################################################################
#
# gera_numero - recebe o input do utilizador e verifica se está dentro do aceitável e implementa a logica do cpu
#
# Argumentos:
# Não tem
#
# Retorno:
# Retorna acaba o jogo quando o numero que gerou tiver 4 touros
#
####################################################################################################

def gera_numero():
    count = touro = 0
    while touro != 4:
        digitos = set(range(10))
        n = input("Código? ")  # pede um numero a ser advinhado pelo computador
        check_n = verifica_input(n)  # verifica se o input é de facto valido

        if check_n:
            temp_n = str(n)
            jog.clear()
            for i in temp_n:
                k = int(i)
                jog.append(k)  # se o input for valido coloca o numero numa lista

            numero = random.sample(digitos, 4)  #gera um numero de 4 algarismos distintos aleatorios dentro dos numeros disponiveis em "digitos"
            cpu = list(numero)  # transforma o numero gerado numa lista
            for k in cpu:
                digitos -= {k}

            while touro != 4:
                resultados = conta_touros_porcos(cpu, jog)
                str_c = ''
                for k in cpu:
                    str_c += str(k)
                conta_tent(count, resultados[0], resultados[1], str_c)
                touro = resultados[0]
                porco = resultados[1]
                tp = touro + porco

                """
                transforma a lista com o numero atual gerado numa string de forma
                a coloca-lo no dicionário das tentativas
                """
                count += 1
                if (porco >= 1) or ((touro >= 1) and (touro < 3)):  #caso aja porcos no numero gerado vai transforma-los em touros
                    p = []
                    f = []
                    for i in permutacao(cpu):
                        p.append(i)
                    j = 0
                    while j < len(p):
                        resultados = conta_touros_porcos(p[j], jog)
                        str_c = ''
                        for k in cpu:
                            str_c += str(k)
                        conta_tent(count, resultados[0], resultados[1], str_c)
                        if resultados[0] == tp:
                            f.append(p[j])
                        if len(f) == 2:
                            break
                        j += 1
                        count += 1
                    c = []
                    # compara as listas obtidas,os numeros que sejam
                    # diferentes nas mesmas colunas são removidos
                    for i in range(len(f) - 1):
                        for j in range(len(f[i])):
                            if digitos:  #sempre que gera um novo algarismo retira da amostra de algarismos possiveis, caso não esteja vazia
                                digitos -= {f[i][j]}
                            if f[i][j] != f[i + 1][j]:
                                c.append(j)

                    cpu = f[0]
                    u = list(set(c))  #retira os numeros repetidos da lista c
                    for h in range(len(u)):
                        for t in range(len(cpu)):
                            if t == u[h]:
                                numero2 = random.sample(digitos, 1)
                                l_numero = list(numero2)
                                if digitos:  # sempre que gera um novo algarismo retira da amostra de algarismos possiveis, caso não esteja vazia
                                    digitos -= {l_numero[0]}
                                cpu.insert(t, l_numero[0])
                                cpu.pop(t + 1)

                # vai substituir um a um cada elemento do cpu por um numero ainda n testado
                # se a avaliação do user for menos do que 3T então quer dizer que o numero que substitui era um touro
                # quando encontrar um numero que n é touro
                # vai substituindo até o user dar uma avaliação de 4T que termina o jogo
                elif touro == 3:
                    count += 1
                    while touro != 4:
                        i = 0
                        while i < len(cpu):
                            numero2 = random.sample(digitos, 1)
                            l_numero = list(numero2)
                            f = cpu[i]
                            cpu.insert(i, l_numero[0])
                            cpu.pop(i + 1)
                            resultados = conta_touros_porcos(cpu, jog)
                            str_c = ''
                            for k in cpu:
                                str_c += str(k)
                            conta_tent(count, resultados[0], resultados[1], str_c)
                            touro = resultados[0]
                            porco = resultados[1]
                            if touro == 4:
                                i = 5
                            elif touro == 2:
                                cpu.insert(i, f)
                                cpu.pop(i + 1)
                            else:
                                while touro != 4:
                                    numero2 = random.sample(digitos, 1)
                                    l_numero = list(numero2)
                                    if digitos:
                                        digitos -= {l_numero[0]}
                                    cpu.insert(i, l_numero[0])
                                    cpu.pop(i + 1)
                                    resultados = conta_touros_porcos(cpu, jog)
                                    str_c = ''
                                    for k in cpu:
                                        str_c += str(k)
                                    conta_tent(count, resultados[0], resultados[1], str_c)
                                    touro = resultados[0]
                                    porco = resultados[1]
                                    if touro == 4:
                                        i = 5
                                    count += 1
                            count += 1
                            i += 1
                # caso o numero gerado não tenha porcos ou touros gera um novo numero
                # e retira esses algarismos da amostra de algarismos possiveis
                elif touro == 0 and porco == 0:
                    for h in cpu:
                        digitos -= {h}
                    cpu.clear()
                    numero = random.sample(digitos, 4)  # .sample(0-9, com tamanho 4)
                    cpu = list(numero)
        else:
            print("Por favor insira um numero com 4 digitos distintos")

    print_tentativas(tentativas)
    inicia_jogo()


######################################################################################################
#
# print_tentativas - recebe o dicionário já depois de o jogo ter terminado e imprime-o
#
# Argumentos:
# tentativas - dicionário global onde fica registado as respostas e score do jogador
#
# Retorno:
# Imprime o dicionário "tentativas"
#
######################################################################################################


def print_tentativas(tentativas):
    chaves = list(tentativas.keys())
    chaves.sort(key=int)
    print("As tentativas do cpu foram:")
    for i in range(len(tentativas)):
        print("T" + str(chaves[i]), ":", tentativas[chaves[i]])


######################################################################################################
#
# verifica_input - verifica se o número inserido pelo jogador é constituido apenas por 4 digitos
#
# Argumentos:
# n - input do jogador
#
# Retorna:
# Retorna True se o numero for aceitável, caso contrário retorna False
#
######################################################################################################


def verifica_input(n):
    var = str(n)
    if len(var) != 4:
        return False

    for i in var:
        x = var.count(i)
        if x > 1:
            return False

    try:
        return True
    except ValueError:
        return False


######################################################################################################
#
# conta_touros_porcos - implementa a logica do jogo, comparando as respostas do jogador
#                       com a chave gerada pelo computador
#
# Argumentos:
# cpu - lista global onde fica registado o numero gerado pelo computador
# jog - lista global onde fica registado o numero gerado pelo jogador
#
# Retorna:
# Retorna uma lista que contem os resultados finais das variaveis “touro” e “porco” – [“touro”,”porco”]
#
######################################################################################################


def conta_touros_porcos(cpu, jog):
    t = p = 0
    resultados = []
    for c in range(len(cpu)):
        if (cpu[c] in jog) and (cpu[c] == jog[c]):
            t += 1
        elif cpu[c] in jog:
            p += 1
    resultados.append(t)
    resultados.append(p)

    return resultados


######################################################################################################
#
# inicia_jogo - inicia o jogo caso a resposta seja "sim"
#
# Argumentos:
# Não tem
#
# Retorno:
# Chama a função gera_numero() caso a resposta seja "sim"
#
######################################################################################################

def inicia_jogo():
    pergunta = input("Jogar? (Sim ou Não): ")
    pergunta = pergunta.lower()
    if pergunta == "sim":
        cpu.clear()
        jog.clear()
        tentativas.clear()
        gera_numero()


inicia_jogo()
