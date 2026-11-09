class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        count=0
        for i in range(len(words)):
            if pref in words[i][0:len(pref)]:
                count+=1
        return count