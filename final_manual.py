import random

cpu = []
jog = []
tentativas = {}

######################################################################################################
#
# swap - troca os nas posições i e j entre si da lista l
#
# Argumentos:
# l - lista que contem o numero gerado atual pelo cpu
# i - posição do elemento a trocar
# j - posição do elemento a trocar
#
# Retorno:
# Retorna uma lista que contem a avaliação do utilizador e a "lista" em string
#
######################################################################################################

def swap(l,i,j):
    l[i], l[j] = l[j], l[i]

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


def list_to_string(cpu):
    str_c = ''
    resultados = []
    for k in cpu:
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
        tentativas[count] = stri + ", " + str(touro) + "T"
    elif touro == 0 and porco != 0:
        print("o cpu gerou o numero: " + stri + " e obteve a seguinte avaliação: " + str(porco) + "P")
        tentativas[count] = stri + ", " + str(porco) + "P"
    elif touro != 0 and porco == 0 and touro < 4:
        print("o cpu gerou o numero: " + stri + " e obteve a seguinte avaliação: " + str(touro) + "T")
        tentativas[count] = stri + ", " + str(touro) + "T"
    else:
        print("o cpu gerou o numero: " + stri + " e obteve a seguinte avaliação: " + str(touro) + "T" + " " + str(porco) + "P")
        tentativas[count] = stri + ", " + str(touro) + "T" + " " + str(porco) + "P"

######################################################################################################
#
# gera_numero - recebe o input do utilizador e verifica se está dentro
#               do aceitável e implementa a logica do cpu
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
            print(digitos, "digitos")

            while touro != 4:
                print(count, "aqui fora")
                count += 1
                respostas = list_to_string(cpu)
                touro = respostas[0]
                porco = respostas[1]
                conta_tent(count, touro, porco, respostas[2])
                if porco >= 1 or touro >= 1:
                    if touro == 3:
                        touro_3_melhor(cpu, digitos, count)
                    elif touro == 0 and porco == 4:
                        swap(cpu, 0, 1)
                        count += 1
                        respostas = list_to_string(cpu)
                        touro = respostas[0]
                        porco = respostas[1]
                        conta_tent(count, touro, porco, respostas[2])
                        if touro == 2 and porco == 2:
                            touro_2_porco_2(cpu, digitos, count)
                        elif touro == 1 and porco == 3:
                            swap(cpu, 1, 0)
                            swap(cpu, 2, 3)
                            touro_2_porco_2(cpu, digitos, count)
                        elif touro == 0 and porco == 4:
                            swap(cpu, 1, 0)
                            swap(cpu, 0, 2)
                            swap(cpu, 1, 3)
                            count += 1
                            respostas = list_to_string(cpu)
                            touro = respostas[0]
                            porco = respostas[1]
                            if touro == 4:
                                touro = 4
                                conta_tent(count, touro, porco, respostas[2])
                            elif touro == 2 and porco == 2:
                                touro_2_porco_2(cpu, digitos, count)
                            elif touro == 0 and porco == 4:
                                swap(cpu, 0 ,1)
                                swap(cpu, 2, 3)
                                count += 1
                                touro = 4
                                porco = 0
                                cpu_s = ''
                                for i in cpu:
                                    cpu_s += str(i)
                                conta_tent(count, touro, porco, cpu_s)
                    elif touro == 2 and porco == 2:
                        touro_2_porco_2(cpu, digitos, count)
                    elif (touro == 0 and porco == 1) or (touro == 1 and porco == 0):
                        i = random.randint(0, 3)
                        numero2 = random.sample(digitos, 1)
                        l_numero = list(numero2)
                        while l_numero[0] in cpu:
                            numero2 = random.sample(digitos, 1)
                            l_numero = list(numero2)
                        f = cpu[i]
                        cpu.insert(i, l_numero[0])
                        cpu.pop(i + 1)
                        count += 1
                        respostas = list_to_string(cpu)
                        touro_i = respostas[0]
                        porco_i = respostas[1]
                        conta_tent(count, touro, porco, respostas[2])
                        if touro < touro_i and touro == 1:
                            touro_2(cpu, digitos, count)
                        elif porco == porco_i and touro == touro_i:
                            cpu.clear()
                            numero = random.sample(digitos, 4)
                            cpu = list(numero)
                        elif touro > touro_i:
                            cpu.clear()
                            numero = random.sample(digitos, 4)
                            cpu = list(numero)
                        elif touro_i == 1 and porco_i == 1:
                            touro_1_porco_1(cpu, digitos, count)
                        elif touro == touro_i and porco < porco_i:
                            porco_dois(cpu, digitos, count)
                        elif touro == touro_i and porco > porco_i:
                            cpu.clear()
                            numero = random.sample(digitos, 4)
                            cpu = list(numero)
                    elif touro == 0 and porco == 3:
                        cpu.clear()
                        numero = random.sample(digitos, 4)
                        cpu = list(numero)
                    elif touro == 0 and porco == 2:
                        count += 1
                        porco_dois(cpu, digitos, count)
                    elif touro == 1 and porco == 1:
                        count += 1
                        touro_1_porco_1(cpu, digitos, count)
                    elif touro == 2 and porco == 0:
                        count += 1
                        touro_2(cpu, digitos, count)
                    elif touro == 2 and porco == 1:
                        count +=1
                        touro_2_porco_1(cpu, digitos, count)
                    elif touro == 1 and porco == 2:
                        count += 1
                        touro_1_porco_2(cpu, digitos, count)
                # caso o numero gerado não tenha porcos ou touros gera um novo numero
                # e retira esses algarismos da amostra de algarismos possiveis
                else:
                    for h in cpu:
                        digitos -= {h}
                    cpu.clear()
                    numero = random.sample(digitos, 4)  # .sample(0-9, com tamanho 4)
                    cpu = list(numero)
                    print(digitos, "digitoscabaixo")
        else:
            print("Por favor insira um numero com 4 digitos distintos")

    print_tentativas(tentativas)
    inicia_jogo()

