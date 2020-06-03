class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, tmp_res = set(), ()
        srt_nums = sorted(nums)
        print(srt_nums)
                       
        for fix_idx_1 in range(len(nums)):
            for fix_idx_2 in range(len(nums)-1, 0, -1):
                new_target = target - (srt_nums[fix_idx_1] + srt_nums[fix_idx_2])
                print(target, new_target)
                idx_1, idx_2 = fix_idx_1+1, fix_idx_2-1
    
                while idx_1 < idx_2:
                    num_1, num_2 = srt_nums[idx_1], srt_nums[idx_2]
                    if num_1 + num_2 < new_target:
                        idx_1 += 1
                    elif num_1 + num_2 > new_target:
                        idx_2 -= 1
                    else:
                        tmp_res = (srt_nums[fix_idx_1], num_1, num_2, srt_nums[fix_idx_2])
                        print(tmp_res)
                        res.add(tmp_res)
                        idx_1 += 1       
        print(res)
                       
        return res
