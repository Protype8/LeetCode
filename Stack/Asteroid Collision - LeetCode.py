class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for asteroid in asteroids[1:]:
            if(asteroid < 0):
                if(len(stack) == 0):
                    stack.append(asteroid)
                else:
                    while len(stack) > 0:
                        prev_asteroid = stack.pop()
                        if(prev_asteroid < 0):
                            stack.append(prev_asteroid)
                            stack.append(asteroid)
                            break
                        elif(prev_asteroid+asteroid > 0):
                            stack.append(prev_asteroid)
                            break
                        elif(prev_asteroid+asteroid == 0):
                            break
                    else:
                        stack.append(asteroid)
            else:
                stack.append(asteroid)
        return stack
