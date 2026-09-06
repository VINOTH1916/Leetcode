class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        
            n =  len(arr)
            res = 0
            stack = []
            for i in range(n):
                while stack and arr[stack[-1]] >= arr[i]:
                    t = stack.pop()
                
                    if stack:
                        wid = i - stack[-1] - 1
                    else:
                        wid = i

                    res = max(res,wid*arr[t])

                stack.append(i)

            while stack:
                t = stack.pop()
                if not stack:
                    wid = n
                else:
                    wid = n - stack[-1] - 1

                res = max(res, wid*arr[t])

            return res


        
        