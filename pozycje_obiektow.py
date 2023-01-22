import matlab.engine
import numpy as np
from math import sqrt
from statistics import median
import threading

note_poz=[]
line_h=[]

line_5=[]
notes_on_line=[]



def get_notes_poz(eng, name):
    global note_poz
    note_poz = np.array(eng.ao_nuty(name))
    # print(note_poz)
    # print(note_poz[0])


    to_del={}

    for i in range(len(note_poz)):
        for j in range(i+1, len(note_poz)):
            tmp = note_poz[i]-note_poz[j]
            
            if sqrt(tmp[0]**2 + tmp[1]**2) < 30:
                if note_poz[i,1] < note_poz[j,1]:
                    to_del[i]=None
                else:
                    to_del[j]=None

    note_poz = np.delete(note_poz, list(to_del), 0)


def get_lines_poz(eng, name):
    global line_h
    line_h = np.array(eng.ao_pieciolinia(name))

def generate_notes(name):
    eng_n = matlab.engine.start_matlab()
    eng_p = matlab.engine.start_matlab()

    s = eng_n.genpath('wspolczynniki_morf')
    eng_n.addpath(s, nargout=0)

    s = eng_p.genpath('wspolczynniki_morf')
    eng_p.addpath(s, nargout=0)

    name = 'nuty1.jpg'

    t1 = threading.Thread(target=get_notes_poz, args=(eng_n, name))
    t2 = threading.Thread(target=get_lines_poz, args=(eng_p, name))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # sortowanie pieciolinii
    line_h.sort()
    # sortowanie wzgledem wysokosci nut
    sorted_notes = np.argsort(note_poz[:, 1])
    note_poz = note_poz[sorted_notes]
    # print(len(note_poz))
    # print('Pozycja nut:\n', note_poz, '\n')
    # print('Pozycja pieciolini:\n', line_h)

    # dodawanie linii w piecioliniach
    line_h = np.array(line_h).flatten()
    for i in range(0, len(line_h), 5):
        if i % 5 == 0:
            line_5.append(line_h[i:i + 5].tolist())

    # dodawanie nut do pieciolinii
    # print('Pieciolinie posortowane:\n', line_5, '\n')
    it = 0
    for j in line_5:
        notes2=[]
        for i in note_poz:
            dist = (j[-1] - j[1]) / 4
            if (i[1] >= j[0]) and (i[1] <= j[-1] + 4 * dist):
                notes2.append(list(i))
                it += 1
        notes_on_line.append(notes2)

    # print('Nuty na pięcioliniach:\n', notes_on_line)
    # print('Ilosc nut: ', it ,'\n')
    # sortowanie nut w piecioliniach
    for i in range(len(notes_on_line)):
        notes_on_line[i] = sorted(notes_on_line[i], key=lambda x: x[0])

    # print('Nuty na pięcioliniach posortowane:\n', notes_on_line)
    tune=[]
    for i in notes_on_line:
        notes_in_line=[]
        for j in i:
            for k in line_5:
                if len(k)<5:
                    continue
                # print(k)
                dist = (k[-1] - k[0]) / 4
                d = (dist - 4) / 2
                # print(dist)
                if k[0]+d >= j[1] >= k[0]-d:
                    # print(j, ' 1')
                    notes_in_line.append('F^')
                elif k[1]+d >= j[1] >= k[1]-d:
                    # print(j, ' 2')
                    notes_in_line.append('D^')
                elif k[2]+d >= j[1] >= k[2]-d:
                    # print(j, ' 3')
                    notes_in_line.append('H')
                elif k[3]+d >= j[1] >= k[3]-d:
                    # print(j, ' 4')
                    notes_in_line.append('G')
                elif k[4]+d >= j[1] >= k[4]-d:
                    # print(j, ' 5')
                    notes_in_line.append('E')
                elif k[4]+dist-d <= j[1] <= k[4]+d+dist:
                    # print(j, ' 6')
                    notes_in_line.append('C')
                elif k[0]+d <= j[1] <= k[1]-d:
                    # print(j, '1 2')
                    notes_in_line.append('E^')
                elif k[1]+d <= j[1] <= k[2]-d:
                    # print(j, '2 3')
                    notes_in_line.append('C^')
                elif k[2]+d <= j[1] <= k[3]-d:
                    # print(j, '3 4')
                    notes_in_line.append('A')
                elif k[3]+d <= j[1] <= k[4]-d:
                    # print(j, '4 5')
                    notes_in_line.append('F')
                elif k[4]+d <= j[1] <= k[4]-d+dist:
                    # print(j, '5 6')
                    notes_in_line.append('D')
                elif k[4]+d+dist <= j[1] <= k[4]-d+2*dist:
                    # print(j, '6+')
                    notes_in_line.append('H_')
        tune.append(notes_in_line)
    return tune


