def dailyTemperatures(temperatures: list[int]) -> list[int]:

    stack: list[tuple[int, int]] = []
    result = [0] * len(temperatures)
    for i, temperature in enumerate(temperatures):          
        for j in range(len(stack)-1, -1, -1):
            if temperature > stack[j][1]:
                result[stack[j][0]] = i - stack[j][0]
                stack.pop()
                continue
            break
    
        stack.append((i, temperature))

    return result

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))
print(dailyTemperatures([30,60,90]))