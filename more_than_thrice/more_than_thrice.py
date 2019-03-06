#
# CS1010X --- Programming Methodology
#
# Mission 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###########
# Task 1a #
###########

def compose(f, g):
    return lambda x:f(g(x))

def thrice(f):
    return compose(f, compose(f, f))

def repeated(f, n):
    if n == 0:
        return identity
    else:
        return compose(f, repeated(f, n - 1))

# Your answer here:
# n =9

###########
# Task 1b #
###########

identity = lambda x: x
add1 = lambda x: x + 1
sq = lambda x: x**2

# (i) print(thrice(thrice)(add1)(6))
# Explanation:output is 33 because thrice(thrice) will do thrice(thrice(thrice(f(x)))) and f(x)=add(x).Also let thrice(f(x)) be t.Then thrice(t) is t(t(t)).also
# thrice(t(t(t)))will be t(t(t)) 9 times. and thrice(f(x)) 9 times will be 27 times of f(x).so therefore it is equivalent repeated(add1,27)(6)

# (ii) print(thrice(thrice)(identity)(compose))
# Explanation:it is equivalent to thrice(thrice(thrice(compose(f,g)))) but in thrice function when we do compose(f,f) then it returns f(f(x)),but compose is 2 value
# input function and f takes only one value so it should throw an error when some value is tested. 

# (iii) print(thrice(thrice)(sq)(1))
# Explanation:as above explained it is equivalent to repeated(sq,27)(1) that is 1.

# (iv) print(thrice(thrice)(sq)(2))
# Explanation:as above explained it is equivalent to repeated(sq,27)(2) that is 2 the power 2*2*2*2*2.... upto 27. therefore answer is 2^(2^27)

###########
# Task 2a #
###########

def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
    return result

def smiley_sum(t):
    def f(x):
        if x==1:
            return 1
        else:
            return (x**2)*2
    def op(x, y):
        return x+y
    n  =t+1

    # Do not modify this return statement
    return combine(f, op, n)

###########
# Task 2b #
###########

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def new_fib(n):
    def f(x):
        if x==1:
            return 1
        if x==2:
            return 1
    def op(x, y):
        return x+y
    def combine(f, op ,n):
        for i in range(1,n):
            if(i==1):
                d=f(1)
                result=f(1)
            elif(i==2):
                m=f(2)
                result=f(2)
            else:
                result=op(d,m)
                d=op(result,-d)
                m=result
        return result


    return combine(f, op, n+1)

# Your answer here:
#here i have a confusion that can i make another function combine as i was not able to get the desired result using the given combine function.if not,then the problem iscoming in my case i
#i am not able to make use combine function given 
