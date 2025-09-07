class Solution:


    def isAnagram(self, s: str, t: str) -> bool:
        def countAlphabet(string: str) -> dict:
            countDict = {}
            for c in string:
                # countDict[c]+=1 if c in countDict else countDict[c] == 1
                if c in countDict:
                    countDict[c] += 1
                else:
                    countDict[c] = 1
            return sorted(countDict.items())
        # 구성이 same이지만 .. 배열은 다른 두 문자열 ..
        # 우선 길이가 같은지 봐야겠군
        if len(s) != len(t):
            return False
        else:
            return countAlphabet(s) == countAlphabet(t)
        
        