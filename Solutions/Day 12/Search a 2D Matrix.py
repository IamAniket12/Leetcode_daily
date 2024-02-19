class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom = 0,len(matrix)-1
        row=-1

        while top<=bottom:
            mid = (top+bottom)//2
            print(mid)
            if matrix[mid][0]<=target and matrix[mid][-1]>=target:
                row=mid
                break
            elif matrix[mid][0]>target:
                bottom = mid-1
            else:
                top = mid+1       
        if row==-1:
            return False

        start=0
        end=len(matrix[0])-1
        while start<=end:
            mid = (start+end)//2
            if matrix[row][mid]==target:
                return True  
            elif matrix[row][mid]<target:
                start+=1
            else:
                end-=1
        return False                  


        