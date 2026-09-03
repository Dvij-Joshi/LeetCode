class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = 0
        maxCount = 0  

        for right in range(len(s)):
            freq[s[right]] += 1
            maxCount = max(maxCount, freq[s[right]])
            
            if (right - left + 1) - maxCount > k:
                freq[s[left]] -= 1
                left += 1

        return len(s) - left

                