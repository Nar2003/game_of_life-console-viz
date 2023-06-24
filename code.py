"""game of life (console mode)
    In : None (because map is generizing random)
    Out : 10 fps(can be modificated) game of life on console
    Enjoy:)
"""
import numpy as np
import time
from scipy.signal import convolve2d
# import itertools

#%%
PLAYGROUND_SIZE = (32,30)
# PLAYGROUND = np.random.random(PLAYGROUND_SIZE)
PLAYGROUND = np.random.randint(0, 2, size=PLAYGROUND_SIZE)
# print(PLAYGROUND) #window of game

# for _ in range(PLAYGROUND_SIZE[0] * 3) :

def die_or_alive_codex(playground = PLAYGROUND):
    """rules of game (can be modificate to)

    In:
        playground (ndarray, map of game): actually frame.

    Out:
        None
    """
    # print(convolve2d(playground,np.ones((3,3),dtype=int),'same') - playground) #test
    # print(playground) #test

    sum_matrix = convolve2d(playground,np.ones((3,3),dtype=int),'same') - playground
    for x in range(PLAYGROUND_SIZE[0]):
        for y in range(PLAYGROUND_SIZE[1]):
            # print(playground[x,y]) #test
            if playground[x,y] >= 1: # bit is live
                if sum_matrix[x,y] >= 2 and sum_matrix[x,y] <= 3: #classic rules of game (can be modificate)
                    playground[x,y] = 1 # bit is most be live
                else:
                    playground[x,y] = 0 #bit is dead
            else: # bit is dead
                if sum_matrix[x,y] == 3 :
                    playground[x,y] = 1
                else:
                    playground[x,y] = 0
    # print('\n\n\n')
    # print(playground)
    print('\n\n\n\n\n\n\n\n' + str(playground)\
        .replace('[','')\
            .replace(' ','')\
                .replace(']','')\
                    .replace('1','O')\
                        .replace('0',' ')
        ) # module for refracturing list to pixel graphics
# print(die_or_alive_codex()) #test
#%%

close_time = time.time()
first_time = time.time()
while True:
    if close_time - first_time < 1/10:  #module for controling fps
        time.sleep(close_time - first_time)
    first_time = close_time
    die_or_alive_codex() # game
    close_time = time.time()

# %%
