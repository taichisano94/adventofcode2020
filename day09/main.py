def find_invalid(xmas, window_size):
  position = window_size
  pair_found = True

  while position < len(xmas) and pair_found:
    ## reset this for each iteration
    pair_found = False

    window = set(xmas[position-window_size:position])
    for n in window:
      target = xmas[position] - n
      if target in window:
        pair_found = True
        position += 1
        break

  return position

def find_continguous_total(xmas, total):
  """
  Uses a sliding window that extends and contracts to find
  continguous numbers that sum to total
  """
  lower_bound = 0
  upper_bound = 1

  while sum(xmas[lower_bound:upper_bound]) != total:
    current_total = sum(xmas[lower_bound:upper_bound])

    if current_total == total:
      break

    ## if we have too much, remove from the end of the window
    elif current_total > total:
      lower_bound += 1

    ## if we have too little, add more to the window
    elif current_total < total:
      upper_bound += 1

  return lower_bound, upper_bound


if __name__ == "__main__":
  xmas = list()

  with open("input/input.txt", "r") as f:
    for line in f:
      line = line.strip()

      xmas.append(int(line))

  invalid_position = find_invalid(xmas, 25)

  print(f"Part 1 solution is {xmas[invalid_position]}")

  l, u = find_continguous_total(xmas, xmas[invalid_position])
  smallest = min(xmas[l:u])
  greatest = max(xmas[l:u])
  encryption_weakness = smallest + greatest

  print(f"Part 2 solution is {encryption_weakness}")
