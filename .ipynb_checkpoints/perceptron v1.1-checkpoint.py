# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run
import random
import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection

random.seed(7)
LEARNING_RATE = 0.1
index_list = [0,1,2,3]

x_train = [(1.0,-1.0,-1.0), (1,-1.0,1.0), (1.0,1.0,-1.0), (1.0,1.0,1.0)]
y_train = [1.0,1.0,1.0,-1,0]

w = [0.2, -0.6, 0.25]


def show_learning(w):
    print('w0 =', '%5.2f' % w[0] ,', w1=', '%5.2f' % w[1], ', w2=', '%5.2f' % w[2])
    
    
    fig, ax = plt.subplots()
    ax.plot(w[0], w[1])
    
    


def perceptron(w, x):
    z = 0.0
    for i in range(len(w)):
       z += w[i] * x[i]
    if z < 0:
        return -1
    else:
        return 1

all_correct = False
while not all_correct:
    all_correct = True
    random.shuffle(index_list)
    
    for i in index_list:
        x = x_train[i]
        y = y_train[i]
        
        p_out = perceptron(w, x)
        
        if y!= p_out:
            for j in range(0, len(w)):
                w[j] += (y* LEARNING_RATE * x[j])
                all_correct = False
                show_learning(w)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',title='About as simple as it gets, folks')
ax.grid()
plt.show()


"""
def get_input():
    row_size = 3
    column_size = 2
    #input_list = [[float(input("Enter the data:")) for _ in range(row_size)] for _ in range(column_size)]
    input_list = [0.9,-0.6,-0.5],[1,1,1]
    for i in range(len(input_list)):
        for _ in range(len(input_list[0])):
            input_list[i][_] = float(input_list[i][_])
    return input_list
    
    
    
def perceptron(input_list):
    x = []
    z = 0.0
    for row in range(len(input_list[0])):
        for col in range(len(input_list)):
           x.append(input_list[col][row])
           
    for i, element in zip(x[1::2], x[::2]):
       z += i*element
       
    if z < 0:
        return -1
    else:
        return 1
        
print(perceptron(get_input()))
"""
