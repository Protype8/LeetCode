class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        current = s[:10]
        seen_patterns = set([current])
        output = set([])
        for i in range(10,len(s)):
            current = current[1:]+s[i]
            if(current in seen_patterns):
                output.add(current)
            else:
                seen_patterns.add(current)
        return output
