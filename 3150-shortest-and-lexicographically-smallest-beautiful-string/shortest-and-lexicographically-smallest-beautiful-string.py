class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ans = ""
        count = 0
        for right in range(len(s)):
            if s[right] == "1":
                count += 1
            while count == k:
               current = s[left:right+1]
               if (ans == "" or len(current) < len(ans) or (len(current) == len(ans) and current < ans)):
                   ans = current
               if s[left] == "1":
                    count -=1
               left += 1
        return ans

              
       