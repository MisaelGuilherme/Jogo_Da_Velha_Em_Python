import os
jogador1 = 0
jogador2 = 0
quemJoga = 1
vezesJogar = 0
maxTent = 9
ganhaX = ['x','x','x']
ganhaO = ['O','O','O']                
m = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

#CONFIGURAÇÕES DO CONTROLE DO 1º JOGADOR

def comandoJogador1():
    global vezesJogar
    global quemJoga
    if quemJoga == 1 and vezesJogar < maxTent:
        jogador1 = int(input('VEZ DE ( X ): '))
        if m[0][0] == ' ' and jogador1 == 1:
            m[0][0] = 'x'
        if m[0][1] == ' ' and jogador1 == 2:
            m[0][1] = 'x'
        if m[0][2] == ' ' and jogador1 == 3:
            m[0][2] = 'x'
        if m[1][0] == ' ' and jogador1 == 4:
            m[1][0] = 'x'
        if m[1][1] == ' ' and jogador1 == 5:
            m[1][1] = 'x'
        if m[1][2] == ' ' and jogador1 == 6:
            m[1][2] = 'x'
        if m[2][0] == ' ' and jogador1 == 7:
            m[2][0] = 'x'
        if m[2][1] == ' ' and jogador1 == 8:
            m[2][1] = 'x'
        if m[2][2] == ' ' and jogador1 == 9:
            m[2][2] = 'x'
        quemJoga = 2
        vezesJogar += 1

#CONFIGURAÇÕES DO CONTROLE DO 2º JOGADOR
def comandoJogador2():
    global vezesJogar
    global quemJoga
    if quemJoga == 2 and vezesJogar < maxTent:
        jogador2 = int(input('VEZ DE ( O ): '))
        if m[0][0] == ' ' and jogador2 == 1:
            m[0][0] = 'O'
        if m[0][1] == ' ' and jogador2 == 2:
            m[0][1] = 'O'
        if m[0][2] == ' ' and jogador2 == 3:
            m[0][2] = 'O'
        if m[1][0] == ' ' and jogador2 == 4:
            m[1][0] = 'O'
        if m[1][1] == ' ' and jogador2 == 5:
            m[1][1] = 'O'
        if m[1][2] == ' ' and jogador2 == 6:
            m[1][2] = 'O'
        if m[2][0] == ' ' and jogador2 == 7:
            m[2][0] = 'O'
        if m[2][1] == ' ' and jogador2 == 8:
            m[2][1] = 'O'
        if m[2][2] == ' ' and jogador2 == 9:
            m[2][2] = 'O'
        quemJoga = 1
        vezesJogar += 1

def tabuleiroVelha():
    print('')
    print(f'                   _{m[0][0]}_|_{m[0][1]}_|_{m[0][2]}_             ')
    print(f'                   _{m[1][0]}_|_{m[1][1]}_|_{m[1][2]}_             ')
    print(f'                    {m[2][0]} | {m[2][1]} | {m[2][2]}              ')
    print('')
    
def verificaGanhador():
    ganhaX
    ganhaO
    somaX = 0
    somaO = 0
    vitoria = 0
    #--------NÃO MEXER
    for c in range(0,3):
        if m[c] == ganhaX:
            print('VENCEU X')
            vitoria = 1    
        if m[c] == ganhaO:
            print('VENCEU O')
            vitoria = 1
    for d in m:
        if d[jogador1] == 'x':
            somaX += 1
            if somaX == 3:
                print('ok X')
                vitoria = 1
                break
    for e in m:
        if e[jogador2] == 'O':
            somaO += 1
            if somaO == 3:
                print('ok O')
                vitoria = 1
                break
    return vitoria
#---------------------

#=====================================================================================    
            
print(50*'=')
print('')
print('===============   JOGO DA VELHA   ================')
print('')
print('   APERTE: ')
print('           [1]  INICIAR PARTIDA')
print('           [2]  COMO JOGAR')
print('           [3]  CRÉDITOS')
print('           [4]  SAIR')
print('')
aperte = int(input('   DIGITE: '))

while aperte < 1 or aperte > 4:
    print('ERROR, VALOR NÃO ACEITO TENTE DE NOVO!')
    print('')
    aperte = int(input('DIGITE: '))
    
if aperte == 1:
    os.system('cls')
    cruz = 0
    bola = 0
    empate = 0
    
    print('===============   PLACAR DO JOGO   ===============')
    print('')
    print(f'       O => {bola}          X         x => {cruz}')
    print('                                              ')
    print(f'      EMPATE: {empate}                       ')
    print('==============================================')
    print('')
    cont = 0
    tabuleiroVelha()
    print('')
    while True:
        comandoJogador1()
        tabuleiroVelha()
        vit = verificaGanhador()
        if vit == 1:
            break
        comandoJogador2()
        tabuleiroVelha()
        vit = verificaGanhador()
        if vit == 1:
            break
    
    ''' 
        if matriz[0][0] and matriz[1][0] and matriz[2][0] == 'x':
            print(10*'=',  ' ( X ) VENCEU! ',  10*'=')
        if matriz[0][1] and matriz[1][1] and matriz[2][1] == 'x':
            print(10*'=',  ' ( X ) VENCEU! ',  10*'=')
        if matriz[0][2] and matriz[1][2] and matriz[2][2] == 'x':
            print(10*'=',  ' ( X ) VENCEU! ',  10*'=')'''
    '''
    #=====================================================================================        
        
            jogador2 = int(input('2º JOGADOR: '))
            comandoJogador2()
            tabuleiroVelha()'''
        

if aperte == 2:
    print('')
    print('COMO JOGAR: ')
    print('''
    O 1º JOGADOR INICIARÁ COM X, PARA ESCOLHER O CAMPO EM QUE DESEJA JOGAR
    DIGITE O NÚMERO REFERENCIADO AO MESMO. O TEBULEIRO POSSUI 9 CAMPOS.
                                                                
                                    _1_|_2_|_3_                 
                                    _4_|_5_|_6_                 
                                     7 | 8 | 9                      ''')
    
if aperte == 3:
    print('')
    print('CRÉDITOS:')
    print('')
    print('PROGRAMADOR: MISAEL JESUS')
    print('RA: 2010816155')
    print('UNIFBV WYDEN')
    print('EMAIL: misaellleite2002@gmai.com')

if aperte == 4:
    os.system('cls')
    os.system('exit')

    '''for i in range(0,3):
        print(i)
    if matriz[0][0] and matriz[1][1] and matriz[2][2]:
        print('VENCEDOR')'''