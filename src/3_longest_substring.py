import time

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """Brute Force Approach
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        if s.strip() == "":
            return 1

        max_length = 0
        str_length = len(s)

        for i in range(str_length):
            for j in range(i, str_length):
                substring = s[i:j + 1]
                prev_length_of_substring = len(substring)
                post_length_of_substring = len(set(substring))
                if prev_length_of_substring == post_length_of_substring:
                    if len(substring) > max_length:
                        max_length = len(substring)
        return max_length
    
    def betterLengthOfLongestSubstring(self, s):
        """Moving Window Approach

        :type s: str
        :rtype: int
        """
        max_length = 0
        left = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length


 

if __name__ == "__main__":
    solution = Solution()
    
    st_1 = time.time()
    result = solution.lengthOfLongestSubstring("tmmzuxt")
    print(f"| {2 * '-'} {result} {2 * '-'} |")
    result = solution.lengthOfLongestSubstring("p")
    print(f"| {2 * '-'} {result} {2 * '-'} |")
    result = solution.lengthOfLongestSubstring("")
    print(f"| {2 * '-'} {result} {2 * '-'} |")
    result = solution.lengthOfLongestSubstring(" ")
    print(f"| {2 * '-'} {result} {2 * '-'} |")
    result = solution.lengthOfLongestSubstring("      ")
    print(f"| {2 * '-'} {result} {2 * '-'} |")
    ed_1 = time.time()
    print(f"Time taken: {ed_1 - st_1}")

    st_2 = time.time()
    result = solution.betterLengthOfLongestSubstring("tmmzuxt")
    print(f"| {2 * '-'} {result} {2 * '-'} |")
    result = solution.betterLengthOfLongestSubstring("p")
    print(f"| {2 * '-'} {result} {2 * '-'} |")
    result = solution.betterLengthOfLongestSubstring("")
    print(f"| {2 * '-'} {result} {2 * '-'} |")
    result = solution.betterLengthOfLongestSubstring(" ")
    print(f"| {2 * '-'} {result} {2 * '-'} |")
    result = solution.betterLengthOfLongestSubstring("      ")
    print(f"| {2 * '-'} {result} {2 * '-'} |")
    ed_2 = time.time()
    print(f"time taken: {ed_2 - st_2}")


