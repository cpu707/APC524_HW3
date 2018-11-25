#!/usr/bin/env python3

import unittest
import numpy as np
import math
import newton
import sys

class Test1DNewton(unittest.TestCase):
    def testLinear(self):
        # Just so you see it at least once, this is the lambda keyword
        # in Python, which allows you to create anonymous functions
        # "on the fly". As I commented in testFunctions.py, you can
        # define regular functions inside other
        # functions/methods. lambda expressions are just syntactic
        # sugar for that.  In other words, the line below is
        # *completely equivalent* under the hood to:
        #
        # def f(x):
        #     return 3.0*x + 6.0
        #
        # No difference.
        f = lambda x : 3.0*x + 6.0

        # Setting maxiter to 2 b/c we're guessing the actual root
        solver = newton.Newton(f, tol=1.e-15, maxiter=2)
        x = solver.solve(-2.0)
        # Equality should be exact if we supply *the* root, ergo
        # assertEqual rather than assertAlmostEqual
        self.assertEqual(x, -2.0)
        
        
    def testQuadratic(self):

        f = lambda x : -3.0*x**2 + 6.0

        solver = newton.Newton(f, tol=2.e-15, maxiter=20)
        x = solver.solve(2)

        self.assertAlmostEqual(x, math.sqrt(2))

    def testQuadraticWithRadius(self):

        f = lambda x : -3.0*x**2 + 6.0

        solver = newton.Newton(f, tol=2.e-15, maxiter=20, maxradius = 5)
        x = solver.solve(50)

        self.assertRaises(radiusException)


    def testQuadraticBadGuess(self):

        f = lambda x : -3.0*x**2 + 6.0

        solver = newton.Newton(f, tol=2.e-15, maxiter=20)
        x = solver.solve(0)

        self.assertRaises(customException)


    def testQuadraticNoAnswer(self):

        f = lambda x : 3.0*x**2 + 6.0

        solver = newton.Newton(f, tol=2.e-15, maxiter=20)
        (x,s) = solver.solve(1)

        self.assertEqual(s,"This answer is not accurate, there were not enough iterations")

class Test2DNewton(unittest.TestCase):

    def testLinear2(self):
        initialGuess = np.matrix([[2.5],[1.5]])
        def f(x):
            return np.matrix([[3.0*(float(x[0])) + 6.0],[2.0*(float(x[1])) + 2]])
 #       print("This is f \n {0}".format(f))
        solver = newton.Newton(f, tol=2.e-15, maxiter=20)
        x = solver.solve(initialGuess)

        self.assertEqual(x[0], -2)
        self.assertEqual(x[1], -1)
        
    def testLinear2(self):
        initialGuess = np.matrix([[2.5],[1.5]])
        def f(x):
            return np.matrix([[3.0*(float(x[0])) + 6.0],[2.0*(float(x[0])) + 2]])
 #       print("This is f \n {0}".format(f))
        solver = newton.Newton(f, tol=2.e-15, maxiter=20)
        x = solver.solve(initialGuess)

        self.assertRaises(singularException)


    def test2D(self):
        initialGuess = np.matrix([[2.5],[1.5]])
        def f(x):
            return np.matrix([[3.0*(float(x[0])) +float(x[1])+ 6.0],[2.0*(float(x[1])) + float(x[0])+ 2]])
 #       print("This is f \n {0}".format(f))
        solver = newton.Newton(f, tol=2.e-15, maxiter=20)
        x = solver.solve(initialGuess)

        self.assertEqual(x[0], -2)
        self.assertEqual(np.around(x[1], 10), 0)

if __name__ == "__main__":
    unittest.main()

    
