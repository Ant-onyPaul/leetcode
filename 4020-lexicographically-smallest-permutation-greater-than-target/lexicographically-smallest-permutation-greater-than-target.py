from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:

        count = Counter(s)
        n = len(s)

        def dfs(i, greater):

            if i == n:
                return "" if greater else None

            # Try characters from smallest to largest
            for ch in sorted(count):

                if count[ch] == 0:
                    continue

                # If we are still equal to target,
                # choosing a smaller character is impossible.
                if not greater and ch < target[i]:
                    continue

                # If we are still equal, choosing a bigger
                # character makes the whole answer greater.
                new_greater = greater or ch > target[i]

                count[ch] -= 1

                result = dfs(i + 1, new_greater)

                count[ch] += 1

                if result is not None:
                    return ch + result

            return None

        ans = dfs(0, False)

        return ans if ans is not None else ""