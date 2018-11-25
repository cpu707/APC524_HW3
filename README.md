# APC524_HW3
HW 3 for APC 524

This program uses the Newton-Raphson method to find roots of a function. To use it, the user must specify and store the parameters of the Newton method,. The following line shows the correct syntax:
        
       solver = newton.Newton(f, Df =g,dx=1.e-6,tol=2.e-15, maxiter=20, maxradius = 5)   
       
Where f is the function you wish to find the root of, Df is the derivative of f, dx is the step size of x, tol is how much tolerance the answer has, maxiter is the maximum number of iterations the method will implement, and maxradius is the maximum difference from the original guess that the method is allowed to reach. All inputs are optional except for f. 

Default values for the optional parameters are:

       Df=0, tol=1.e-6, maxiter=20, dx=1.e-6, maxradius=200

After specifying the parameters, the user can then input their initial guess and solve for the root. The following line shows the correct syntax:

       x = solver.solve(2)
       
Where the 2 is the initial guess and solver is the variable holding the parameters previously indicated. 

Newton.py is capable of solving for functions with or without provided the derivative of target function. If a derivative of the function is not provided, the jacobian of the original function will be used to approximate a derivative. 

Newton.py provide bounds for the root the user is looking for. The user can specify a specific radius around their intitial guess by changing maxradius.
