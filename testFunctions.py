#!/usr/bin/env python3

import unittest
import numpy as np
import numpy.testing as npt
import math

import functions as F

class Test1DFunctions(unittest.TestCase):
   
 #scalar tests
    
    def test_ApproxJacobian1(self):
        slope = 3.0
        # Yes, you can define a function inside a function/method. And
        # it has scope only within the method within which it's
        # defined (unless you return it to the outside world, which
        # you can do in Python with no need for anything like C's
        # malloc() or C++'s new() )
        def f(x):
            return slope * x + 5.0

        x0 = 2.0
        dx = 1.e-3
        Df_x = F.approximateJacobian(f, x0, dx)
        # self.assertEqual(Df_x.shape, (1,1)
        # If x and f are scalar-valued, Df_x should be, too
        self.assertTrue(np.isscalar(Df_x))
        self.assertAlmostEqual(Df_x, slope)

    def test_ApproxJacobian1a(self):
        #test for large numbers
        slope = 300000000.0
        def f(x):
            return slope * x + 5000000.0

        x0 = 2.0
        dx = 1.e-3
        Df_x = F.approximateJacobian(f, x0, dx)

        self.assertTrue(np.isscalar(Df_x))
        self.assertAlmostEqual(Df_x, slope)
        
        
    def test_ApproxJacobian1b(self):
        #test for second degree polynomials
        slope = 3.0
        quadratic = F.Polynomial([slope,slope,slope])
        def f(x):
            return quadratic(x)
        x0 = 2.0
        dx = 1.e-7
        Df_x = F.approximateJacobian(f, x0, dx)

        self.assertTrue(np.isscalar(Df_x))
        self.assertAlmostEqual(Df_x, 15)

    def test_ApproxJacobian1bb(self):
        #test for second degree polynomials
        slope = 3.0
        quadratic = F.Polynomial([6,0,slope])
        def f(x):
            return quadratic(x)
        x0 = 0
        dx = 1.e-7
        Df_x = F.approximateJacobian(f, x0, dx)

        self.assertTrue(np.isscalar(Df_x))
        self.assertAlmostEqual(Df_x, 0)

    def test_ApproxJacobian1c(self):
        #test for second degree polynomials, different x0
        slope = 3.0
        quadratic = F.Polynomial([slope,slope,slope])
        def f(x):
            return quadratic(x)
        x0 = 0
        dx = 1.e-007
        Df_x = F.approximateJacobian(f, x0, dx)

        self.assertTrue(np.isscalar(Df_x))
        self.assertAlmostEqual(Df_x, 3)

    def test_ApproxJacobian1d(self):
        #test for trig function
        slope = 3.0
        def f(x):
            return math.sin(x)
        x0 = math.pi
        dx = 1.e-003
        Df_x = F.approximateJacobian(f, x0, dx)

        self.assertTrue(np.isscalar(Df_x))
        self.assertAlmostEqual(Df_x, -1)

    def test_ApproxJacobian1e(self):
        #test for exponential function
        slope = 3.0
        def f(x):
            return math.e**x
        x0 = 1
        dx = 1.e-005
        Df_x = F.approximateJacobian(f, x0, dx)

        self.assertTrue(np.isscalar(Df_x))
        self.assertAlmostEqual(Df_x, math.e)

#nonscalar tests

class Test2DFunctions(unittest.TestCase):

    def test_ApproxJacobian2(self):
        # numpy matrices can also be initialized with strings. The
        # semicolon separates rows; spaces (or commas) delimit entries
        # within a row.
        A = np.matrix([[1.0, 2.0], [3.0, 4.0]])

        def f(x):
            # The * operator for numpy matrices is overloaded to mean
            # matrix-multiplication, rather than elementwise
            # multiplication as it does for numpy arrays
            return A * x

        # The vector-valued function f defined above is the following:
        # if we let u = f(x), then
        #
        # u1 = x1 + 2 x2
        # u2 = 3 x1 + 4 x2
        #
        # The Jacobian of this function is constant and exactly equal
        # to the matrix A. approximateJacobian should thus return
        # something pretty close to A.

        x0 = np.matrix([[5.0], [6.0]])
        dx = 1.e-6
        Df_x = F.approximateJacobian(f, x0, dx)

        # Make sure approximateJA
        self.assertEqual(Df_x.shape, (2,2))
        # numpy arrays and matrices vectorize comparisons. So if a & b
        # are arrays, the expression a==b will itself be an array of
        # booleans. But an array of booleans does not itself evaluate
        # to a clean boolean (this is an exception to the general
        # Python rule that "every object can be interpreted as a
        # boolean"), so normal assert statements will break. We need
        # array-specific assert statements found in numpy.testing
        npt.assert_array_almost_equal(Df_x, A)

    def test_ApproxJacobian2a(self):
        A = np.matrix([[10,0],[0,21]])
        poly1 = F.Polynomial([2,2,2])
        poly2 = F.Polynomial([3,3,3])
        def f(x):
            return np.matrix([[poly1(float(x[0]))],[poly2(float(x[1]))]])
  #      print('This is f(x)\n {0}'.format(f(x)))
        x0 = np.matrix([[2.0],[3.0]])
        dx = 1.e-6
        Df_x = F.approximateJacobian(f, x0, dx)

 #       print('This is Df_x\n {0}'.format(Df_x))
        self.assertEqual(len(Df_x), 2)
        npt.assert_array_almost_equal(Df_x, A)

    def test_ApproxJacobian2b(self):
        A = np.matrix([[8,2],[36,3]])

        def f(x):
            
            return np.matrix([[2*(float(x[0]))**2+2*(float(x[1]))],[3*(float(x[0]))**3+ 3*(float(x[1]))]])

        x0 = np.matrix([[2.0] , [3.0]])
        dx = 1.e-6
        Df_x = F.approximateJacobian(f, x0, dx)

        self.assertEqual(len(Df_x), 2)
        npt.assert_array_almost_equal(Df_x, A)

class miscTests(unittest.TestCase):

    def test_Polynomial(self):
        # p(x) = x^2 + 5x + 4
        p = F.Polynomial([4, 5, 1])
        # linspace(a, b, N) produces N equally spaced values from a to
        # b, including both a & b.
        for x in np.linspace(-2,2,11):
            self.assertAlmostEqual(p(x), 4 + 5*x + x**2)
        
        # It would have been more Pythonic to feed the whole array x into p
        # (the way the Polynomial class is written, it's agnostic
        # about whether x is a scalar or an array) and compare with an
        # npt assertion, as follows:
        #
        # p = F.Polynomial([4, 5, 1])
        # npt.assert_array_almost_equal(p(x), 4 + 5*x + x**2)
        #
        # But I though this would be more legible.

if __name__ == '__main__':
    unittest.main()