######################################################################################################
#
# touro_1_porco_1 - recebe o número gerado no caso 1T 1P e transforma em 2T 0P
#
# Argumentos:
# cpu - lista com o número gerado pelo computador
# digitos - variavel com os numeros que ainda podem ser gerados
# count - variavel que contem o número de tentativas
#
# Retorno:
# Transforma em 2T 0P o número gerado pelo cpu
#
#######################################################################################################

def touro_1_porco_1(cpu, digitos, count):
    print("touro_1_porco_1")
    swap(cpu, 2, 3)
    count += 1
    respostas = list_to_string(cpu)
    touro = respostas[0]
    porco = respostas[1]
    conta_tent(count, touro, porco, respostas[2])
    if touro == 2 and porco == 0:
        touro_2(cpu, digitos, count)
    elif touro == 1 and porco == 1:
        swap(cpu, 3, 2)
        swap(cpu, 0, 3)
        count += 1
        respostas = list_to_string(cpu)
        touro = respostas[0]
        porco = respostas[1]
        conta_tent(count, touro, porco, respostas[2])
        if touro == 2 and porco == 0:
            touro_2(cpu, digitos, count)
        else:
            swap(cpu, 3, 0)
            swap(cpu, 1, 2)
            count += 1
            respostas = list_to_string(cpu)
            touro = respostas[0]
            porco = respostas[1]
            conta_tent(count, touro, porco, respostas[2])
            if touro == 2 and porco == 0:
                touro_2(cpu, digitos, count)
            else:
                swap(cpu, 2, 1)
                swap(cpu, 0, 3)
                count += 1
                respostas = list_to_string(cpu)
                touro = respostas[0]
                porco = respostas[1]
                conta_tent(count, touro, porco, respostas[2])
                if touro == 2 and porco == 0:
                    touro_2
                else:
                    swap(cpu, 3, 0)
                    swap(cpu, 1, 3)
                    touro_2(cpu, digitos, count)
    elif touro == 0 and porco == 2:
        swap(cpu, 3, 2)
        swap(cpu, 0, 1)
        count += 1
        respostas = list_to_string(cpu)
        touro = respostas[0]
        porco = respostas[1]
        conta_tent(count, touro, porco, respostas[2])
        if touro == 2 and porco == 0:
            touro_2(cpu, digitos, count)
        else:
            swap(cpu, 1, 0)
            swap(cpu, 0, 2)
            count += 1
            respostas = list_to_string(cpu)
            touro = respostas[0]
            porco = respostas[1]
            conta_tent(count, touro, porco, respostas[2])
            if touro == 2 and porco == 0:
                touro_2(cpu, digitos, count)
            else:
                swap(cpu, 2, 0)
                swap(cpu, 0, 3)
                count += 1
                respostas = list_to_string(cpu)
                touro = respostas[0]
                porco = respostas[1]
                conta_tent(count, touro, porco, respostas[2])
                if touro == 2 and porco == 0:
                    touro_2(cpu, digitos, count)
                else:
                    swap(cpu, 3, 0)
                    swap(cpu, 1, 3)
                    count += 1
                    respostas = list_to_string(cpu)
                    touro = respostas[0]
                    porco = respostas[1]
                    conta_tent(count, touro, porco, respostas[2])
                    if touro == 2 and porco == 0:
                        touro_2(cpu, digitos, count)
                    else:
                        swap(cpu, 3, 1)
                        swap(cpu, 1, 2)
                        count += 1
                        respostas = list_to_string(cpu)
                        touro = respostas[0]
                        porco = respostas[1]
                        conta_tent(count, touro, porco, respostas[2])
                        if touro == 2 and porco == 0:
                            touro_2(cpu, digitos, count)


######################################################################################################
#
# touro_2_porco_2 - recebe o número gerado no caso 2T 2P e transforma em 4T 0P
#
# Argumentos:
# cpu - lista com o número gerado pelo computador
# digitos - variavel com os numeros que ainda podem ser gerados
# count - variavel que contem o número de tentativas
#
# Retorno:
# Transforma em 4T 0P o número gerado pelo cpu
#
#######################################################################################################

