import matlab.engine
import numpy as np
from math import sqrt
from statistics import median
import matplotlib.pyplot as plt
import threading

note_poz=[]
line_h=[]


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
                if note_poz[i,1] > note_poz[j,1]:
                    to_del[i]=None
                else:
                    to_del[j]=None

    note_poz = np.delete(note_poz, list(to_del), 0)


def get_lines_poz(eng, name):
    global line_h
    line_h = np.array(eng.ao_pieciolinia(name))


if __name__=='__main__':
    eng_n = matlab.engine.start_matlab()
    eng_p = matlab.engine.start_matlab()

    s = eng_n.genpath('wspolczynniki_morf')
    eng_n.addpath(s, nargout=0)

    s = eng_p.genpath('wspolczynniki_morf')
    eng_p.addpath(s, nargout=0)

    plik = 'nuty.jpg'

    t1 = threading.Thread(target=get_notes_poz, args=(eng_n, plik))
    t2 = threading.Thread(target=get_lines_poz, args=(eng_p, plik))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Pozycja nut:\n', note_poz, '\n')
    print('Pozycja pieciolini:\n', line_h)