""" for i in range(2**16+1):
    # преобразовать 10-чную в 2-чную сс
    # проверить длину полученной строки (0b.0000...) вырезать 0b. и добавить нули слева до len(str) == 8
    # разложить поэлементно строку на массив
    # np.reshape 4x4
    # посчитать энергию конфигурации """

import numpy as np

energies = []
def En_calc(S):
    summ = 0
    for i in range(len(S)):
        for j in range(len(S)-1):
                summ+=S[i][j]*S[i][j+1]+S.T[i][j]*S.T[i][j+1]
        summ+=S[i][0]*S[i][len(S)-1]+S.T[i][0]*S.T[i][len(S.T)-1]
    return -summ

for i in range(2**16):
    binary = bin(i)[2:].zfill(16)
    spins = np.array([1 if bit == '1' else -1 for bit in binary])
    S = spins.reshape(4, 4)
    energies.append(En_calc(S))

print(energies)