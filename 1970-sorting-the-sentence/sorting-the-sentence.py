
class Solution:
    def sortSentence(self, s: str) -> str:
        aa = [""] * len(s.split())

        for word in s.split():
            pos = int(word[-1])
            aa[pos-1] = word[:-1]

        return " ".join(aa)
