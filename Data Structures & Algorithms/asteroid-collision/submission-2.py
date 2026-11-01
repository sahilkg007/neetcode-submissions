class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            
            if a < 0:
                if stack :
                    if a == -(stack[-1]):
                        stack.pop()
                    elif stack[-1]<0:
                        stack.append(a)
                    elif -a > stack[-1]:
                        stack.pop()
                    
                else:
                    stack.append(a)

            else:
                stack.append(a)

        return stack