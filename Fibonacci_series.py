def generate_fib_series(num):
    num=int(num)

    series=[0,1]

    if num <= 0:
        return []
    if num == 1:
        return [0]
    if num == 2:
        return series
    
    while num > len(series):
        series.append(series[-1]+series[-2])
    
    return series[-1]
    # return series


if __name__ == "__main__":
    # input_num=input("Enter the number of elements in the Fibonacci series: ")
    # print(generate_fib_series(input_num))
    n=input("Enter the value of n: ")
    print(generate_fib_series(n))

# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)

# if __name__ == "__main__":
#     print(fib(10))


