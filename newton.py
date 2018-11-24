'''newton.py

Implementation of a Newton-Raphson root-finder.

'''

import numpy as np
import functions as F


class Newton(object):
    """Newton objects have a solve() method for finding roots of f(x)
    using Newton's method. x and f can both be vector-valued.

    """
    
    def __init__(self, f, tol=1.e-6, maxiter=20, dx=1.e-6, maxradius=200):
        """Parameters:
        
        f: the function whose roots we seek. Can be scalar- or
        vector-valued. If the latter, must return an object of the
        same "shape" as its input x

        tol, maxiter: iterate until ||f(x)|| < tol or until you
        perform maxiter iterations, whichever happens first

        dx: step size for computing approximate Jacobian

        """
        self._f = f
        self._tol = tol
        self._maxiter = maxiter
        self._dx = dx
        self._maxradius = maxradius

    def solve(self, x0):
        """Determine a solution of f(x) = 0, using Newton's method, starting
        from initial guess x0. x0 must be scalar or 1D-array-like. If
        x0 is scalar, return a scalar result; if x0 is 1D, return a 1D
        numpy array.

        """
        # NOTE: no need to check whether x0 is scalar or vector. All
        # the functions/methods invoked inside solve() return "the
        # right thing" when x0 is scalar.
        print('new test')
        x = x0
        for i in range(self._maxiter):
            fx = self._f(x)
            print(x)
            # linalg.norm works fine on scalar inputs
            if np.linalg.norm(fx) < self._tol:
                return x

            x = self.step(x, fx)
#            print('This is x after the step \n {0}'.format(x))
#            if type(x) == customException:
#                return x
            if type(x) == singularException:
                return x
            if np.linalg.norm(x - x0) > self._maxradius:
                return radiusException('The guess is to far from the answer. Try a different guess.')
 #       print('this is np.linalg.norm \n {0}'.format(np.linalg.norm(fx)))
        if np.linalg.norm(fx) > self._tol:
            s = "This answer is not accurate, there were not enough interations"
            return(x, s)
        return x

            

    def step(self, x, fx=None):
        """Take a single step of a Newton method, starting from x. If the
        argument fx is provided, assumes fx = f(x).

        """

        
        if fx is None:
            fx = self._f(x)

        Df_x = F.approximateJacobian(self._f, x, self._dx)

        # linalg.solve(A,B) returns the matrix solution to AX = B, so
        # it gives (A^{-1}) B. np.matrix() promotes scalars to 1x1
        # matrices.

 #       if np.isscalar(x):
 #           if Df_x ==0:
 #               return customException("The starting guess is not good. Try again with a different guess")
 #       else:
 #           if np.linalg.cond(Df_x) > 1/sys.float_info.epsilon:
 #               return customException("The starting guess is not good. Try again with a different guess")
        
        try:
            
            h = np.linalg.solve(np.matrix(Df_x), np.matrix(fx))
            
        except np.linalg.LinAlgError as err:
            return singularException("The starting guess is not good. Try again with a different guess")   
        # Suppose x was a scalar. At this point, h is a 1x1 matrix. If
        # we want to return a scalar value for our next guess, we need
        # to re-scalarize h before combining it with our previous
        # x. The function np.asscalar() will act on a numpy array or
        # matrix that has only a single data element inside and return
        # that element as a scalar.
        if np.isscalar(x):
            h = np.asscalar(h)
    
        return x - h

     
class customException(Exception):
    pass

class radiusException(customException):
    pass
class singularException(customException):
    pass