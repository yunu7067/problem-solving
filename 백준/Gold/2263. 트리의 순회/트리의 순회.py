import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
index_inorder = [0] * (N + 1)
for i, v in enumerate(inorder):
    index_inorder[v] = i

def re_tree(in_pos, post_pos):
    if (in_pos[0] > in_pos[1]) or (post_pos[0] > post_pos[1]): return
    root = postorder[post_pos[1]]
    print(root, end=" ")
    left_len = index_inorder[root] - in_pos[0]
    right_len = in_pos[1] - index_inorder[root]
    # left node
    re_tree((in_pos[0], in_pos[0] + left_len - 1), (post_pos[0], post_pos[0] + left_len - 1))
    # right node
    re_tree((in_pos[1] - right_len + 1, in_pos[1]), (post_pos[1] - right_len, post_pos[1] - 1))

re_tree((0, N - 1), (0, N - 1))