def touro_2_porco_2(cpu, digitos, count): # exemplo:1243 , 2134, 4231, 3214, 1324, 1432
    swap(cpu, 2, 3)
    count += 1
    respostas = list_to_string(cpu)
    touro = respostas[0]
    porco = respostas[1]
    cpu_s = ''
    for i in cpu:
        cpu_s += str(i)
    conta_tent(count, touro, porco, cpu_s)
    if touro == 4 and porco == 0:
        print_tentativas(tentativas)
        inicia_jogo()
    elif touro == 0 and porco == 4:
        swap(cpu, 3, 2)
        swap(cpu, 0, 1)
        count += 1
        cpu_s = ''
        for i in cpu:
            cpu_s += str(i)
        conta_tent(count, 4, 0, cpu_s)
        print_tentativas(tentativas)
        inicia_jogo()
    elif touro == 1 and porco == 3:
        swap(cpu, 3, 2)
        count += 1
        respostas = list_to_string(cpu)
        touro = respostas[0]
        porco = respostas[1]
        conta_tent(count, touro, porco, respostas[2])
        if touro == 2 and porco == 2:
            swap(cpu, 1, 3)
            count += 1
            respostas = list_to_string(cpu)
            touro = respostas[0]
            porco = respostas[1]
            cpu_s = ''
            for i in cpu:
                cpu_s += str(i)
            conta_tent(count, touro, porco, cpu_s)
            if touro == 4 and porco == 0:
                print_tentativas(tentativas)
                inicia_jogo()
            elif touro == 0 and porco == 4:
                swap(cpu, 3, 1)
                swap(cpu, 0, 2)
                count += 1
                cpu_s = ''
                for i in cpu:
                    cpu_s += str(i)
                conta_tent(count, 4, 0, cpu_s)
                print_tentativas(tentativas)
                inicia_jogo()
            elif touro == 1 and porco == 3:
                swap(cpu, 3, 1)
                count += 1
                respostas = list_to_string(cpu)
                touro = respostas[0]
                porco = respostas[1]
                conta_tent(count, touro, porco, respostas[2])
                if touro == 2 and porco == 2:
                    swap(cpu, 0, 3)
                    count += 1
                    respostas = list_to_string(cpu)
                    touro = respostas[0]
                    porco = respostas[1]
                    cpu_s = ''
                    for i in cpu:
                        cpu_s += str(i)
                    conta_tent(count, touro, porco, cpu_s)
                    if touro == 4 and porco == 0:
                        print_tentativas(tentativas)
                        inicia_jogo()
                    elif touro == 0 and porco == 4:
                        swap(cpu, 0, 3)
                        swap(cpu, 1, 2)
                        count += 1
                        cpu_s = ''
                        for i in cpu:
                            cpu_s += str(i)
                        conta_tent(count, 4, 0, cpu_s)
                        print_tentativas(tentativas)
                        inicia_jogo()

######################################################################################################
#
# porco_dois - recebe o número gerado no caso 0T 1P ou 1T 0P e transforma em 2T 0P ou 1T 1P
#
# Argumentos:
# cpu - lista com o número gerado pelo computador
# digitos - variavel com os numeros que ainda podem ser gerados
# count - variavel que contem o número de tentativas
#
# Retorno:
# Transforma em 2T 0P ou 1T 1P o número gerado pelo cpu
#
#######################################################################################################

def porco_dois(cpu, digitos, count):
    count = count
    print("porco_2")
    swap(cpu, 2, 3)
    count += 1
    respostas = list_to_string(cpu)
    touro = respostas[0]
    porco = respostas[1]
    conta_tent(count, touro, porco, respostas[2])
    if touro == 1 and porco == 1:
        touro_1_porco_1(cpu, digitos, count)
    elif touro == 2:
        touro_2(cpu, digitos, count)
    elif touro == 0 and porco == 2:
        swap(cpu, 3, 2)
        swap(cpu, 1, 2)
        count += 1
        respostas = list_to_string(cpu)
        touro = respostas[0]
        porco = respostas[1]
        conta_tent(count, touro, porco, respostas[2])
        if touro == 1 and porco == 1:
            touro_1_porco_1(cpu, digitos, count)
        elif touro == 2:
            touro_2(cpu, digitos, count)
        elif touro == 0 and porco == 2:
            swap(cpu, 2, 1)
            swap(cpu, 0, 2)
            count += 1
            respostas = list_to_string(cpu)
            touro = respostas[0]
            porco = respostas[1]
            conta_tent(count, touro, porco, respostas[2])
            if touro == 1 and porco == 1:
                touro_1_porco_1(cpu, digitos, count)
            elif touro == 2:
                touro_2(cpu, digitos, count)
            elif touro == 0 and porco == 2:
                swap(cpu, 2, 0)
                swap(cpu, 0, 3)
                count += 1
                respostas = list_to_string(cpu)
                touro = respostas[0]
                porco = respostas[1]
                conta_tent(count, touro, porco, respostas[2])
                if touro == 1 and porco == 1:
                    touro_1_porco_1(cpu, digitos, count)
                elif touro == 2:
                    touro_2(cpu, digitos, count)
                elif touro == 0 and porco == 2:
                    swap(cpu, 3, 0)
                    swap(cpu, 0, 1)
                    count += 1
                    respostas = list_to_string(cpu)
                    touro = respostas[0]
                    porco = respostas[1]
                    conta_tent(count, touro, porco, respostas[2])
                    if touro == 1 and porco == 1:
                        touro_1_porco_1(cpu, digitos, count)
                    elif touro == 2:
                        touro_2(cpu, digitos, count)
                    elif touro == 0 and porco == 2:
                        swap(cpu, 1, 0)
                        swap(cpu, 1, 3)
                        touro_2(cpu, digitos, count)

