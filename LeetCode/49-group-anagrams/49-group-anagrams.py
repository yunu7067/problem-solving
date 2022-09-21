import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = collections.defaultdict(list)
        for str in strs:
            wordDict[''.join(sorted(str))].append(str)
        return wordDict.values()