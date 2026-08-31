class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array=[]
        n1=len(nums1)
        n2=len(nums2)
        left=0
        right=0
        while left<n1 or right<n2:
            if right==n2:
                merged_array.append(nums1[left])
                left+=1
            elif left==n1:
                merged_array.append(nums2[right])
                right+=1
            else:
                if(nums1[left]<nums2[right]):
                    merged_array.append(nums1[left])
                    left+=1
                else:
                    merged_array.append(nums2[right])
                    right+=1
        print(merged_array)
        n3=len(merged_array)
        if n3%2==0:
            median=(merged_array[((n3)//2)-1]+merged_array[(((n3)//2)-1)+1])/2
            return median
        else:
            temp=merged_array[(n3-1)//2]
            return temp
