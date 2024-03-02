import numpy as np
X = [0.5,2.5]
Y = [0.2,0.9]

def f(w,b,x):
    return 1.0 / (1.0 + np.exp(-(w*x + b)))

def error(w,b):
    err = 0
    for x,y in Zip(X,Y):
        fx = f(w,b,x)
        err += 0.5 * (fx-y)**2
    return err

def grad_b(w,b,x,y):
    fx = f(w,b,x)
    return (fx-y)*fx*(1-fx)

def grad_w(w,b,x,y):
    fx = f(w,b,x)
    return (fx-y)*fx*(1-fx)*w

import matplotlib.pyplot as plt

# Assuming X, Y, grad_w, and grad_b are defined elsewhere

def do_grad_descent():
    w, b, eta, max_epochs = -2, -2, 1.0, 100
    w_values, b_values = [],  []  # Lists to store values for plotting

    for i in range(max_epochs):
        print(f"At epochs {i}")
        dw, db = 0, 0
        for x, y in zip(X, Y):
            dw += grad_w(w, b, x, y)
            db += grad_b(w, b, x, y)
        w = w - eta * dw
        b = b - eta * db

        w_values.append(w)
        b_values.append(b)

        print(f"weight:{w}, bias:{b}")
        print("==================================")

    # Plotting
    plt.plot(range(max_epochs), w_values, label='Weight (w)')
    plt.plot(range(max_epochs), b_values, label='Bias (b)')
    plt.xlabel('Epochs')
    plt.ylabel('Values')
    plt.legend()
    plt.show()


do_grad_descent()


