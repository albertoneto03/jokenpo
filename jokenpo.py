import pygame
from random import choice

pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):
    vitoria=[]
    derrota=[]
    empate=[]
    print('{:=^40}'.format( 'PEDRA, PAPEL OU TESOURA'))
    print('Escolha sua jogada:')
    print(' [ 0 ] PEDRA')
    print(' [ 1 ] PAPEL')
    print(' [ 2 ] TESOURA')
    print(' [ 3 ] SAIR')
    while True:
        jogador = ['PEDRA', 'PAPEL', 'TESOURA']
        jogada = int(input('Qual e a sua jogada?: '))
        if jogada == 3:
            break
        while jogada < 0 or jogada > 2:
            print('\033[1;30;41mOPCAO INVALIDA. INSIRA OPCAO ENTRE 0 E 3\033[m')
            print('{:=^40}'.format( 'PEDRA, PAPEL OU TESOURA'))
            print('Escolha sua jogada:')
            print(' [ 0 ] PEDRA')
            print(' [ 1 ] PAPEL')
            print(' [ 2 ] TESOURA')
            print(' [ 3 ] SAIR')
            jogador = ['PEDRA', 'PAPEL', 'TESOURA','SAIR']
            jogada = int(input('Qual e a sua jogada?: '))
        nome = jogador[jogada]
        pc = ['PEDRA', 'PAPEL', 'TESOURA']
        escolhido = pc.index(choice(pc))
        nome_pc = pc[escolhido]
        if escolhido == jogada:
            msg = 'EMPATE! JOGUE NOVAMENTE'
            empate.append(jogada)
        elif (escolhido == 0 and jogada == 2) or (escolhido == 2and jogada == 1) or (escolhido == 1  and jogada == 0):
            msg = 'COMPUTADOR GANHA! VOCÊ \033[7;31mPERDEU\033[m'
            derrota.append(jogada)
        else:
            msg = 'VOCÊ \033[7;30mGANHOU\033[m !! PARABENS!'
            vitoria.append(jogada)
        print('-='*20)
        print('Sua Jogada: \033[4;36m{}\033[m'.format(nome))
        print('*'*40)
        print('Jogada do Computador: \033[4;33m{}\033[m'.format(nome_pc))
        print('-='*20)
        print(msg)
    break
print('Você ganhou:',len(vitoria),'partida(s)')
print('Você perdeu:',len(derrota),'partida(s)')
print('Você empatou:',len(empate),'partida(s)')
