import numpy as np
import matplotlib.pyplot as plt

k = 8.99 * 10**9  # Coulomb's constant

def electric_field(q, r, x, y):

    r_squared = r**2
    # Calculating the electric field using Coulomb's law
    e_x = (k * q * x) / r_squared
    e_y = (k * q * y) / r_squared
    return e_x, e_y

def plot_electric_field(charges):

    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Ex = np.zeros_like(X)
    Ey = np.zeros_like(Y)
    
    for charge in charges:
        q, qx, qy = charge
        r = np.sqrt((X - qx)**2 + (Y - qy)**2)
        e_x, e_y = electric_field(q, r, X - qx, Y - qy)
        Ex += e_x
        Ey += e_y
    
    plt.streamplot(X, Y, Ex, Ey, density=2, arrowsize=2, color='blue')  
    
    for charge in charges:
        q, qx, qy = charge
        plt.scatter(qx, qy, color='red' if q < 0 else 'blue')  # Negative charges in red, positive in blue
        if q > 0:
            plt.text(qx, qy, f"+{q}", verticalalignment='bottom', horizontalalignment='right', color='blue')
        else:
            plt.text(qx, qy, f"{q}", verticalalignment='top', horizontalalignment='right', color='red')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Electric Field')
    plt.show()

if __name__ == "__main__":
    # Adding electric charges
    # charges = [(1, -2, 0), (-1, 2, 0), (2, 0, 2), (-2, 0, -2)]
    charges = [(-1, -2, 0)]

    plot_electric_field(charges)
