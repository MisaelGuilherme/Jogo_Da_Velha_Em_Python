'''
Programador: Misael Jesus
Data: 10/02/2002
email: misaelleite2002@gmail.com
'''
import os
jogador1 = 0
jogador2 = 0
quemJoga = 1
vezesJogar = 0
maxTent = 10
ganhaX = ['x','x','x']
ganhaO = ['O','O','O']                
m = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

#========================= CONFIGURAÇÕES DO CONTROLE DO 1º JOGADOR ==========================

def comandoJogador1():
    global vezesJogar
    global quemJoga
    if quemJoga == 1 and vezesJogar < maxTent:
        try:
            jogador1 = int(input('VEZ DE ( X ): '))
        except:
            print('ERROR: VALOR DIGITADO NÃO RECONHECIDO!')
        else:
            while jogador1 < 1 or jogador1 > 9:
                print('ERROR: DIGITE UM NÚMERO VÁLIDO PARA O TABULEIRO!')
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
        
#========================= CONFIGURAÇÕES DO CONTROLE DO 2º JOGADOR ==========================

def comandoJogador2():
    global vezesJogar
    global quemJoga
    if quemJoga == 2 and vezesJogar <= maxTent:
        try:
            jogador2 = int(input('VEZ DE ( O ): '))
        except:
            print('ERROR: VALOR DIGITADO NÃO RECONHECIDO!')
        else:
            while jogador2 < 1 or jogador2 > 9:
                print('ERROR: DIGITE UM NÚMERO VÁLIDO PARA O TABULEIRO!')
                jogador2 = int(input('VEZ DE ( X ): '))
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
    
    #========================= VITÓRIA NA HORIZONTAL ==========================
    
    for c in range(0,3):
        if m[c] == ganhaX:
            print(10*'=',  ' VENCEU! | X |',  10*'=')
            vitoria = 1    
            break
        if m[c] == ganhaO:
            print(10*'=',  ' VENCEU! | O |',  10*'=')
            vitoria = 1
            break
    
    #========================= VITÓRIA NA VERTICAL ==========================
    
    for d in m:
        if m[0][0] == 'x' and m[1][0] == 'x' and m[2][0] == 'x':
            print(10*'=',  ' VENCEU! | X |',  10*'=')
            vitoria = 1
            break
        if m[0][1] == 'x' and m[1][1] == 'x' and m[2][1] == 'x':
            print(10*'=',  ' VENCEU! | X |',  10*'=')
            vitoria = 1
            break
        if m[0][2] == 'x' and m[1][2] == 'x' and m[2][2] == 'x':
            print(10*'=',  ' VENCEU! | X |',  10*'=')
            vitoria = 1
            break
    for e in m:
        if m[0][0] == 'O' and m[1][0] == 'O' and m[2][0] == 'O':
            print(10*'=',  ' VENCEU! | O |',  10*'=')
            vitoria = 1
            break
        if m[0][1] == 'O' and m[1][1] == 'O' and m[2][1] == 'O':
            print(10*'=',  ' VENCEU! | O |',  10*'=')
            vitoria = 1
            break
        if m[0][2] == 'O' and m[1][2] == 'O' and m[2][2] == 'O':
            print(10*'=',  ' VENCEU! | O |',  10*'=')
            vitoria = 1
            break
    
    #========================= VITÓRIA NA DIAGONAL ==========================
    
    for i in m:
        if m[0][0] == 'x' and m[1][1] == 'x' and m[2][2] == 'x':
            print(10*'=',  ' VENCEU! | X |',  10*'=')
            vitoria = 1
            break
    for i in m:
        if m[0][2] == 'x' and m[1][1] == 'x' and m[2][0] == 'x':
            print(10*'=',  ' VENCEU! | X |',  10*'=')
            vitoria = 1
            break
    for l in m:
        if m[0][0] == 'O' and m[1][1] == 'O' and m[2][1] == 'O':
            print(10*'=',  ' VENCEU! | O |',  10*'=')
            vitoria = 1
            break
    for i in m:
        if m[0][2] == 'O' and m[1][1] == 'O' and m[2][0] == 'O':
            print(10*'=',  ' VENCEU! | O |',  10*'=')
            vitoria = 1
            break
    return vitoria

#========================= MENU DO JOGO ==========================   

def menu_jogo():
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

    #========================= ESCOLHA 1 DO JOGO - INICIAR PARTIDA ==========================

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
            if vezesJogar == 9:
                print('EMPATE X . O')
                break
            comandoJogador2()
            tabuleiroVelha()
            vit = verificaGanhador()
            if vit == 1:
                break
            if vezesJogar == 9:
                print('EMPATE X . O')
                break
        
    #========================= ESCOLHA 2 DO JOGO - COMO JOGAR ==========================

    if aperte == 2:
        print('')
        print('COMO JOGAR: ')
        print('''
        O 1º JOGADOR INICIARÁ COM X, PARA ESCOLHER O CAMPO EM QUE DESEJA JOGAR
        DIGITE O NÚMERO REFERENCIADO AO MESMO. O TEBULEIRO POSSUI 9 CAMPOS.
                                                                    
                                        _1_|_2_|_3_                 
                                        _4_|_5_|_6_                 
                                        7 | 8 | 9                      ''')
        
        voltar = int(input('Voltar ao Menu? Sim[1] Não[0] : '))
        if voltar == 1:
            menu_jogo()
        
    #========================= ESCOLHA 3 DO JOGO - CRÉDITOS ==========================

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

menu_jogo()