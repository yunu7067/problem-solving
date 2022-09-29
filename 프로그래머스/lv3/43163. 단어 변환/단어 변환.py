from collections import defaultdict, deque
import re
from typing import List


def solution(begin: str, target: str, words: List[str]):
    if not target in words:
        return 0

    dic = defaultdict(list)
    word_len = len(begin)
    words.append(begin)
    # pick word
    for i, word in enumerate(words):
        for word_idx in range(word_len):
            temp = list(word)
            temp[word_idx] = "."
            temp = "".join(temp)
            # search word
            for j in range(i + 1, len(words)):
                if re.match(temp, words[j]):
                    dic[word].append(words[j])
                    dic[words[j]].append(word)

    visited = defaultdict(bool)
    Q = deque([(begin, 0)])
    count = 1_000_000_000_000
    while Q:
        (cur, cnt) = Q.popleft()

        if cur == target:
            count = min(count, cnt)
        for next_word in dic[cur]:
            if not visited[next_word]:
                Q.append((next_word, cnt + 1))
                visited[next_word] = True

    return count
