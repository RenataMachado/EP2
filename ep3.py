import random

MAX_TENTATIVAS = 6
NUM_LETRAS = 5


def main():
    ' Implementa mecanismo principal do jogo. '   
    # pede opção de lingua
    lingua = input ("Digite 'P' para Português ou 'I' para Inglês:").strip().upper()
    while lingua != 'P' and lingua != 'I':
        lingua = input("Qual o idioma (I para inglês ou P para português)? ")
    
    # carrega lista de palavras do arquivo correspondente
    if lingua == 'P':
        lista_palavras = cria_lista_palavras('portugues.txt')
    elif lingua == 'I':
        lista_palavras = cria_lista_palavras('ingles.txt')


    # sorteia uma palavra da lista
    palavra = normaliza_string(lista_palavras[random.randint(0,len(lista_palavras)-1)])
    
    num_tentativas = 0
    lista_tentativas = []
    ganhou = False
    teclado =  inicializa_teclado()
    

    while num_tentativas < MAX_TENTATIVAS and not ganhou:
        imprime_teclado(teclado)
        
        chute = normaliza_string(input("Digite seu chute: ").lower())
        
        if len(chute) != NUM_LETRAS:
            print(f"Chute deve ter {NUM_LETRAS} letras.")
            continue

        feedback = checa_tentativa(palavra, chute)

        lista_tentativas.append([chute, feedback])
        
        imprime_resultado(lista_tentativas)
        atualiza_teclado(chute, feedback, teclado)

        if chute == palavra:
            ganhou = True
        
        num_tentativas += 1

    if ganhou: 
       print("PARABÉNS!")
    else: 
       print("Que pena... A palavra era",palavra,".")


##### FUNÇÕES PRONTAS #####

def inicializa_teclado():
    '''
    Devolve a lista com as teclas na ordem.
    As letras que aparecem nos chutes e que não estão no teclado são substtuídas por ' '.
    '''
    
    teclado = [['q','w','e','r','t','y','u','i','o','p'],
               ['a','s','d','f','g','h','j','k','l'],
               ['z','x','c','v','b','n','m']]
    return teclado


def imprime_teclado(teclado):
    ''' Exibe o teclado com as letras possiveis. '''   
    print('-----------------------------------------')
    for linha in teclado:
        for letra in linha:
            print(letra, end = ' ')
        print()
    print('-----------------------------------------')


# ##### FUNÇÕES OBRIGATÓRIAS #####


def cria_lista_palavras(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.readlines()
        
        lista_palavras = [linha.strip() for linha in conteudo]
    return lista_palavras


def checa_tentativa(palavra,chute):
    feedback = []
    for i in range(len(chute)):
        if chute[i] == palavra[i]:
            feedback.append('*')  # Letra na posição correta
        elif chute[i] in palavra:
            feedback.append('+')  # Letra na palavra, mas na posição errada
        else:
            feedback.append('_')  # Letra não está na palavra
    return feedback



def  imprime_resultado(lista):
    ''' Recebe a lista de tentativas e imprime as tentativas,
      usando * para verde , + para amarelo e _ para letras que não aparecem na
      palavra sorteada. A lista de tentativas tem formato
      [[chute1, feedback1], [chute2, feedback2], …, [chuten,feedbackn]].
      Esta função não devolve valor. '''
    for tentativa, feedback in lista:
        print(f"{tentativa}: {' '.join(feedback)}")

            

def atualiza_teclado(chute,feedback,teclado):
    ''' Modifica teclado para que as letras marcadas como inexistentes
     no chute sejam substituídas por espaços. Esta função não devolve valor.'''
    for i in range(len(chute)):
        if feedback[i] == '_':
            for linha in teclado:
                for j in range(len(linha)):
                    if linha[j] == chute[i]:
                        linha[j] = ' '

# ##### FUNÇÕES EXTRAS (caso existam) #####
def normaliza_string(s):
    ''' Remove acentos e converte para minúsculas. '''
    a = {'á', 'à', 'ã', 'â'}
    e = {'é', 'ê','è'}
    i= {'í','ì','î'}
    o= {'ò','ò','ô','õ'}
    u={'ú','ù','û'}
    c= {'ç'}
    n= {'ñ'}

    for char in range(len(s)):
        if char in a:
            char = 'a'
        elif char in e:
            char == 'e'
        elif char in i:
            char =='i'
        elif char in o:
            char =='o'
        elif char in u:
            char =='u'
        elif char in c:
            char =='c'
        elif char in n:
            char =='n'
    return s

##### NÃO ALTERE O TRECHO ABAIXO #####
if __name__ == "__main__":
    main()