######################################################################################################
#
# touro_2 - recebe o número gerado no caso 0T 2P ou 1T 1P e transforma em 3T 0P ou 2T 1P
#
# Argumentos:
# cpu - lista com o número gerado pelo computador
# digitos - variavel com os numeros que ainda podem ser gerados
# count - variavel que contem o número de tentativas
#
# Retorno:
# Transforma em 3T 0P ou 2T 1P o número gerado pelo cpu
#
#######################################################################################################

def touro_2(cpu, digitos, count):
    print("touro_2")
    # xx34 -> 3xx4
    swap(cpu, 0, 2)
    count += 1
    respostas = list_to_string(cpu)
    touro = respostas[0]
    porco = respostas[1]
    conta_tent(count, touro, porco, respostas[2])
    if touro == 0 and porco == 2:
        swap(cpu, 2, 0)
        for h in cpu:
            digitos -= {h}
        print("caso 5")
        while True:
            p1 = cpu[1]
            numero2 = random.sample(digitos, 1)
            l_numero = list(numero2)
            novo1 = l_numero[0]
            cpu.insert(1, l_numero[0])
            cpu.pop(2)
            numero2 = random.sample(digitos, 1)
            l_numero2 = list(numero2)
            while l_numero2[0] in cpu:
                numero2 = random.sample(digitos, 1)
                l_numero2 = list(numero2)
            novo2 = l_numero2[0]
            cpu.insert(3, l_numero2[0])
            cpu.pop(4)
            count += 1
            respostas = list_to_string(cpu)
            touro = respostas[0]
            porco = respostas[1]
            conta_tent(count, touro, porco, respostas[2])
            if touro == 4:
                print_tentativas(tentativas)
                inicia_jogo()
            elif touro == 3:
                cpu.insert(1, p1)
                cpu.pop(2)
                count += 1
                respostas = list_to_string(cpu)
                touro = respostas[0]
                porco = respostas[1]
                conta_tent(count, touro, porco, respostas[2])
                if touro == 2:
                    cpu.insert(0, novo1)
                    cpu.pop(1)
                    while touro != 4:
                        for h in cpu:
                            digitos -= {h}
                        numero2 = random.sample(digitos, 1)
                        l_numero = list(numero2)
                        digitos -= {l_numero[0]}
                        cpu.insert(3, l_numero[0])
                        cpu.pop(4)
                        count += 1
                        respostas = list_to_string(cpu)
                        touro = respostas[0]
                        porco = respostas[1]
                        conta_tent(count, touro, porco, respostas[2])
                        if touro == 4:
                            print_tentativas(tentativas)
                            inicia_jogo()
                        count += 1
                else:
                    while touro != 4:
                        for h in cpu:
                            digitos -= {h}
                        numero2 = random.sample(digitos, 1)
                        l_numero = list(numero2)
                        digitos -= {l_numero[0]}
                        cpu.insert(1, l_numero[0])
                        cpu.pop(2)
                        count += 1
                        respostas = list_to_string(cpu)
                        touro = respostas[0]
                        porco = respostas[1]
                        conta_tent(count, touro, porco, respostas[2])
                        if touro == 4:
                            print_tentativas(tentativas)
                            inicia_jogo()
                        count += 1
            elif touro == 2 and porco == 0:
                digitos -= {novo1}
                digitos -= {novo2}
            elif touro == 2 and porco == 2:
                touro_2_porco_2(cpu, digitos, count)
    elif touro == 2 and porco == 0:
        swap(cpu, 2, 0)
        for h in cpu:
            digitos -= {h}
        print("caso 6")
        while True:
            p1 = cpu[0]
            numero2 = random.sample(digitos, 1)
            l_numero = list(numero2)
            novo1 = l_numero[0]
            cpu.insert(0, l_numero[0])
            cpu.pop(1)
            numero2 = random.sample(digitos, 1)
            l_numero2 = list(numero2)
            while l_numero2[0] in cpu:
                numero2 = random.sample(digitos, 1)
                l_numero2 = list(numero2)
            novo2 = l_numero2[0]
            cpu.insert(2, l_numero2[0])
            cpu.pop(3)
            count += 1
            respostas = list_to_string(cpu)
            touro = respostas[0]
            porco = respostas[1]
            conta_tent(count, touro, porco, respostas[2])
            if touro == 4:
                print_tentativas(tentativas)
                inicia_jogo()
            elif touro == 3:
                cpu.insert(0, p1)
                cpu.pop(1)
                count += 1
                respostas = list_to_string(cpu)
                touro = respostas[0]
                porco = respostas[1]
                conta_tent(count, touro, porco, respostas[2])
                if touro == 2:
                    cpu.insert(0, novo1)
                    cpu.pop(1)
                    while touro != 4:
                        for h in cpu:
                            digitos -= {h}
                        numero2 = random.sample(digitos, 1)
                        l_numero = list(numero2)
                        digitos -= {l_numero[0]}
                        cpu.insert(2, l_numero[0])
                        cpu.pop(3)
                        count += 1
                        respostas = list_to_string(cpu)
                        touro = respostas[0]
                        porco = respostas[1]
                        conta_tent(count, touro, porco, respostas[2])
                        if touro == 4:
                            print_tentativas(tentativas)
                            inicia_jogo()
                        count += 1
                else:
                    while touro != 4:
                        for h in cpu:
                            digitos -= {h}
                        numero2 = random.sample(digitos, 1)
                        l_numero = list(numero2)
                        digitos -= {l_numero[0]}
                        cpu.insert(0, l_numero[0])
                        cpu.pop(1)
                        count += 1
                        respostas = list_to_string(cpu)
                        touro = respostas[0]
                        porco = respostas[1]
                        conta_tent(count, touro, porco, respostas[2])
                        if touro == 4:
                            print_tentativas(tentativas)
                            inicia_jogo()
                        count += 1
            elif touro == 2 and porco == 0:
                digitos -= {novo1}
                digitos -= {novo2}
            elif touro == 2 and porco == 2:
                touro_2_porco_2(cpu, digitos, count)
    elif touro == 1 and porco == 1:
        swap(cpu, 2, 0)
        print("caso 1/2/3/4")
        # xx34 -> 4x3x
        swap(cpu, 0, 3)
        count += 1
        respostas = list_to_string(cpu)
        touro = respostas[0]
        porco = respostas[1]
        conta_tent(count, touro, porco, respostas[2])
        if touro == 2 and porco == 0:
            swap(cpu, 3, 0)
            for h in cpu:
                digitos -= {h}
            print("caso 4")
            while True:
                p1 = cpu[0]
                numero2 = random.sample(digitos, 1)
                l_numero = list(numero2)
                novo1 = l_numero[0]
                cpu.insert(0, l_numero[0])
                cpu.pop(1)
                numero2 = random.sample(digitos, 1)
                l_numero2 = list(numero2)
                while l_numero2[0] in cpu:
                    numero2 = random.sample(digitos, 1)
                    l_numero2 = list(numero2)
                novo2 = l_numero2[0]
                cpu.insert(3, l_numero2[0])
                cpu.pop(4)
                count += 1
                respostas = list_to_string(cpu)
                touro = respostas[0]
                porco = respostas[1]
                conta_tent(count, touro, porco, respostas[2])
                if touro == 4:
                    print_tentativas(tentativas)
                    inicia_jogo()
                elif touro == 3:
                    cpu.insert(0, p1)
                    cpu.pop(1)
                    count += 1
                    respostas = list_to_string(cpu)
                    touro = respostas[0]
                    porco = respostas[1]
                    conta_tent(count, touro, porco, respostas[2])
                    if touro == 2:
                        cpu.insert(0, novo1)
                        cpu.pop(1)
                        while touro != 4:
                            for h in cpu:
                                digitos -= {h}
                            numero2 = random.sample(digitos, 1)
                            l_numero = list(numero2)
                            digitos -= {l_numero[0]}
                            cpu.insert(3, l_numero[0])
                            cpu.pop(4)
                            count += 1
                            respostas = list_to_string(cpu)
                            touro = respostas[0]
                            porco = respostas[1]
                            conta_tent(count, touro, porco, respostas[2])
                            if touro == 4:
                                print_tentativas(tentativas)
                                inicia_jogo()
                            count += 1
                    else:
                        while touro != 4:
                            for h in cpu:
                                digitos -= {h}
                            numero2 = random.sample(digitos, 1)
                            l_numero = list(numero2)
                            digitos -= {l_numero[0]}
                            cpu.insert(0, l_numero[0])
                            cpu.pop(1)
                            count += 1
                            respostas = list_to_string(cpu)
                            touro = respostas[0]
                            porco = respostas[1]
                            conta_tent(count, touro, porco, respostas[2])
                            if touro == 4:
                                print_tentativas(tentativas)
                                inicia_jogo()
                            count += 1
                elif touro == 2 and porco == 0:
                    digitos -= {novo1}
                    digitos -= {novo2}
                elif touro == 2 and porco == 2:
                    touro_2_porco_2(cpu, digitos, count)
        elif touro == 0 and porco == 2:
            swap(cpu, 3, 0)
            for h in cpu:
                digitos -= {h}
            print("caso 3")
            while True:
                p1 = cpu[1]
                numero2 = random.sample(digitos, 1)
                l_numero = list(numero2)
                novo1 = l_numero[0]
                cpu.insert(1, l_numero[0])
                cpu.pop(2)
                numero2 = random.sample(digitos, 1)
                l_numero2 = list(numero2)
                while l_numero2[0] in cpu:
                    numero2 = random.sample(digitos, 1)
                    l_numero2 = list(numero2)
                novo2 = l_numero2[0]
                cpu.insert(2, l_numero2[0])
                cpu.pop(3)
                count += 1
                respostas = list_to_string(cpu)
                touro = respostas[0]
                porco = respostas[1]
                conta_tent(count, touro, porco, respostas[2])
                if touro == 4:
                    print_tentativas(tentativas)
                    inicia_jogo()
                elif touro == 3:
                    cpu.insert(1, p1)
                    cpu.pop(2)
                    count += 1
                    respostas = list_to_string(cpu)
                    touro = respostas[0]
                    porco = respostas[1]
                    conta_tent(count, touro, porco, respostas[2])
                    if touro == 2:
                        cpu.insert(1, novo1)
                        cpu.pop(2)
                        while touro != 4:
                            for h in cpu:
                                digitos -= {h}
                            numero2 = random.sample(digitos, 1)
                            l_numero = list(numero2)
                            digitos -= {l_numero[0]}
                            cpu.insert(2, l_numero[0])
                            cpu.pop(3)
                            count += 1
                            respostas = list_to_string(cpu)
                            touro = respostas[0]
                            porco = respostas[1]
                            conta_tent(count, touro, porco, respostas[2])
                            if touro == 4:
                                print_tentativas(tentativas)
                                inicia_jogo()
                            count += 1
                    else:
                        while touro != 4:
                            for h in cpu:
                                digitos -= {h}
                            numero2 = random.sample(digitos, 1)
                            l_numero = list(numero2)
                            digitos -= {l_numero[0]}
                            cpu.insert(1, l_numero[0])
                            cpu.pop(2)
                            count += 1
                            respostas = list_to_string(cpu)
                            touro = respostas[0]
                            porco = respostas[1]
                            conta_tent(count, touro, porco, respostas[2])
                            if touro == 4:
                                print_tentativas(tentativas)
                                inicia_jogo()
                            count += 1
                elif touro == 2 and porco == 0:
                    digitos -= {novo1}
                    digitos -= {novo2}
                elif touro == 2 and porco == 2:
                    touro_2_porco_2(cpu, digitos, count)
        elif touro == 1 and porco == 1:
            swap(cpu, 3, 0)
            print("caso 1/2")
            # 12xx -> 21xx
            swap(cpu, 0, 1)
            count += 1
            respostas = list_to_string(cpu)
            touro = respostas[0]
            porco = respostas[1]
            conta_tent(count, touro, porco, respostas[2])
            if touro == 2 and porco == 0:
                swap(cpu, 0, 1)
                for h in cpu:
                    digitos -= {h}
                print("caso 1")
                while True:
                    p1 = cpu[0]
                    numero2 = random.sample(digitos, 1)
                    l_numero = list(numero2)
                    novo1 = l_numero[0]
                    cpu.insert(0, l_numero[0])
                    cpu.pop(1)
                    numero2 = random.sample(digitos, 1)
                    l_numero2 = list(numero2)
                    while l_numero2[0] in cpu:
                        numero2 = random.sample(digitos, 1)
                        l_numero2 = list(numero2)
                    novo2 = l_numero2[0]
                    cpu.insert(1, l_numero2[0])
                    cpu.pop(2)
                    count += 1
                    respostas = list_to_string(cpu)
                    touro = respostas[0]
                    porco = respostas[1]
                    conta_tent(count, touro, porco, respostas[2])
                    if touro == 4:
                        print_tentativas(tentativas)
                        inicia_jogo()
                    elif touro == 3:
                        cpu.insert(0, p1)
                        cpu.pop(1)
                        count += 1
                        respostas = list_to_string(cpu)
                        touro = respostas[0]
                        porco = respostas[1]
                        conta_tent(count, touro, porco, respostas[2])
                        if touro == 2:
                            cpu.insert(0, novo1)
                            cpu.pop(1)
                            while touro != 4:
                                for h in cpu:
                                    digitos -= {h}
                                numero2 = random.sample(digitos, 1)
                                l_numero = list(numero2)
                                digitos -= {l_numero[0]}
                                cpu.insert(1, l_numero[0])
                                cpu.pop(2)
                                count += 1
                                respostas = list_to_string(cpu)
                                touro = respostas[0]
                                porco = respostas[1]
                                conta_tent(count, touro, porco, respostas[2])
                                if touro == 4:
                                    print_tentativas(tentativas)
                                    inicia_jogo()
                                count += 1
                        else:
                            while touro != 4:
                                for h in cpu:
                                    digitos -= {h}
                                numero2 = random.sample(digitos, 1)
                                l_numero = list(numero2)
                                digitos -= {l_numero[0]}
                                cpu.insert(0, l_numero[0])
                                cpu.pop(1)
                                count += 1
                                respostas = list_to_string(cpu)
                                touro = respostas[0]
                                porco = respostas[1]
                                conta_tent(count, touro, porco, respostas[2])
                                if touro == 4:
                                    print_tentativas(tentativas)
                                    inicia_jogo()
                                count += 1
                    elif touro == 2 and porco == 0:
                        digitos -= {novo1}
                        digitos -= {novo2}
                    elif touro == 2 and porco == 2:
                        touro_2_porco_2(cpu, digitos, count)
            elif touro == 0 and porco == 2:
                swap(cpu, 0, 1)
                print("caso 2")
                for h in cpu:
                    digitos -= {h}
                while True:
                    p1 = cpu[2]
                    numero2 = random.sample(digitos, 1)
                    l_numero = list(numero2)
                    novo1 = l_numero[0]
                    cpu.insert(2, l_numero[0])
                    cpu.pop(3)
                    numero2 = random.sample(digitos, 1)
                    l_numero2 = list(numero2)
                    while l_numero2[0] in cpu:
                        numero2 = random.sample(digitos, 1)
                        l_numero2 = list(numero2)
                    novo2 = l_numero2[0]
                    cpu.insert(3, l_numero2[0])
                    cpu.pop(4)
                    count += 1
                    respostas = list_to_string(cpu)
                    touro = respostas[0]
                    porco = respostas[1]
                    conta_tent(count, touro, porco, respostas[2])
                    if touro == 4:
                        print_tentativas(tentativas)
                        inicia_jogo()
                    elif touro == 3:
                        cpu.insert(2, p1)
                        cpu.pop(3)
                        count += 1
                        respostas = list_to_string(cpu)
                        touro = respostas[0]
                        porco = respostas[1]
                        conta_tent(count, touro, porco, respostas[2])
                        if touro == 2:
                            cpu.insert(2, novo1)
                            cpu.pop(3)
                            while touro != 4:
                                for h in cpu:
                                    digitos -= {h}
                                numero2 = random.sample(digitos, 1)
                                l_numero = list(numero2)
                                digitos -= {l_numero[0]}
                                cpu.insert(3, l_numero[0])
                                cpu.pop(4)
                                count += 1
                                respostas = list_to_string(cpu)
                                touro = respostas[0]
                                porco = respostas[1]
                                conta_tent(count, touro, porco, respostas[2])
                                if touro == 4:
                                    print_tentativas(tentativas)
                                    inicia_jogo()
                                count += 1
                        else:
                            while touro != 4:
                                for h in cpu:
                                    digitos -= {h}
                                numero2 = random.sample(digitos, 1)
                                l_numero = list(numero2)
                                digitos -= {l_numero[0]}
                                cpu.insert(2, l_numero[0])
                                cpu.pop(3)
                                count += 1
                                respostas = list_to_string(cpu)
                                touro = respostas[0]
                                porco = respostas[1]
                                conta_tent(count, touro, porco, respostas[2])
                                if touro == 4:
                                    print_tentativas(tentativas)
                                    inicia_jogo()
                                count += 1
                    elif touro == 2 and porco == 0:
                        digitos -= {novo1}
                        digitos -= {novo2}
                    elif touro == 2 and porco == 2:
                        touro_2_porco_2(cpu, digitos, count)

