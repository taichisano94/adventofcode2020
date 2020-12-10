def brute_force(q1input):
  ## make a list here in case there are multiple solutions in the input
  solutions = list()
  for i in range(len(q1input)):
    for j in range(i+1, len(q1input)):
      ## we start at i+1 for j because 
      ## we don't want to do anything for when i = j
      if q1input[i] + q1input[j] == 2020:
        ## append the pair as a tuple so we won't accidentally
        ## mutate the data when we don't mean to
        solutions.append((q1input[i], q1input[j]))
  
  return solutions

def find_complement(q1input, whole):
  """
  Searches for the complement of each element in the set within the same set.  
  """
  ## make a set here in case there are multiple solutions in the input
  solutions = set()
  for x in q1input:
    y = whole - x
    if y in q1input and (y, x) not in solutions:
      ## we check that (y, x) is not in solutions so we don't have duplicate answers
      ## checking if a set contains something is O(1) so this operation is
      ## very minimal impact in the run time
      solutions.add((x, y))
  
  return solutions

def find_three(q1input, whole):
  for x in q1input:
    for y in q1input:
      if x != y:
        z = whole - (x + y)
        if z in q1input:
          return (x, y, z)

  raise Exception("Input error: could not find 3 numbers that sum to 2020")

if __name__ == "__main__":
  q1input = list()

  ## read in the input file
  with open("inputs/input1.txt", "r") as f:
    ## we iterate over the file object since readlines() is not memory efficient
    for line in f:
      ## we strip the \n so we can convert the lines to an int
      q1input.append(int(line.strip()))

  # bf_solution = brute_force(q1input)
  # print(bf_solution)

  complements = find_complement(set(q1input), 2020)

  print("Part 1 solution is:")
  for ans in complements:
    print("\t{} * {} = {}".format(ans[0], ans[1], ans[0]*ans[1]))

  ans = find_three(set(q1input), 2020)
  print("Part 2 solution is:")
  print("\t{} * {} * {} = {}".format(ans[0], ans[1], ans[2], ans[0]*ans[1]*ans[2]))