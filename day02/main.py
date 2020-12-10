class PasswordPolicy:
  def __init__(self, lower, upper, policy, password=None):
    self.lower = lower
    self.upper = upper
    self.policy = policy
    self.password = password

  def is_compliant_password(self, password=None):
    p = password if password is not None else self.password
    c = p.count(self.policy)
    return self.lower <= c and c <= self.upper

  def revised_is_compliant_password(self, password=None):
    p = password if password is not None else self.password
    ## the ^ is a logical xor
    ## see https://stackoverflow.com/a/432844
    ## in this case, we want one or the other but not both
    ## subtract one from the bounds since the bounds are not zero indexed
    return (p[self.lower-1] == self.policy) ^ (p[self.upper-1] == self.policy)

def split_bound(bound):
  """
  Helper function to deal with the input for bounds.
  Assumes input is a string in format of "int-int"
  ex. "1-3"
  """
  b = bound.split("-")
  return int(b[0]), int(b[1])

if __name__ == "__main__":
  policies = list()

  ## extracting the input file into a format easier to work with
  with open("inputs/input.txt", "r") as f:
    for line in f:
      entry = line.strip().split(" ")

      lower, upper = split_bound(entry[0])
      policy_letter = entry[1][0]
      password = entry[2]

      policies.append(PasswordPolicy(lower, upper, policy_letter, password))
  
  valid_count = 0
  for policy in policies:
    if policy.is_compliant_password():
      valid_count += 1

  print(f"Part 1 solution is {valid_count}")

  valid_count = 0
  for policy in policies:
    if policy.revised_is_compliant_password():
      valid_count += 1

  print(f"Part 2 solution is {valid_count}")

      
