class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            
            if a < 0:
                if stack and a == -(stack[-1]):
                    stack.pop()
            else:
                stack.append(a)

        return stack