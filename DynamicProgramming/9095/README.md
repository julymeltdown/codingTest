# 백준 9095번
https://www.acmicpc.net/problem/9095
> dp 문제인데 점화식은 혼자 생각해내지 못했다. DP는 어려워잉..
> <br/> 이 문제의 점화식은 dp[i]=dp[i-1]+dp[i-2]+dp[i-3]이다 
> <br/> N==4일 때, 1+(dp[3]을 표현할 수 있는 경우의 수), 2+(dp[2]을 표현할 수 있는 경우의 수),3+(dp[1]을 표현할 수 있는 경우의 수) 이렇게 되는 것을 알 수 있었다.