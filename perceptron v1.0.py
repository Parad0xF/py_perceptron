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
