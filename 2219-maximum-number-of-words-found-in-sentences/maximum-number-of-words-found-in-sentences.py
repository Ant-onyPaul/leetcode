class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        count=0
        for s in sentences:
            words=s.split()
            count=max(len(words),count)
        return count
        