if __name__=='__main__':
    # eng_n = matlab.engine.start_matlab()
    # eng_p = matlab.engine.start_matlab()

    # s = eng_n.genpath('wspolczynniki_morf')
    # eng_n.addpath(s, nargout=0)

    # s = eng_p.genpath('wspolczynniki_morf')
    # eng_p.addpath(s, nargout=0)

    # name = 'nuty1.jpg'

    # t1 = threading.Thread(target=get_notes_poz, args=(eng_n, name))
    # t2 = threading.Thread(target=get_lines_poz, args=(eng_p, name))
    
    # t1.start()
    # t2.start()

    # t1.join()
    # t2.join()

    # # sortowanie pieciolinii
    # line_h.sort()
    # # sortowanie wzgledem wysokosci nut
    # sorted_notes = np.argsort(note_poz[:, 1])
    # note_poz = note_poz[sorted_notes]
    # # print(len(note_poz))
    # # print('Pozycja nut:\n', note_poz, '\n')
    # # print('Pozycja pieciolini:\n', line_h)

    # # dodawanie linii w piecioliniach
    # line_h = np.array(line_h).flatten()
    # for i in range(0, len(line_h), 5):
    #     if i % 5 == 0:
    #         line_5.append(line_h[i:i + 5].tolist())

    # # dodawanie nut do pieciolinii
    # # print('Pieciolinie posortowane:\n', line_5, '\n')
    # it = 0
    # for j in line_5:
    #     notes2=[]
    #     for i in note_poz:
    #         dist = (j[-1] - j[1]) / 4
    #         if (i[1] >= j[0]) and (i[1] <= j[-1] + 4 * dist):
    #             notes2.append(list(i))
    #             it += 1
    #     notes_on_line.append(notes2)

    # # print('Nuty na pięcioliniach:\n', notes_on_line)
    # # print('Ilosc nut: ', it ,'\n')
    # # sortowanie nut w piecioliniach
    # for i in range(len(notes_on_line)):
    #     notes_on_line[i] = sorted(notes_on_line[i], key=lambda x: x[0])

    # # print('Nuty na pięcioliniach posortowane:\n', notes_on_line)
    # tune=[]
    # for i in notes_on_line:
    #     notes_in_line=[]
    #     for j in i:
    #         for k in line_5:
    #             if len(k)<5:
    #                 continue
    #             # print(k)
    #             dist = (k[-1] - k[0]) / 4
    #             d = (dist - 4) / 2
    #             # print(dist)
    #             if k[0]+d >= j[1] >= k[0]-d:
    #                 # print(j, ' 1')
    #                 notes_in_line.append('F^')
    #             elif k[1]+d >= j[1] >= k[1]-d:
    #                 # print(j, ' 2')
    #                 notes_in_line.append('D^')
    #             elif k[2]+d >= j[1] >= k[2]-d:
    #                 # print(j, ' 3')
    #                 notes_in_line.append('H')
    #             elif k[3]+d >= j[1] >= k[3]-d:
    #                 # print(j, ' 4')
    #                 notes_in_line.append('G')
    #             elif k[4]+d >= j[1] >= k[4]-d:
    #                 # print(j, ' 5')
    #                 notes_in_line.append('E')
    #             elif k[4]+dist-d <= j[1] <= k[4]+d+dist:
    #                 # print(j, ' 6')
    #                 notes_in_line.append('C')
    #             elif k[0]+d <= j[1] <= k[1]-d:
    #                 # print(j, '1 2')
    #                 notes_in_line.append('E^')
    #             elif k[1]+d <= j[1] <= k[2]-d:
    #                 # print(j, '2 3')
    #                 notes_in_line.append('C^')
    #             elif k[2]+d <= j[1] <= k[3]-d:
    #                 # print(j, '3 4')
    #                 notes_in_line.append('A')
    #             elif k[3]+d <= j[1] <= k[4]-d:
    #                 # print(j, '4 5')
    #                 notes_in_line.append('F')
    #             elif k[4]+d <= j[1] <= k[4]-d+dist:
    #                 # print(j, '5 6')
    #                 notes_in_line.append('D')
    #             elif k[4]+d+dist <= j[1] <= k[4]-d+2*dist:
    #                 # print(j, '6+')
    #                 notes_in_line.append('H_')
    #     tune.append(notes_in_line)

    # print('Nuty na piecioliniach:\n', tune, '\n')

