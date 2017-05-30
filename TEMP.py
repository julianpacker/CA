class S():
    def __init__(self,n):
        self.l = [(1 + n), (2+n), (3+n)]

NS = [S(1), S(4)]
a = list(map(sum, zip(*(NS[i].l for i in range(2)))))
print (a)
