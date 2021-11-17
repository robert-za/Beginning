If we assume that the integers are stored with 32 bits, the bitwise image of the two variables will be as follows:

i: 00000000000000000000000000001111
j: 00000000000000000000000000010110

The assignment is given:

log = i and j


We are dealing with a logical conjunction here. Let's trace the course of the calculations. Both variables i and j are not zeros, so will be deemed to represent True. Consulting the truth table for the and operator, we can see that the result will be True. No other operations are performed.

log: True

Now the bitwise operation - here it is:

bit = i & j


The & operator will operate with each pair of corresponding bits separately, producing the values of the relevant bits of the result. Therefore, the result will be as follows:

i	00000000000000000000000000001111
j	00000000000000000000000000010110
bit = i & j	00000000000000000000000000000110
These bits correspond to the integer value of six.



Let's look at the negation operators now. First the logical one:

logneg = not i


The logneg variable will be set to False - nothing more needs to be done.

The bitwise negation goes like this:

bitneg = ~i


It may be a bit surprising: the bitneg variable value is -16. This may seem strange, but isn't at all. If you wish to learn more, you should check out the binary numeral system and the rules governing two's complement numbers.

i	00000000000000000000000000001111
bitneg = ~i	11111111111111111111111111110000
Each of these two-argument operators can be used in abbreviated form. These are the examples of their equivalent notations:

x = x & y	x &= y
x = x | y	x |= y
x = x ^ y	x ^= y

0001$0
0010$1
0101$4
0110$5
0011$2
0100$3


0111$6

Answers:
0000 0000 0000 0000 0000 0000 0000 0000%
1111 1111 1111 1111 1111 1111 1111 0111%
1111 1111 1111 1111 1111 1111 1111 1010%
0000 0000 0000 0000 0000 0000 0000 0100%
0000 0000 0000 0000 0000 0000 0000 0001%
0000 0000 0000 0000 0000 0000 0001 0100%
