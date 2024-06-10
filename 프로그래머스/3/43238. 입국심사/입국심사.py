def solution(n, times):
    start_t = min(times)
    end_t = start_t * n # 1_000_000_000 * 1_000_000_000 

    while start_t + 1 != end_t:
        mid_t = (end_t + start_t) // 2

        if sum(mid_t // _t for _t in times) >= n:
            end_t = mid_t
        else:
            start_t = mid_t;
    
    return end_t