class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, tmp_res = 0, 0
        wid_l, wid_r = 0, len(height)-1
        wid, hei = 0, 0
        
        while wid_l < wid_r:
            wid = wid_r - wid_l
            hei = min(height[wid_l], height[wid_r])
            tmp_res = wid * hei
            if tmp_res > res:
                res = tmp_res
            
            if height[wid_l] <= height[wid_r]:
                wid_l += 1
            else:
                wid_r -= 1

        #print(res)
        
        return res
