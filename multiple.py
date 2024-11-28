def multiply(num1, num2):
    # Determine the sign of the result
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    # Initialize result array
    result = [0] * (len(num1) + len(num2))

    # Perform multiplication using the traditional grade-school algorithm
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # Remove leading zeros
    start_idx = next((i for i, x in enumerate(result) if x != 0), len(result))
    result = result[start_idx:] or [0]

    # Adjust for the sign
    result[0] *= sign
    return result

print(multiply([1, 2, 3], [4, 5]))