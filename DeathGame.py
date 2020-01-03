def surviv(a,k):
  def getrem(b,k):
    if k%len(b)>len(b):
      getrem(k%len(b),len(b))

    elif k%len(b) == 0:
      return len(b)
    else:
      return k%len(b)
  while len(a) != 1:
    if len(a) >= k:
      a.pop(k-1)
      a = a[k-1:]+a[:k-1]
      #print(a)
    else:
      t = getrem(a,k)
      a.pop(t-1)
      a = a[t-1:]+a[:t-1]
      #print(a)
  return (a[0])

T = int(input())
for i in range(T):
    arr = list(input().split())
    arr = list(map(int,arr))
    a = [j for j in range(1,arr[0]+1)]
    k = arr[1]
    print(surviv(a,k))