######################################################################################################
#
# touro_2_porco_1 - recebe o número gerado no caso 2T 1P ou 2T 0P e transforma em 4T 0P
#
# Argumentos:
# cpu - lista com o número gerado pelo computador
# digitos - variavel com os numeros que ainda podem ser gerados
# count - variavel que contem o número de tentativas
#
# Retorno:
# Transforma em 4T 0P o número gerado pelo cpu
#
#######################################################################################################

def touro_3_melhor(cpu, digitos, count):
    for i in cpu:
        digitos -= {i}
    swap(cpu, 2, 3)
    count += 1
    respostas = list_to_string(cpu)
    touro = respostas[0]
    porco = respostas[1]
    conta_tent(count, touro, porco, respostas[2])
    if touro == 1 and porco == 2:
        swap(cpu, 2, 3)
        while touro != 4:
            f = cpu[0]
            numero2 = random.sample(digitos, 1)
            l_numero = list(numero2)
            digitos -= {l_numero[0]}
            cpu.insert(0, l_numero[0])
            cpu.pop(1)
            count += 1
            respostas = list_to_string(cpu)
            touro = respostas[0]
            porco = respostas[1]
            conta_tent(count, touro, porco, respostas[2])
            if touro == 4:
                print_tentativas(tentativas)
                inicia_jogo()
            elif touro == 2:
                cpu.insert(0, f)
                cpu.pop(1)
                while touro != 4:
                    numero2 = random.sample(digitos, 1)
                    l_numero = list(numero2)
                    digitos -= {l_numero[0]}
                    cpu.insert(1, l_numero[0])
                    cpu.pop(2)
                    count += 1
                    respostas = list_to_string(cpu)
                    touro = respostas[0]
                    porco = respostas[1]
                    conta_tent(count, touro, porco, respostas[2])
                    if touro == 4:
                        print_tentativas(tentativas)
                        inicia_jogo()
    else:
        swap(cpu, 2, 3)
        while touro != 4:
            f = cpu[2]
            numero2 = random.sample(digitos, 1)
            l_numero = list(numero2)
            digitos -= {l_numero[0]}
            cpu.insert(2, l_numero[0])
            cpu.pop(3)
            count += 1
            respostas = list_to_string(cpu)
            touro = respostas[0]
            porco = respostas[1]
            conta_tent(count, touro, porco, respostas[2])
            if touro == 4:
                print_tentativas(tentativas)
                inicia_jogo()
            elif touro == 2:
                cpu.insert(2, f)
                cpu.pop(3)
                while touro != 4:
                    numero2 = random.sample(digitos, 1)
                    l_numero = list(numero2)
                    digitos -= {l_numero[0]}
                    cpu.insert(3, l_numero[0])
                    cpu.pop(4)
                    count += 1
                    respostas = list_to_string(cpu)
                    touro = respostas[0]
                    porco = respostas[1]
                    conta_tent(count, touro, porco, respostas[2])
                    if touro == 4:
                        print_tentativas(tentativas)
                        inicia_jogo()
        
        
