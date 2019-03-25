def Search(List,N):
    lower_bound = 0
    upper_bound = len(List)-1
    print ('Something')
    while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound) // 2
            if List[mid] == N:
                return True, mid
            else:
                if List[mid] < N:
                    lower_bound = mid+1
                else:
                    upper_bound = mid-1
    return False,None


List = [5,6,7,8,2,4]
N = 45
res,pos = Search(List,N)
if res:
    print('Found at',pos)
else:
    print('Not found')
