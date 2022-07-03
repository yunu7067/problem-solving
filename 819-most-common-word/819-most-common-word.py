import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        return collections.Counter([word for word in re.sub(r'[^\w]', ' ', paragraph.lower()).split() if not word in banned]).most_common(1)[0][0]