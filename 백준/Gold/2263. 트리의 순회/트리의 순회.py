import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
preorder = []

def re_tree(in_pos, post_pos):
    _root = postorder[post_pos[1] - 1]
    preorder.append(_root)
    _root_idx = inorder.index(_root)

    next_l_len = _root_idx - in_pos[0]
    next_l_in_pos = (in_pos[0], in_pos[0] + next_l_len)
    next_l_post_pos = (post_pos[0], post_pos[0] + next_l_len)

    next_r_in_pos = (_root_idx + 1, in_pos[1])
    next_r_post_pos = (post_pos[0] + next_l_len, post_pos[1] - 1)
    next_r_len = next_r_post_pos[1] - next_r_post_pos[0]

    if next_l_len == 1:
        preorder.append(postorder[next_l_post_pos[1] - 1])
    elif next_l_len != 0:
        re_tree(next_l_in_pos, next_l_post_pos)

    if next_r_len == 1:
        preorder.append(postorder[next_r_post_pos[1] - 1])
    elif next_r_len != 0:
        re_tree(next_r_in_pos, next_r_post_pos)


re_tree((0, len(inorder)), (0, len(inorder)))
print(*preorder)