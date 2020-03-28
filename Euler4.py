'''
Largest palindrome product
   
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''
answer = -1
for i in range(100, 1000):
    for j in range(100, 1000):
        r = i * j
        rev =''.join(reversed(str(r)))
        if rev == str(r) and r > answer:
            answer = r
     
print(answer)
