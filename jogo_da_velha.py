import os
jogador1 = 0
jogador2 = 0
ganhax = ['x','x','x']
matriz = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
#CONFIGURAÇÕES DO CONTROLE DO 1º JOGADOR
def comandoJogador1():
    if jogador1 == 1:
        matriz[0][0] = 'x'
    if jogador1 == 2:
        matriz[0][1] = 'x'
    if jogador1 == 3:
        matriz[0][2] = 'x'
    if jogador1 == 4:
        matriz[1][0] = 'x'
    if jogador1 == 5:
        matriz[1][1] = 'x'
    if jogador1 == 6:
        matriz[1][2] = 'x'
    if jogador1 == 7:
        matriz[2][0] = 'x'
    if jogador1 == 8:
        matriz[2][1] = 'x'
    if jogador1 == 9:
        matriz[2][2] = 'x'
    
#CONFIGURAÇÕES DO CONTROLE DO 2º JOGADOR
def comandoJogador2():
    if jogador2 == 1:
        matriz[0][0] = 'O'
    if jogador2 == 2:
        matriz[0][1] = 'O'
    if jogador2 == 3:
        matriz[0][2] = 'O'
    if jogador2 == 4:
        matriz[1][0] = 'O'
    if jogador2 == 5:
        matriz[1][1] = 'O'
    if jogador2 == 6:
        matriz[1][2] = 'O'
    if jogador2 == 7:
        matriz[2][0] = 'O'
    if jogador2 == 8:
        matriz[2][1] = 'O'
    if jogador2 == 9:
        matriz[2][2] = 'O'
def tabuleiroVelha():
    print('')
    print(f'                   _{matriz[0][0]}_|_{matriz[0][1]}_|_{matriz[0][2]}_             ')
    print(f'                   _{matriz[1][0]}_|_{matriz[1][1]}_|_{matriz[1][2]}_             ')
    print(f'                    {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]}              ')
    print('')
    
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

while aperte != 1 and aperte != 2 and aperte != 3 and aperte != 4:
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

    print('')
    verdade = True
    while verdade:
        jogador1 = int(input('VEZ DE ( X ): '))
        comandoJogador1()
        tabuleiroVelha()
        for c in range(0,3):
            if matriz[c] == ganhax:
                print(10*'=',  ' ( X ) VENCEU! ',  10*'=')
                verdade = False
                break
        for m in matriz:
            if m[0] == 'x':
                cont += 1
                if cont == 4:
                    print(10*'=',  ' ( X ) VENCEU! ',  10*'=')
                    verdade = False
                    break
        if matriz[0][0] and matriz[1][1] and matriz[2][2] == 'x':
            print('verdade')
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