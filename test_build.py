
import sys
from fibonacci_build import fib_dynamic
from fibonacci_build import fib_iterative
from fibonacci_build import fib_recursive

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

test(fib_recursive(0))
test(fib_dynamic(1))
test(fib_iterative(8))
    
