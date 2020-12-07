class BagPolicy:
  def __init__(self, policy_dict):
    self.policy = policy_dict

  def find_possible_bags(self, bag_type):
    """
    Finds all bags that can contain the given bag_type
    """

    ## we use dynamic programming to store results of bags
    evaluated = dict()
    contain = list()
    for bag in self.policy:
      ## we don't want to process itself
      if bag == bag_type:
        continue

      if bag in evaluated:
        if evaluated[bag]:
          contain.append(bag)
      else:
        can_contain = self._evaluate_contain(bag, bag_type, evaluated)

        if can_contain:
          contain.append(bag)

    return contain

  def _evaluate_contain(self, bag, bag_type, evaluated):
    """
    Recursive function to see if bag can contain bag_type
    """
    ## if this bag can't contain any other bag
    if len(self.policy[bag]) == 0:
      return bag == bag_type

    results = list()
    for inner_bag in self.policy[bag]:
      if inner_bag == bag_type:
        return True
      
      elif inner_bag in evaluated:
        results.append(evaluated[inner_bag])

      else:
        r = self._evaluate_contain(inner_bag, bag_type, evaluated)
        evaluated[inner_bag] = r
        results.append(r)

    r = any(results)
    evaluated[bag] = r
    return r

  def find_total_bags(self, bag_type):
    """
    Finds total bags that can be inside bag_type
    """
    ## we use dynamic programming to store results of bags
    evaluated = dict()
    contain = 0

    inner_bags = self.policy[bag_type]
    for bag, quantity in inner_bags.items():
      if bag in evaluated:
        ## we need to count the bag itself as well as the inside bags
        contain += evaluated[bag] * quantity + quantity
      else:
        ## we need to count the bag itself as well as the inside bags
        contain += self._find_inner_total(bag, evaluated) * quantity + quantity

    return contain

  def _find_inner_total(self, bag, evaluated):
    """
    Recursive function to find total bags a bag can fit
    """
    if len(self.policy[bag]) == 0:
      return 0

    result = 0
    for inner, quantity in self.policy[bag].items():
      if inner in evaluated:
        result += evaluated[inner] * quantity + quantity

      else:
        inside_count = self._find_inner_total(inner, evaluated)
        evaluated[inner] = inside_count
        result += inside_count * quantity + quantity

    evaluated[bag] = result
    return result

if __name__ == "__main__":
  rules = dict()

  with open("input/input.txt", "r") as f:
    for line in f:
      inner = dict()

      line = line.strip()

      ## we do a series of string splits to extract information we need
      ## we also do some data normalization for easier processing
      line = line.replace("bags", "bag").replace(".", "")

      ## we divide the information into two;
      ## bigger bag --> smaller bags
      lhs, rhs = [l.strip() for l in line.split("contain")]

      ## process the left hand side first
      ## we really just need to extract the bag color
      lhs = lhs.replace("bag", "").strip()

      if rhs.startswith("no other"):
        rules[lhs] = inner
        continue

      ## process the right hand side
      ## this can be a list of bag colors with quantity so we need to store that
      rhs = [l.strip() for l in rhs.split(",")]
      
      for rule in rhs:
        ## throw away the phrase "bag" since it's not important
        rule = rule.split(" ")[:-1]
        bag_type = f"{rule[1]} {rule[2]}"
        bag_quantity = int(rule[0])
        
        inner[bag_type] = bag_quantity

      rules[lhs] = inner
  
  bp = BagPolicy(rules)

  possible_bags = len(bp.find_possible_bags("shiny gold"))

  print(f"Part 1 solution is {possible_bags}")

  total_bags = bp.find_total_bags("shiny gold")

  print(f"Part 2 solution is {total_bags}")
