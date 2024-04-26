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
    if index % 2:
      print(f"Skip {index}")
      continue

    print(index)

  # Using Python continue in a while loop example

  index = 0
  while index < 10:
    index += 1

    if index % 2:
      print(f"Skip {index}")
      continue

    print(index)
