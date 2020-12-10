from collections import defaultdict

if __name__ == "__main__":
  adapters = list()

  with open("input/input.txt", "r") as f:
    for line in f:
      line = line.strip()

      adapters.append(int(line))

  joltage_diff = defaultdict(int)

  ## include the outlet
  adapters.append(0)

  adapters.sort()

  ## include the device adapter at the end
  adapters.append(adapters[-1]+3)

  for i, adapter in enumerate(adapters):
    if i + 1 == len(adapters):
      break

    difference = adapters[i+1] - adapter
    joltage_diff[difference] += 1

  print(f"Part 1 solution is {joltage_diff[1] * joltage_diff[3]}")

  adapters.sort(reverse=True)

  path_counter = defaultdict(int)
  ## initialize the greatest adapter with 1
  path_counter[adapters[0]] = 1

  ## we're working backwards down the sorted list
  ## explanation in the README
  for i, adapter in enumerate(adapters):
    offset = 1

    ## we visit all the nodes that are within 3 jolts
    while i >= offset and adapters[i - offset] - adapter <= 3:
      path_counter[adapter] += path_counter[adapters[i - offset]]
      offset += 1

  print(f"Part 2 solution is {path_counter[0]}")
