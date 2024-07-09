def solution(A, B):
    A.sort();
    B.sort();
    pa, pb, win = 0, 0, 0;
    
    while pb < len(B):
        if A[pa] > B[pb]:
            pb += 1;
        elif A[pa] == B[pb] :
            pb += 1;
        else:
            win += 1;
            pa += 1;
            pb += 1;
        # print(pb, win)
       
    return win