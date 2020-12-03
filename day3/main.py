class Slope:
  def __init__(self, slopes):
    self.slopes = slopes
    self.column_width = len(slopes[0])

  def is_open_space(self, row, column):
    ## there are no trees for a slope that doesn't exist
    if row > len(self.slopes):
      return True
    
    column = column % self.column_width
    return self.slopes[row][column] == "."

if __name__ == "__main__":
  slopes = list()

  with open("input/input.txt", "r") as f:
    for line in f:
      slopes.append(line.strip())

  s = Slope(slopes)

  trees_count = 0
  right_counter = 0
  down_counter = 0
  for line in slopes[1:]:
    right_counter += 3
    down_counter += 1
    if not s.is_open_space(down_counter, right_counter):
      trees_count += 1

  print(f"Part 1 solution is {trees_count}")
  
  print("Calculating Part 2")

  ## make a list to traverse over; this is so there's less copy/paste to do
  slopes_to_test = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
  trees_count_mult = 1

  for test in slopes_to_test:
    right_movement = test[0]
    down_movement = test[1]
    right_counter = 0
    down_counter = 0
    trees_count = 0

    for line in slopes[1:]:
      right_counter += right_movement
      down_counter += down_movement
      if not s.is_open_space(down_counter, right_counter):
        trees_count += 1

    print(f"\tTrees count for right {right_movement} down {down_movement} is {trees_count}")

    trees_count_mult = trees_count_mult * trees_count

  print(f"Part 2 solution is {trees_count_mult}")