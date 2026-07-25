class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        visited = set()

        for i in range(len(strs)):
            if i in visited:
                continue

            ana = [strs[i]]
            visited.add(i)

            for j in range(i + 1, len(strs)):
                if j not in visited and sorted(strs[i]) == sorted(strs[j]):
                    ana.append(strs[j])
                    visited.add(j)

            out.append(ana)

        return out