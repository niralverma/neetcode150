class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0]*len(temperatures)
        stack=[]   # pair :[temp, index]

        for i , t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackTemp, stackIndex=stack.pop()
                answer[stackIndex]= i - stackIndex
            stack.append((t,i))
        return answer
