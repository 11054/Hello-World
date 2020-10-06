
# recursive function


def recursivFib(scope=int(input("insert some number: ")), a=0, b=1, fib_number=0, sum=0):

    fib_number = a + b
    if fib_number > scope:
        return(sum)

    if (fib_number % 2 == 0):
        sum += fib_number

    if (fib_number < scope):

        sum = recursivFib(scope, b, fib_number, fib_number, sum)

    return (sum)


print(recursivFib())
