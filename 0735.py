def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []

    def sgn(x: int):
        return abs(x) / x

    for asteroid in asteroids:
        if not stack:
            stack.append(asteroid)
            continue

        head = stack[-1]

        while stack and asteroid < 0 < stack[-1]:
            if -asteroid > stack[-1]:
                stack.pop()
                continue
            elif asteroid == stack[-1]:
                stack.pop()
            break
        else:
            stack.append(asteroid)

        # while True:
        #     if sgn(asteroid) == sgn(head):
        #         stack.append(asteroid)
        #         break

        #     if sgn(head) == -1:
        #         stack.append(asteroid)
        #         break

        #     if abs(asteroid) == abs(head):
        #         stack.pop()
        #         break

        #     if abs(asteroid) > abs(head):
        #         stack.pop()
        #         if not stack:
        #             stack.pop(asteroid)
        #             break
        #         head = stack[-1]
        #     else:
        #         break


    return stack


print(asteroidCollision([-2, -1, 1, 2]))
