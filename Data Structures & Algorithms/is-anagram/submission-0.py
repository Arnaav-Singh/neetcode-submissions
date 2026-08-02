class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        constS = {}
        constT = {}
        for ch in s:
            constS[ch] = constS.get(ch,0) + 1
        for ch in t:
            constT[ch] = constT.get(ch,0) + 1
        return constS == constT