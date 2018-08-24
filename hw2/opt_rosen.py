import scipy.optimize
import numpy as np
import random


def rosen_fun(ls):
    """
    implement the Rosenbrock function (n=3)
    :param ls: a list with three elements (n=3)
    :return: the value of the function
    """
    x1,x2,x3 = ls
    result = 100*(x2-x1**2)**2+(1-x1)**2+100*(x3-x2**2)**2+(1-x2)**2
    return result

def rosen_gradient(ls):
    """
    get the gradient of Rosenbrock function (n=3)
    :param ls: a list with three elements (n=3)
    :return: an array of the gradients of the Rosenbrock function
    """
    x1,x2,x3 = ls
    gradient_x1 = -400*(x2-x1**2)*x1-2*(1-x1)
    gradient_x2 = -400*(x3-x2**2)*x2-2*(1-x2)+200*(x2-x1**2)
    gradient_x3 = 200*(x3-x2**2)
    return np.array([gradient_x1, gradient_x2,gradient_x3])

if __name__ == "__main__":
    obj_value = []
    resol = []

    for i in range(100):
        start_point = [random.uniform(-30, 30) for k in range(3)]
        result = scipy.optimize.minimize(rosen_fun, start_point, method="BFGS", jac = rosen_gradient)
        resol.append(result.x)
        obj_value.append(result.fun)

    opt_value = obj_value[0]
    opt_resol = resol[0]
    for i in range(1, len(obj_value)):
        if obj_value[i] < opt_value:
            opt_value = obj_value[i]
            opt_sol = resol[i]

    print("The optimal solution is: ",opt_sol)
    print("The optimal value is: ", opt_value)
