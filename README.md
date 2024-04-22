# CMSE318Assignment3_Parser_Application

We are given the following grammar for generating arithmetic expressions.

G1:

G -> E

E -> E + T | E - T | T

T -> T * F | T / F | F

F -> ( E ) | M | N

M -> a | b | c | d 

N -> 0 | 1 | 2 | 3

This grammar is not suitable for topdown recursive descent parsing because of 
left recursion. 

Removing left recursion, we get the grammar G2:

G2:

G -> E

E -> T R

R -> + T R | - T R | ε

T -> F S

S -> * F S | / F S | ε

F -> ( E ) | M | N 

M -> a | b | c | d

N -> 0 | 1 | 2 | 3

"ε" means the empty production, i.e. if T ε ->, then T can derive the empty string.

Write parser program (based on the pseudo-code given above) in Python to parse 
expressions as defined by the grammar above. The input should be in a file. You should 
have global variables error (of type Boolean), and next_token (of type char). Define a 
function lex() that gets the next character from the file and places it inside next_token. lex()
should skip any white spaces, such as newlines or the space character. The function 
unconusmed_input() should return the remaining input in the file. The last character in the 
file should always be $. Define functions (hint: class methods) G(), E(), R(), T(), F() and N(). 
In the main() function, open the file containing the expression and call G().
