class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)
        def get_next(i):
            return (i + nums[i]) % n
        for i in range(n):
            if nums[i] == 0:
                continue
            slow = i
            fast = i
            is_forward = nums[i] > 0
            while True:
                slow = get_next(slow)
                if (nums[slow] > 0) != is_forward or nums[slow] == 0:
                    break
                fast = get_next(fast)
                if (nums[fast] > 0) != is_forward or nums[fast] == 0:
                    break                
                fast = get_next(fast)
                if (nums[fast] > 0) != is_forward or nums[fast] == 0:
                    break
                if slow == fast:
                    if slow == get_next(slow):
                        break
                    return True
            slow = i
            val = nums[i]
            while (nums[slow] > 0) == (val > 0) and nums[slow] != 0:
                nxt = get_next(slow)
                nums[slow] = 0
                slow = nxt

        return False