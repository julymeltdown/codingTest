# 백준 14501번
https://www.acmicpc.net/problem/14501
>dp 문제풀이할 때 점화식 만드는게 너무 어렵다..
> 다른분들은 날짜를 역순으로 하여 풀었다는데 나는 그렇게 하면 헷갈릴 것 같아서 그냥 정직하게 첫날부터 풀었다.
> 이 문제의 점화식은 dp[i+x]=max(dp[i-1]+PArr[i],dp[i+x]) 이거다. 아직 좀 어려운 것 같다.