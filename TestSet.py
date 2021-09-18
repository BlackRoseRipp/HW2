Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==== RESTART: C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py ====
Running unit tests
FF..FFFFFF
======================================================================
FAIL: testEquilateralTriangleB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 30, in testEquilateralTriangleB
    self.assertEqual(classifyTriangle(5,5,9),'Isosceles','5,5,9 should not be equilateral')
AssertionError: 'InvalidInput' != 'Isosceles'
- InvalidInput
+ Isosceles
 : 5,5,9 should not be equilateral

======================================================================
FAIL: testEquilateralTriangles (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 27, in testEquilateralTriangles
    self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
AssertionError: 'InvalidInput' != 'Equilateral'
- InvalidInput
+ Equilateral
 : 1,1,1 should be equilateral

======================================================================
FAIL: testIsoscelesTriangleA (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 39, in testIsoscelesTriangleA
    self.assertEqual(classifyTriangle(3,4,3),'Isosceles','3,4,3 should be isosceles')
AssertionError: 'InvalidInput' != 'Isosceles'
- InvalidInput
+ Isosceles
 : 3,4,3 should be isosceles

======================================================================
FAIL: testIsoscelesTriangleB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 42, in testIsoscelesTriangleB
    self.assertEqual(classifyTriangle(3,3,5),'Isosceles','3,4,3 should be isosceles')
AssertionError: 'InvalidInput' != 'Isosceles'
- InvalidInput
+ Isosceles
 : 3,4,3 should be isosceles

======================================================================
FAIL: testRightTriangleA (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 21, in testRightTriangleA
    self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
AssertionError: 'InvalidInput' != 'Right'
- InvalidInput
+ Right
 : 3,4,5 is a Right triangle

======================================================================
FAIL: testRightTriangleB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 24, in testRightTriangleB
    self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
AssertionError: 'InvalidInput' != 'Right'
- InvalidInput
+ Right
 : 5,3,4 is a Right triangle

======================================================================
FAIL: testScaleneTriangleA (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 33, in testScaleneTriangleA
    self.assertEqual(classifyTriangle(3,4,5),'Scalene','3,4,5 should be scalene')
AssertionError: 'InvalidInput' != 'Scalene'
- InvalidInput
+ Scalene
 : 3,4,5 should be scalene

======================================================================
FAIL: testScaleneTriangleB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 36, in testScaleneTriangleB
    self.assertEqual(classifyTriangle(5,4,3),'Scalene','3,4,3 should not be scalene')
AssertionError: 'InvalidInput' != 'Scalene'
- InvalidInput
+ Scalene
 : 3,4,3 should not be scalene

----------------------------------------------------------------------
Ran 10 tests in 0.019s

FAILED (failures=8)
>>> 
==== RESTART: C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py ====
Running unit tests
FF.FFFFFFF
======================================================================
FAIL: testEquilateralTriangleB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 30, in testEquilateralTriangleB
    self.assertEqual(classifyTriangle(5,5,9),'Isosceles','5,5,9 should not be equilateral')
AssertionError: 'NotATriangle' != 'Isosceles'
- NotATriangle
+ Isosceles
 : 5,5,9 should not be equilateral

======================================================================
FAIL: testEquilateralTriangles (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 27, in testEquilateralTriangles
    self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
AssertionError: 'NotATriangle' != 'Equilateral'
- NotATriangle
+ Equilateral
 : 1,1,1 should be equilateral

======================================================================
FAIL: testInvalidB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 48, in testInvalidB
    self.assertEqual(classifyTriangle(150,150,200),'InvalidInput','A side cannot be greater than 200')
AssertionError: 'NotATriangle' != 'InvalidInput'
- NotATriangle
+ InvalidInput
 : A side cannot be greater than 200

======================================================================
FAIL: testIsoscelesTriangleA (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 39, in testIsoscelesTriangleA
    self.assertEqual(classifyTriangle(3,4,3),'Isosceles','3,4,3 should be isosceles')
AssertionError: 'NotATriangle' != 'Isosceles'
- NotATriangle
+ Isosceles
 : 3,4,3 should be isosceles

======================================================================
FAIL: testIsoscelesTriangleB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 42, in testIsoscelesTriangleB
    self.assertEqual(classifyTriangle(3,3,5),'Isosceles','3,4,3 should be isosceles')
AssertionError: 'NotATriangle' != 'Isosceles'
- NotATriangle
+ Isosceles
 : 3,4,3 should be isosceles

======================================================================
FAIL: testRightTriangleA (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 21, in testRightTriangleA
    self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
AssertionError: 'NotATriangle' != 'Right'
- NotATriangle
+ Right
 : 3,4,5 is a Right triangle

======================================================================
FAIL: testRightTriangleB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 24, in testRightTriangleB
    self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
AssertionError: 'NotATriangle' != 'Right'
- NotATriangle
+ Right
 : 5,3,4 is a Right triangle

======================================================================
FAIL: testScaleneTriangleA (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 33, in testScaleneTriangleA
    self.assertEqual(classifyTriangle(3,4,5),'Scalene','3,4,5 should be scalene')
AssertionError: 'NotATriangle' != 'Scalene'
- NotATriangle
+ Scalene
 : 3,4,5 should be scalene

======================================================================
FAIL: testScaleneTriangleB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 36, in testScaleneTriangleB
    self.assertEqual(classifyTriangle(5,4,3),'Scalene','3,4,3 should not be scalene')
AssertionError: 'NotATriangle' != 'Scalene'
- NotATriangle
+ Scalene
 : 3,4,3 should not be scalene

----------------------------------------------------------------------
Ran 10 tests in 0.021s

FAILED (failures=9)
>>> 
==== RESTART: C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py ====
Running unit tests
F..FFFFF..
======================================================================
FAIL: testEquilateralTriangleB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 30, in testEquilateralTriangleB
    self.assertEqual(classifyTriangle(5,5,9),'Isosceles','5,5,9 should not be equilateral')
AssertionError: 'Equilateral' != 'Isosceles'
- Equilateral
+ Isosceles
 : 5,5,9 should not be equilateral

======================================================================
FAIL: testIsoscelesTriangleA (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 39, in testIsoscelesTriangleA
    self.assertEqual(classifyTriangle(3,4,3),'Isosceles','3,4,3 should be isosceles')
AssertionError: 'Scalene' != 'Isosceles'
- Scalene
+ Isosceles
 : 3,4,3 should be isosceles

======================================================================
FAIL: testIsoscelesTriangleB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 42, in testIsoscelesTriangleB
    self.assertEqual(classifyTriangle(3,3,5),'Isosceles','3,4,3 should be isosceles')
AssertionError: 'Equilateral' != 'Isosceles'
- Equilateral
+ Isosceles
 : 3,4,3 should be isosceles

======================================================================
FAIL: testRightTriangleA (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 21, in testRightTriangleA
    self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
AssertionError: 'Scalene' != 'Right'
- Scalene
+ Right
 : 3,4,5 is a Right triangle

======================================================================
FAIL: testRightTriangleB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 24, in testRightTriangleB
    self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
AssertionError: 'Scalene' != 'Right'
- Scalene
+ Right
 : 5,3,4 is a Right triangle

----------------------------------------------------------------------
Ran 10 tests in 0.016s

FAILED (failures=5)
>>> 
==== RESTART: C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py ====
Running unit tests
F...FFFF..
======================================================================
FAIL: testEquilateralTriangleB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 30, in testEquilateralTriangleB
    self.assertEqual(classifyTriangle(5,5,9),'Isosceles','5,5,9 should not be equilateral')
AssertionError: 'Equilateral' != 'Isosceles'
- Equilateral
+ Isosceles
 : 5,5,9 should not be equilateral

======================================================================
FAIL: testIsoscelesTriangleA (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 39, in testIsoscelesTriangleA
    self.assertEqual(classifyTriangle(3,4,3),'Isosceles','3,4,3 should be isosceles')
AssertionError: 'Scalene' != 'Isosceles'
- Scalene
+ Isosceles
 : 3,4,3 should be isosceles

======================================================================
FAIL: testIsoscelesTriangleB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 42, in testIsoscelesTriangleB
    self.assertEqual(classifyTriangle(3,3,5),'Isosceles','3,4,3 should be isosceles')
AssertionError: 'Equilateral' != 'Isosceles'
- Equilateral
+ Isosceles
 : 3,4,3 should be isosceles

======================================================================
FAIL: testRightTriangleA (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 21, in testRightTriangleA
    self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
AssertionError: 'Scalene' != 'Right'
- Scalene
+ Right
 : 3,4,5 is a Right triangle

======================================================================
FAIL: testRightTriangleB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 24, in testRightTriangleB
    self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
AssertionError: 'Scalene' != 'Right'
- Scalene
+ Right
 : 5,3,4 is a Right triangle

----------------------------------------------------------------------
Ran 10 tests in 0.019s

FAILED (failures=5)
>>> 
==== RESTART: C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py ====
Running unit tests
F...FF.FF.
======================================================================
FAIL: testEquilateralTriangleB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 30, in testEquilateralTriangleB
    self.assertEqual(classifyTriangle(5,5,9),'Isosceles','5,5,9 should not be equilateral')
AssertionError: 'Isoceles' != 'Isosceles'
- Isoceles
+ Isosceles
?    +
 : 5,5,9 should not be equilateral

======================================================================
FAIL: testIsoscelesTriangleA (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 39, in testIsoscelesTriangleA
    self.assertEqual(classifyTriangle(3,4,3),'Isosceles','3,4,3 should be isosceles')
AssertionError: 'Isoceles' != 'Isosceles'
- Isoceles
+ Isosceles
?    +
 : 3,4,3 should be isosceles

======================================================================
FAIL: testIsoscelesTriangleB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 42, in testIsoscelesTriangleB
    self.assertEqual(classifyTriangle(3,3,5),'Isosceles','3,4,3 should be isosceles')
AssertionError: 'Isoceles' != 'Isosceles'
- Isoceles
+ Isosceles
?    +
 : 3,4,3 should be isosceles

======================================================================
FAIL: testRightTriangleB (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 24, in testRightTriangleB
    self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
AssertionError: 'Scalene' != 'Right'
- Scalene
+ Right
 : 5,3,4 is a Right triangle

======================================================================
FAIL: testScaleneTriangleA (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py", line 33, in testScaleneTriangleA
    self.assertEqual(classifyTriangle(3,4,5),'Scalene','3,4,5 should be scalene')
AssertionError: 'Right' != 'Scalene'
- Right
+ Scalene
 : 3,4,5 should be scalene

----------------------------------------------------------------------
Ran 10 tests in 0.011s

FAILED (failures=5)
>>> 
==== RESTART: C:\Users\Owner\Desktop\Stevens\SSW-567\HW2\TestTriangle.py ====
Running unit tests
..........
----------------------------------------------------------------------
Ran 10 tests in 0.032s

OK
>>> 