"""
def touro_3_melhor(cpu, digitos, count):
    touro = 3
    for i in cpu:
        digitos -= {i}
    while touro != 4:
        i = 0
        while i < len(cpu):
            numero2 = random.sample(digitos, 1)
            l_numero = list(numero2)
            f = cpu[i]
            cpu.insert(i, l_numero[0])
            cpu.pop(i + 1)
            count += 1
            respostas = list_to_string(cpu)
            touro = respostas[0]
            porco = respostas[1]
            conta_tent(count, touro, porco, respostas[2])
            if touro == 4:
                print_tentativas(tentativas)
                inicia_jogo()
            elif touro == 2:
                cpu.insert(i, f)
                cpu.pop(i + 1)
            else:
                while touro != 4:
                    numero2 = random.sample(digitos, 1)
                    l_numero = list(numero2)
                    digitos -= {l_numero[0]}
                    cpu.insert(i, l_numero[0])
                    cpu.pop(i + 1)
                    count += 1
                    respostas = list_to_string(cpu)
                    touro = respostas[0]
                    porco = respostas[1]
                    conta_tent(count, touro, porco, respostas[2])
                    if touro == 4:
                        print_tentativas(tentativas)
                        inicia_jogo()
            i += 1
"""

######################################################################################################
#
# touro_2_porco_1 - recebe o número gerado no caso 1T 2P e transforma em 3T 0P
#
# Argumentos:
# cpu - lista com o número gerado pelo computador
# digitos - variavel com os numeros que ainda podem ser gerados
# count - variavel que contem o número de tentativas
#
# Retorno:
# Transforma em 3T 0P o número gerado pelo cpu
#
#######################################################################################################

