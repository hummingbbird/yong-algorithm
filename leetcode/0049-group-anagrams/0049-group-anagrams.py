class Solution:
    # anagrams 끼리 그룹화하여 return 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        dict = {}
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS in dict:
                dict[sortedS].append(s)
            else:
                dict[sortedS] = [s]
        return list(dict.values())