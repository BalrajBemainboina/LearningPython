
def Search(List,N):
    for i in List:
        if N == i:
            return True, List.index(i)

    return False,None


List = [5,6,7,8,2,4]
N = 45
res,pos = Search(List,N)
if res:
    print('FOund at',pos)
else:
    print('Not found')

