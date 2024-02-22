class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        total = len(nums1)+len(nums2)
        half = total//2
        if len(B)<len(A):
            B,A=A,B
        l,r = 0,len(A)-1

        while True:
            mid1 = (l+r)//2
            mid2 = half-mid1-2

            Aleft = A[mid1] if mid1>=0 else float("-inf")
            Aright = A[mid1+1] if mid1+1<len(A) else float("inf")
            Bleft = B[mid2] if mid2>=0 else float("-inf")
            Bright = B[mid2+1] if mid2+1<len(B) else float("inf")

            if Aleft<=Bright and Bleft<=Aright:
                if total%2:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+ min(Aright,Bright)) /2


            if Aleft>Bright:
                r = mid1-1
            else:
                l = mid1+1     
        return 0
