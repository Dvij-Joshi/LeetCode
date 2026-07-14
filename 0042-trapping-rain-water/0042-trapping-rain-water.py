class Solution:
    def trap(self, height: List[int]) -> int:
        r=1
        l=0
        container=0
        array_max=max(height)
        max_index = height.index(array_max)
        while r <=max_index:
            if height[r]<height[l]:
                container=container+(height[l]-height[r])
                r+=1
            else:
                l=r
                r+=1
        r=len(height)-1
        l=r-1
        while l>=max_index:
            if height[l]>=height[r]:
                r=l
                l-=1
            else:
                container=container+(height[r]-height[l])
                l-=1

        return container
