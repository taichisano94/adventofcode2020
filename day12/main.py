class Direction:
  EAST = 0
  NORTH = 1
  WEST = 2
  SOUTH = 3

  @staticmethod
  def get_direction_string(value):
    if value == Direction.EAST:
      return "EAST"
    elif value == Direction.NORTH:
      return "NORTH"
    elif value == Direction.WEST:
      return "WEST"
    elif value == Direction.SOUTH:
      return "SOUTH"
    else:
      raise Exception(f"Unknown value {value} for direction")

class InstructionCode:
  FORWARD = "F"
  RIGHT_ROTATE = "R"
  LEFT_ROTATE = "L"
  NORTH = "N"
  SOUTH = "S"
  EAST = "E"
  WEST = "W"

class Ship:
  def __init__(self):
    """
    We treat moving east as positive x and north as positive y
    """
    self.x = 0
    self.y = 0
    self.direction = Direction.EAST

  def do_instruction(self, code, value):
    """
    Process a single instruction
    """
    if code == InstructionCode.FORWARD:
      self._update_direction_movement(self.direction, value)
      
    elif code == InstructionCode.NORTH:
      self._update_direction_movement(Direction.NORTH, value)

    elif code == InstructionCode.SOUTH:
      self._update_direction_movement(Direction.SOUTH, value)

    elif code == InstructionCode.EAST:
      self._update_direction_movement(Direction.EAST, value)

    elif code == InstructionCode.WEST:
      self._update_direction_movement(Direction.WEST, value)

    elif code == InstructionCode.LEFT_ROTATE or code == InstructionCode.RIGHT_ROTATE:
      self._update_direction_face(code, value)

  def _update_direction_movement(self, direction, value):
    """
    Updates the coordinate movement according to given direction
    """
    if direction == Direction.EAST:
      self.x += value
    elif direction == Direction.WEST:
      self.x -= value
    elif direction == Direction.NORTH:
      self.y += value
    elif direction == Direction.SOUTH:
      self.y -= value
    else:
      raise Exception(f"Unknown direction {direction} given")

  def _update_direction_face(self, rotation, value):
    """
    Update the way the ship is facing
    """
    rotation_amount = value / 90
    if rotation == InstructionCode.LEFT_ROTATE:
      self.direction = (self.direction + rotation_amount) % 4

    elif rotation == InstructionCode.RIGHT_ROTATE:
      self.direction = (self.direction - rotation_amount) % 4

    else:
      raise Exception(f"Unknown rotation direction {rotation}")

  def get_manhattan_distance(self):
    return abs(self.x) + abs(self.y)

  def get_current_location(self):
    return (self.x, self.y)

  def __str__(self):
    return f"{self.get_current_location()}[{Direction.get_direction_string(self.direction)}]"

class Waypoint:
  """
  The x and y values are relative to the ship's position and does not mean
  the literal position in the grid
  """
  def __init__(self):
    self.relative_x = 10
    self.relative_y = 1

  def move(self, direction, value):
    """
    Moves the waypoint's relative position
    """
    if direction == Direction.EAST:
      self.relative_x += value
    elif direction == Direction.WEST:
      self.relative_x -= value
    elif direction == Direction.NORTH:
      self.relative_y += value
    elif direction == Direction.SOUTH:
      self.relative_y -= value
    else:
      raise Exception(f"Unknown direction {direction}")

  def rotate(self, rotation, value):
    """
    Rotates the relative position of the waypoint
    """
    rotation_amount = int(value / 90)
    for i in range(rotation_amount):
      if rotation == InstructionCode.LEFT_ROTATE:
        self.relative_x, self.relative_y = self.relative_y * -1, self.relative_x
      else:
        self.relative_x, self.relative_y = self.relative_y, self.relative_x * -1

  def __str__(self):
    x_str = f"+{self.relative_x}" if self.relative_x > 0 else self.relative_x
    y_str = f"+{self.relative_y}" if self.relative_y > 0 else self.relative_y
    return f"({x_str}, {y_str})"


class ShipWaypointManager:
  """
  Class that manages how the ship and waypoint moves
  """
  def __init__(self):
    self.ship = Ship()
    self.waypoint = Waypoint()

  def do_instruction(self, code, value):
    if code == InstructionCode.FORWARD:
      for i in range(value):
        self.ship.x += self.waypoint.relative_x
        self.ship.y += self.waypoint.relative_y

    elif code == InstructionCode.EAST:
      self.waypoint.move(Direction.EAST, value)

    elif code == InstructionCode.WEST:
      self.waypoint.move(Direction.WEST, value)

    elif code == InstructionCode.NORTH:
      self.waypoint.move(Direction.NORTH, value)

    elif code == InstructionCode.SOUTH:
      self.waypoint.move(Direction.SOUTH, value)

    elif code == InstructionCode.LEFT_ROTATE or code == InstructionCode.RIGHT_ROTATE:
      self.waypoint.rotate(code, value)

    else:
      raise Exception(f"Unknown instruction {code}")

  def __str__(self):
    return f"{self.ship}{self.waypoint}"

if __name__ == "__main__":
  instructions = list()

  with open("input/input.txt", "r") as f:
    for line in f:
      line = line.strip()

      instructions.append(line)

  ship = Ship()
  
  for i in instructions:
    code = i[0]
    value = int(i[1:])

    ship.do_instruction(code, value)

  print(f"Part 1 solution is {ship.get_manhattan_distance()}")

  m = ShipWaypointManager()

  for i in instructions:
    code = i[0]
    value = int(i[1:])

    m.do_instruction(code, value)

  print(f"Part 2 solution is {m.ship.get_manhattan_distance()}")
