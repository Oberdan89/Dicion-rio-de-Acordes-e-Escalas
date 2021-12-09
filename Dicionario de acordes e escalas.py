print('------------------------------- Dicionário de Escalas e acordes -------------------------------')
print('')
tom = str(input('Escolha um tom (C, C#,D, D#, E, F, F#, G, G#, A, A#, B): ').upper())
escala = int(input('Escolha uma escala\n[1] Maior Natural\n[2] Menor Natural\n[3] Menor Harmônica\n[4] Menor melódica\n[5] Ver todas ao mesmo tempo:\n ').upper())

notas = ('C', 'C#' , 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C')
escala_maior = (0, 2, 4, 5, 7, 9, 11, 12)
escala_menor = (0, 2, 3, 5, 7, 8, 10, 12)
menor_harm = (0, 2, 3, 5, 7, 8, 11, 12)
menor_mel = (0, 2, 3, 5, 7, 9, 11, 12)
ch_maior = ('7M', 'm7', 'm7', '7M', '7', 'm7', 'm7(b5)')
ch_menor = ('m7', 'm7(b5)', '7M', 'm7', 'm7', '7M', '7')
ch_harm = ('m7M', 'm7(b5)', '7M(#5)', 'm7', '7', '7M', 'º')
ch_mel = ('m7M', 'm7', '7M(#5)', '7', '7', 'm7(b5)', 'm7(b5)')

i = 0
if escala == 1:
    for c in range(0, len(notas)):
        if tom == notas[i]:
            print('A escala maior natural de {} é:'.format(tom))
            print(notas[i + escala_maior[0]], notas[i+escala_maior[1]], notas[i+escala_maior[2]], notas[i++ escala_maior[3]], notas[i+escala_maior[4]], notas[i+escala_maior[5]], notas[i+escala_maior[6]], notas[i+ escala_maior[7]])
            print('---------------------------------------------------')
            print('O campo harmônico maior natural de {} é:'.format(tom))
            print(notas[i + escala_maior[0]]+ch_maior[0], notas[i+escala_maior[1]]+ch_maior[1], notas[i+escala_maior[2]]+ch_maior[2], notas[i+escala_maior[3]]+ch_maior[3], notas[i+escala_maior[4]]+ch_maior[4], notas[i+escala_maior[5]]+ch_maior[5], notas[i+escala_maior[6]]+ch_maior[6])
            break
        else:
            i += 1
if escala == 2:
    for c in range(0, len(notas)):
        if tom == notas[i]:
            print('A escala menor natural de {} é:'.format(tom))
            print(notas[i+escala_menor[0]], notas[i+escala_menor[1]], notas[i+escala_menor[2]], notas[i+escala_menor[3]], notas[i+escala_menor[4]], notas[i+escala_menor[5]], notas[i+escala_menor[6]], notas[i+escala_menor[7]])
            print('---------------------------------------------------')
            print('O campo harmônico menor natural de {} é:'.format(tom))
            print(notas[i+escala_menor[0]]+ch_menor[0], notas[i+escala_menor[1]]+ch_menor[1], notas[i+escala_menor[2]]+ch_menor[2], notas[i+escala_menor[3]]+ch_menor[3], notas[i+escala_menor[4]]+ch_menor[4], notas[i+escala_menor[5]]+ch_menor[5], notas[i+escala_menor[6]]+ch_menor[6])
            break
        else:
            i += 1
if escala == 3:
    for c in range(0, len(notas)):
        if tom == notas[i]:
            print('A escala menor harmônica de {} é:'.format(tom))
            print(notas[i+menor_harm[0]], notas[i+menor_harm[1]], notas[i+menor_harm[2]], notas[i+menor_harm[3]], notas[i+menor_harm[4]], notas[i+menor_harm[5]], notas[i+menor_harm[6]], notas[i+menor_harm[7]])
            print('---------------------------------------------------')
            print('O campo harmônico menor harmônico de {} é:'.format(tom))
            print(notas[i+menor_harm[0]]+ch_harm[0], notas[i+menor_harm[1]]+ch_harm[1], notas[i+menor_harm[2]]+ch_harm[2], notas[i+menor_harm[3]]+ch_harm[3], notas[i+menor_harm[4]]+ch_harm[4], notas[i+menor_harm[5]]+ch_harm[5], notas[i+menor_harm[6]]+ch_harm[6])
            break
        else:
            i += 1
if escala == 4:
    for c in range(0, len(notas)):
        if tom == notas[i]:
            print('A escala menor melódica de {} é:'.format(tom))
            print(notas[i+menor_mel[0]], notas[i+menor_mel[1]], notas[i+menor_mel[2]], notas[i+menor_mel[3]], notas[i+menor_mel[4]], notas[i+menor_mel[5]], notas[i+menor_mel[6]], notas[i+menor_mel[7]])
            print('---------------------------------------------------')
            print('O campo harmônico menor melódica de {} é:'.format(tom))
            print(notas[i+menor_mel[0]]+ch_mel[0], notas[i+menor_mel[1]]+ch_mel[1], notas[i+menor_mel[2]]+ch_mel[2], notas[i+menor_mel[3]]+ch_mel[3], notas[i+menor_mel[4]]+ch_mel[4], notas[i+menor_mel[5]]+ch_mel[5], notas[i+menor_mel[6]]+ch_mel[6])
            break
        else:
            i += 1
if escala == 5:
    for c in range(0, len(notas)):
        if tom == notas[i]:
            print('As 4 escalas de {} são: '.format(tom))
            print('Escala maior natural:'+ notas[i + escala_maior[0]], notas[i+escala_maior[1]], notas[i+escala_maior[2]], notas[i++ escala_maior[3]], notas[i+escala_maior[4]], notas[i+escala_maior[5]], notas[i+escala_maior[6]], notas[i+ escala_maior[7]])
            print('Escala menor natural:'+ notas[i+escala_menor[0]], notas[i+escala_menor[1]], notas[i+escala_menor[2]], notas[i+escala_menor[3]], notas[i+escala_menor[4]], notas[i+escala_menor[5]], notas[i+escala_menor[6]], notas[i+escala_menor[7]])
            print('Escala menor harmonica:'+ notas[i+menor_harm[0]], notas[i+menor_harm[1]], notas[i+menor_harm[2]], notas[i+menor_harm[3]], notas[i+menor_harm[4]], notas[i+menor_harm[5]], notas[i+menor_harm[6]], notas[i+menor_harm[7]])
            print('Escala menor melódica:'+notas[i+menor_mel[0]], notas[i+menor_mel[1]], notas[i+menor_mel[2]], notas[i+menor_mel[3]], notas[i+menor_mel[4]], notas[i+menor_mel[5]], notas[i+menor_mel[6]], notas[i+menor_mel[7]])
            print('---------------------------------------------------')
            print('As 4 campos harmônicos de {} são: '.format(tom))
            print('Campo harmônico maior natural:' + notas[i + escala_maior[0]]+ch_maior[0], notas[i+escala_maior[1]]+ch_maior[1], notas[i+escala_maior[2]]+ch_maior[2], notas[i+escala_maior[3]]+ch_maior[3], notas[i+escala_maior[4]]+ch_maior[4], notas[i+escala_maior[5]]+ch_maior[5], notas[i+escala_maior[6]]+ch_maior[6])
            print('Campo harmônico menor natural:' + notas[i+escala_menor[0]]+ch_menor[0], notas[i+escala_menor[1]]+ch_menor[1], notas[i+escala_menor[2]]+ch_menor[2], notas[i+escala_menor[3]]+ch_menor[3], notas[i+escala_menor[4]]+ch_menor[4], notas[i+escala_menor[5]]+ch_menor[5], notas[i+escala_menor[6]]+ch_menor[6])
            print('Campo harmônico menor harmônico:' + notas[i+menor_harm[0]]+ch_harm[0], notas[i+menor_harm[1]]+ch_harm[1], notas[i+menor_harm[2]]+ch_harm[2], notas[i+menor_harm[3]]+ch_harm[3], notas[i+menor_harm[4]]+ch_harm[4], notas[i+menor_harm[5]]+ch_harm[5], notas[i+menor_harm[6]]+ch_harm[6])
            print('Campo harmônico menor melódico:' + notas[i+menor_mel[0]]+ch_mel[0], notas[i+menor_mel[1]]+ch_mel[1], notas[i+menor_mel[2]]+ch_mel[2], notas[i+menor_mel[3]]+ch_mel[3], notas[i+menor_mel[4]]+ch_mel[4], notas[i+menor_mel[5]]+ch_mel[5], notas[i+menor_mel[6]]+ch_mel[6])
            break
        else:
            i += 1