def touro_2_porco_1(cpu, digitos, count):
    count = count
    swap(cpu, 2, 3)
    respostas = list_to_string(cpu)
    touro = respostas[0]
    porco = respostas[1]
    conta_tent(count, touro, porco, respostas[2])
    if touro == 3 and porco == 0:
        touro_3_melhor(cpu, digitos, count)
    else:
        swap(cpu, 3, 2)
        swap(cpu, 0, 1)
        count += 1
        respostas = list_to_string(cpu)
        touro = respostas[0]
        porco = respostas[1]
        conta_tent(count, touro, porco, respostas[2])
        if touro == 3 and porco == 0:
            touro_3_melhor(cpu, digitos, count)
        else:
            swap(cpu, 1, 0)
            swap(cpu, 0, 2)
            count += 1
            respostas = list_to_string(cpu)
            touro = respostas[0]
            porco = respostas[1]
            conta_tent(count, touro, porco, respostas[2])
            if touro == 3 and porco == 0:
                touro_3_melhor(cpu, digitos, count)
            else:
                swap(cpu, 2, 0)
                swap(cpu, 0, 3)
                count += 1
                respostas = list_to_string(cpu)
                touro = respostas[0]
                porco = respostas[1]
                conta_tent(count, touro, porco, respostas[2])
                if touro == 3 and porco == 0:
                    touro_3_melhor(cpu, digitos, count)
                else:
                    swap(cpu, 3, 0)
                    swap(cpu, 1, 2)
                    count += 1
                    respostas = list_to_string(cpu)
                    touro = respostas[0]
                    porco = respostas[1]
                    conta_tent(count, touro, porco, respostas[2])
                    if touro == 3 and porco == 0:
                        touro_3_melhor(cpu, digitos, count)
                    else:
                        swap(cpu, 2, 1)
                        swap(cpu, 1, 3)
                        touro_3_melhor(cpu, digitos, count)

