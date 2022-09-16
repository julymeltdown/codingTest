import sys

N, M = map(int, sys.stdin.readline().split())

site = dict()

for i in range(N):
    siteDomain, password = sys.stdin.readline().split()
    site[siteDomain] = password

for i in range(M):
    siteToFind = sys.stdin.readline().rstrip()
    print(site.get(siteToFind))
