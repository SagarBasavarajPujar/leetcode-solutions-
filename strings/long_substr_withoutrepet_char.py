
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[l])
                l += 1

            res.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len


# User input
s = input("Enter a string: ")

# Create object and call function
obj = Solution()
result = obj.lengthOfLongestSubstring(s)

print("Length of longest substring without repeating characters:", result)

