class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []

        for i in range(0, len(nums), 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            num = nums[i]
            left = 0
            right = len(nums) - 1

            while left < right:
                
                if left == i:
                    left += 1
                elif right == i:
                    right -= 1

                if left == right:
                    break

                s = nums[left] + nums[right] + num
            
                if s == 0:
                    # -4 -1 -1 0 1 2
                    tmp = [nums[left], nums[right], nums[i]]
                    tmp.sort()
                    #print(tmp, left, right)
                    if tmp not in ans:
                        ans.append(tmp)
                    left += 1
                elif s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
             
        return list(ans)