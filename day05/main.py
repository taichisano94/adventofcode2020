import math

class BoardingPass:
  def __init__(self, partition):
    self.partition = partition
    self.row = self.calculate_binary(partition[:7], "F", "B")
    self.column = self.calculate_binary(partition[7:], "L", "R")

  def calculate_binary_search(self, partitions, lower_half_code, upper_half_code):
    ## the length of number of partitions indicate how many bits there are
    upper_row = 2 ** len(partitions) - 1
    lower_row = 0
    for p in partitions:
      ## on each partition, we need to find the midpoint of the bound
      midpoint = (upper_row+lower_row)/2
      if p == lower_half_code:
        upper_row = math.floor(midpoint)
      elif p == upper_half_code:
        lower_row = math.ceil(midpoint)

    ## at this point, lower and upper row are the same so just return one of them
    return upper_row

  def calculate_binary(self, partitions, zero_code, one_code):
    binary_str = partitions.replace(zero_code, "0").replace(one_code, "1")
    return int(binary_str, 2)

  def calculate_id(self):
    return self.row * 8 + self.column

  def __str__(self):
    return f"BoardingPass(row={self.row}, column={self.column})"

if __name__ == "__main__":
  passes = list()

  with open("input/input.txt", "r") as f:
    for line in f:
      passes.append(BoardingPass(line.strip()))

  highest_id = -1
  for bp in passes:
    id = bp.calculate_id()
    if id > highest_id:
      highest_id = id

  print(f"Part 1 solution is {highest_id}")

  seating = list()
  for bp in passes:
    seating.append(bp.calculate_id())

  seating.sort()

  candidate = None
  for i, id in enumerate(seating):
    ## we know that the seats can't be the very first or last
    ## so skip it
    if i == 0 or i == len(seating) - 1:
      continue

    ## because we're guaranteed to not be index out of bounds
    ## since we skipped the first and last seat, we can
    ## freely check the seat before and after
    if not (seating[i+1] == id + 1) or not (seating[i-1] == id - 1):
      ## add one because id's value is a filled seat
      ## the seat next to this is the empty one
      candidate = id + 1
      break

  print(f"Part 2 solution is {candidate}")