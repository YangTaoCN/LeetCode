class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1,len(s1)):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]) or self.isScramble(s1[:i],s2[len(s1)-i:]) and self.isScramble(s1[i:],s2[:len(s1)-i]):
                return True
        return False
