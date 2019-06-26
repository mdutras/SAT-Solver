'''
Written by Mateus Dutra Santiago in June/2019.
'''
#Transforma string em inteiro
def turn_int0(variavel):
    variavel = int(variavel)
    return variavel
#Transforma os elementos de listas de strings em inteiros
def turn_int1(lista):
    a = []
    for num in lista:
        ni = int(num)
        a.append(ni)
    return a
#Transforma os elementos de listas de listas de strings em inteiros 
def turn_int2(lista):
    a = []
    b = []
    for num in lista:
        for n in num:
            ni = int(n)
            a.append(ni)
        b.append(a)
        a = []
    return b
#Cria as variaveis espontaneamente, sem a necessidade do usuario inserí-las 
def variaveis(y):
    v = []
    a = 0
    while y > 0:
        a += 1
        v.append(a)
        y-=1
    return v
#Inserir as clausulas
def clausulas(y):
    c = []
    while y > 0:
        mini = input().split(" ")
        c.append(mini)
        y-=1
    c = turn_int2(c)
    return c
#Função recebe a permutação de Soma_bin e multiplica os elementos dentro dos párenteses e soma os que estâo fora
#Se a som > 0, então a clausula foi naõ foi satisfativel pára aquela lista
#Se soma==0, então a clausula foi satisfativel para aquela lista
def resolucao(c,b,v):
    #print("-->", b)
    m = 1
    mul = []
    for num in c:
        for n in num:
            if n==0:
                mul.append(m)
                m = 1
            elif n!=0:
                k = 1
                while k <= v:
                    if k==n:
                        m *= b[k-1]
                    elif -k == n:
                        if b[k-1]==0:
                            m*=1
                        elif b[k-1]==1:
                            m*=0
                    k+=1
    soma = 0
    for num in mul:
        soma += num
    return soma
#Calcula todas as permutações de 1 e 0, sendo  0 == True e 1 == False numa lista de tamanho do n de variaveis e envia para função resolução,e acumula o resultado da função  
def soma_bin(c ,v):
    resp = 0
    ans = 0
    r = []
    cont = 0
    while cont<v:
        r.append(0);
        cont+=1
    if resolucao(c,r,v)==0:
        resp += 1
    cont = 1
    cont1 = (2**v)
    while(cont<cont1):
        z = 0
        cont2 = v-1
        while z!=1:
            if cont % 2 == 1:
                r[v-1] = 1
                z = 1
            elif cont % (2**cont2) == 0:
                p = v - cont2 - 1
                r[p] = 1
                p += 1
                while p < v:
                    r[p] = 0
                    p += 1
                z = 1
            cont2-=1
        cont+=1
        resp = resolucao(c,r,v)
        if resp==0:
            ans+=1
    return ans
#-----------------------Programa principal-----------------------------------
entrada = input().split(" ")
var = turn_int0(entrada[2])
clas = turn_int0(entrada[3])
v = variaveis(var)
c = clausulas(clas)
fim = soma_bin(c,var)
if fim > 0:
    print("Satisfiable")#Se for satisfátivel
elif fim==0:
    print("Unsatisfiable")#Se não for satisfátivel