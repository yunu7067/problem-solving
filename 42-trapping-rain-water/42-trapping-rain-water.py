class Solution:
    def trap(self, height: List[int]) -> int:
        base_h = 0
        base_i = 0
        traps = []
        while base_i < len(height):
            cur_h = height[base_i]
            # print(f"base_i:{base_i}, cur_h:{cur_h}")
            if (base_h == 0 and cur_h == 0):
                base_i += 1;
                continue;
            right = height[base_i+1:]
            if right == []:
                break;
            base_h = cur_h
            # print(f"right:{right}, base_h:{base_h}, max(right): {max(right)}")
            # 우측변이 base보다 작다면
            max_right = max(right)
            if base_h > max_right:
                # base 높이를 우측변으로 설정
                base_h = max_right
            # 우측변이 0이면 끝
            elif max_right == 0:
                break
            # 우측변이 base보다 크다면
            # base 그대로 사용
                
            cur_trap = 0
            for j, next_h in enumerate(right):
                # print(f"j: {j}, next_h: {next_h}, base_h: {base_h}")
                # base보다 작다면
                if next_h < base_h:
                    cur_trap += base_h - next_h
                    # 계속
                # base보다 크거나 같다면
                else:
                    base_i = base_i + j + 1
                    # print(f"base_i::{base_i},,j::{j}")
                    traps.append(cur_trap)
                    break;
                    # 계산하고 끝
            
        return sum(traps)
        pass