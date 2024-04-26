if __name__ == "__main__":
  # Introduction to the Python continue statement

  """
  for index in range(n):
    if condition:
      continue

    # more code here
  """

  """
  while condition1:
    if condition2:
      continue

    # more code here
  """

  # Using Python continue in a for loop example

  for index in range(10):
    if index % 2 == 0:
        print(f"Skip {index}")
        continue

    print(index)
