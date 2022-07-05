from itertools import combinations
import collections

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3개 이하면 바로 빈 배열 리턴
        if len(nums) < 3:
            return []

        sums = set()
        p_nums = []
        n_nums = []
        zeros = []
        nums.sort()
        for num in nums:
            if num > 0:
                p_nums.append(num)
            elif num < 0:
                n_nums.append(num)
            else:
                zeros.append(0)
        is_zero = len(zeros) > 0

        if len(zeros) >= 3:
            sums.add((0, 0, 0))

        # 양1음1=0인 경우 (0이 있는 경우)
        if is_zero:
            for p_num in p_nums:
                if -p_num in n_nums:
                    sums.add((-p_num, 0, p_num))

        # 양2음1=0인 경우
        p_2comb_nums = combinations(p_nums, 2)
        p_2comb_dict = collections.defaultdict(list)
        for comb in p_2comb_nums:
            p_2comb_dict[comb[0] + comb[1]].append(comb)
        for n_num in n_nums:
            if -n_num in p_2comb_dict:
                for (a, b) in p_2comb_dict[-n_num]:
                    sums.add((n_num, a, b))
        # 양1음2=0인 경우
        n_2comb_nums = combinations(n_nums, 2)
        n_2comb_dict = collections.defaultdict(list)
        for comb in n_2comb_nums:
            n_2comb_dict[comb[0] + comb[1]].append(comb)
        for p_num in p_nums:
            if -p_num in n_2comb_dict:
                for (a, b) in n_2comb_dict[-p_num]:
                    sums.add((a, b, p_num))
        
        return list(sums)
