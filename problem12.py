def factorial(num):
    l = [1, num]
    for i in xrange(2, num/2 + 1, 1):
        if num % i == 0:
            l.append(i)
            l.append(num/i)
    return len(set(l))

def triangle_factor():
    sum = 0
    for i in xrange(1, 99999999999999, 1):
        sum += i
        print sum
        if factorial(sum) > 100:
            return sum
        
if __name__ == '__main__':
    print triangle_factor()