######################################################################################################
#
# touro_2_porco_1 - recebe o número gerado e transforma em 2T 1P
#
# Argumentos:
# cpu - lista com o número gerado pelo computador
# digitos - variavel com os numeros que ainda podem ser gerados
# count - variavel que contem o número de tentativas
#
# Retorno:
# Transforma em 2T 1P
#
#######################################################################################################

def touro_1_porco_2(cpu, digitos, count):
    count = count
    swap(cpu, 2, 3)
    respostas = list_to_string(cpu)
    touro = respostas[0]
    porco = respostas[1]
    conta_tent(count, touro, porco, respostas[2])
    if touro == 3 and porco == 0:
        touro_3_melhor(cpu, digitos, count)
    elif touro == 2 and porco == 1:
        touro_2_porco_1(cpu, digitos, count)
    else:
        swap(cpu, 3, 2)
        swap(cpu, 0, 1)
        count += 1
        respostas = list_to_string(cpu)
        touro = respostas[0]
        porco = respostas[1]
        conta_tent(count, touro, porco, respostas[2])
        if touro == 3 and porco == 0:
            touro_3_melhor(cpu, digitos, count)
        elif touro == 2 and porco == 1:
            touro_2_porco_1(cpu, digitos, count)
        else:
            swap(cpu, 1, 0)
            swap(cpu, 0, 2)
            count += 1
            respostas = list_to_string(cpu)
            touro = respostas[0]
            porco = respostas[1]
            conta_tent(count, touro, porco, respostas[2])
            if touro == 3 and porco == 0:
                touro_3_melhor(cpu, digitos, count)
            elif touro == 2 and porco == 1:
                touro_2_porco_1(cpu, digitos, count)
            else:
                swap(cpu, 2, 0)
                swap(cpu, 1, 2)
                count += 1
                respostas = list_to_string(cpu)
                touro = respostas[0]
                porco = respostas[1]
                conta_tent(count, touro, porco, respostas[2])
                if touro == 3 and porco == 0:
                    touro_3_melhor(cpu, digitos, count)
                elif touro == 2 and porco == 1:
                    touro_2_porco_1(cpu, digitos, count)
                else:
                    swap(cpu, 2, 1)
                    swap(cpu, 1, 3)
                    count += 1
                    respostas = list_to_string(cpu)
                    touro = respostas[0]
                    porco = respostas[1]
                    conta_tent(count, touro, porco, respostas[2])
                    if touro == 3 and porco == 0:
                        touro_3_melhor(cpu, digitos, count)
                    elif touro == 2 and porco == 1:
                        touro_2_porco_1(cpu, digitos, count)
                    else:
                        swap(cpu, 3, 1)
                        swap(cpu, 0, 3)
                        touro_3_melhor(cpu, digitos, count)

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
