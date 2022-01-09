
'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).


Constraint: 0<= N <= 30

Sample Input:
Testcase T
Input N

3
2
7
13

Sample Output:
1
13
233

'''



import sys


def fib(n,dp):
	if n <=1 :
		dp[n] = n
	else:
		if dp[n]== None:
			dp[n] = fib(n-1,dp)+ fib(n-2,dp)
	return dp[n]


sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

testcase = int(input())
for _ in range(0,testcase):
	n = int(input())
	dp = [None]*30
	ans = fib(n,dp)
	print(ans)



