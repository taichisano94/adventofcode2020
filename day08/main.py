import copy

class BootCode:
  def __init__(self, instructions):
    self.instructions = instructions

  def run_instructions(self):
    """
    Runs the instruction sets.

    This stops when an infinite loop is detected and returns a boolean if so.
    """
    accumulator = 0
    visited_lines = set()
    position = 0
    loop_detected = False
    while position < len(self.instructions):
      if position in visited_lines:
        loop_detected = True
        break

      visited_lines.add(position)

      operation, argument = self.instructions[position]

      if operation == OperationCode.NOP:
        position += 1
        continue
      elif operation == OperationCode.ACC:
        accumulator += argument
        position += 1
        continue
      elif operation == OperationCode.JMP:
        position += argument
      else:
        raise Exception(f"Unknown operation code {operation} encountered at line {position}")

    return accumulator, loop_detected
    
class OperationCode:
  NOP = "nop"
  ACC = "acc"
  JMP = "jmp"

def run_simulation(instructions):
  """
  Brute force way to run simulations until a replacement of jmp or nop operation
  yields a correct termination of instructions
  """
  for position, line in enumerate(instructions):
    ## we only need a shallow copy here since we aren't changing the underlying
    ## objects; just replacing it in this new list
    instructions_copy = copy.copy(instructions)

    operation, argument = line
    if operation == OperationCode.JMP:
      instructions_copy[position] = (OperationCode.NOP, argument)
    elif operation == OperationCode.NOP:
      instructions_copy[position] = (OperationCode.JMP, argument)
    else:
      continue
    
    bp = BootCode(instructions_copy)
    accumulator, loop_detected = bp.run_instructions()
    if not loop_detected:
      break

  return accumulator

if __name__ == "__main__":
  instructions = list()

  with open("input/input.txt", "r") as f:
    for line in f:
      line = line.strip()

      operation, argument = line.split(" ")
      argument = int(argument)

      instructions.append((operation, argument))

  bc = BootCode(instructions)
  
  accumulator, loop_detected = bc.run_instructions()

  print(f"Part 1 solution is {accumulator}")

  accumulator = run_simulation(instructions)
  
  print(f"Part 2 solution is {accumulator}")
