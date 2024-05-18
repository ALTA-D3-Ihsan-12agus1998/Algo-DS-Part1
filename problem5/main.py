def max_sequence(arr):
    n = len(arr)
    max_until_now = 0
    max_end = 0
    for i in range(0, n):
        max_end = max_end + arr[i]
        if max_end > max_until_now:
            max_until_now = max_end
        if max_end < 0:
            max_end = 0
    return max_until_now

if __name__ == "__main__":
  print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
  print(max_sequence([-2, -5, 6, -2, -3, 1, 5, -6]))  # 7
  print(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]))  # 7
  print(max_sequence([-2, -5, 6, -2, -3, 1, 6, -6]))  # 8
  print(max_sequence([-2, -5, 6, 2, -3, 1, 6, -6]))  # 12