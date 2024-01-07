"""
Using the first three lines of the input file we get this system of 9 equations with 9 unknowns.
 
x + a * t = 380596900441035 - 141 * t
y + b * t = 475034410013298 - 244 * t
z + c * t = 238677466991589 + 154 * t
x + a * s = 233796913851006 + 54 * s
y + b * s = 262774170759556 + 10 * s
z + c * s = 265925724673108 + 23 * s
x + a * r = 276006064958748 + 14 * r
y + b * r = 296055609314709 + 21 * r
z + c * r = 391999646036593 + 24 * r

Using https://quickmath.com/webMathematica3/quickmath/equations/solve/advanced.jsp to solve (LOL) gives:
x = 229429688799267
y = 217160931330282
z = 133453231437025
a = 63
b = 104
c = 296
t = 741015743342
s = 485247227971
r = 950538288969
"""

print(229429688799267 + 217160931330282 + 133453231437025)
