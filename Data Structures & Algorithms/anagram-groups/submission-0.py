class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            i = ''.join(sorted(s))
            if i not in anagrams:
                anagrams[i] = []
            anagrams[i].append(s)
        return list(anagrams.values())
