 def minScoreTriangulation(self, A: List[int]) -> int:
        if len(A) == 3:
            return A[0] * A[1] * A[2]
        
        Mylist = []
        for k in range(2,len(A)):
            curprod = A[0]*A[1]*A[k]
            ltriangle = A[1:k+1]
            print(ltriangle)
            
            rtriangle = A[k:]
            rtriangle.append(A[0])
            print(rtriangle)
            
            if len(ltriangle) >= 3:
                curprod += minScoreTriangulation(ltriangle)
            if len(rtriangle) >= 3:
                curprod += minScoreTriangulation(rtriangle)
            Mylist.append(curprod)
            
        Mylist.sort()
        return Mylist[0]
        
 minScoreTriangulation([1,2,3])
