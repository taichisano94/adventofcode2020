class Seating:
  def __init__(self, seating):
    self.seating = seating

  def calculate_seating_iteration(self):
    """
    Does a single iteration of the seating rules

    Returns a new Seating object with the updated seats
    """
    ## we need to make a new list because the rules need to be applied
    ## to every seat simultaneously
    new_seating = list()
    for i, row in enumerate(self.seating):
      new_row = ""
      for j, seat in enumerate(row):
        ## don't process the floor
        if seat == SeatType.FLOOR:
          new_row += SeatType.FLOOR
          continue

        adjacent = self._get_adjacent(i, j)

        if seat == SeatType.EMPTY:
          ## count the number of occupied seats in adjacent spots
          ## if none are occupied, seat becomes occupied
          if adjacent.count(SeatType.OCCUPIED) == 0:
            new_row += SeatType.OCCUPIED
          else:
            new_row += seat
        elif seat == SeatType.OCCUPIED:
          ## count number of occupied seats in adjacent spots
          ## if more than 4, seat becomes empty
          if adjacent.count(SeatType.OCCUPIED) >= 4:
            new_row += SeatType.EMPTY
          else:
            new_row += seat
        else:
          raise Exception(f"Unknown seat type {seat} at {i}x{j}")

      new_seating.append(new_row)

    return Seating(new_seating)

  def _get_adjacent(self, row_index, column_index):
    """
    Helper function to get adjacent seats

    Returns in order of 
    1. diagonal up left
    2. up
    3. diagonal up right
    4. left
    5. right
    6. diagonal down left
    7. down
    8. diagonal down right
    """
    dul = None ## diagonal up left
    up = None
    dur = None ## diagonal up right
    left = None
    right = None
    ddl = None ## diagonal down left
    down = None
    ddr = None ## diagonal down right

    num_rows, num_columns = self.get_dimension()

    ## diagonal up left is one row up and one column left
    if row_index - 1 >= 0 and column_index - 1 >= 0:
      dul = self.seating[row_index-1][column_index-1]
    ## up is one row up
    if row_index - 1 >= 0:
      up = self.seating[row_index-1][column_index]
    ## digonal up right is one row up and one column right
    if row_index - 1 >= 0 and column_index + 1 < num_columns:
      dur = self.seating[row_index-1][column_index+1]
    ## left is one column left
    if column_index - 1 >= 0:
      left = self.seating[row_index][column_index-1]
    ## right is one column right
    if column_index + 1 < num_columns:
      right = self.seating[row_index][column_index+1]
    ## diagonal down left is one row down and one column left
    if row_index + 1 < num_rows and column_index - 1 >= 0:
      ddl = self.seating[row_index+1][column_index-1]
    ## down is one row down
    if row_index + 1 < num_rows:
      down = self.seating[row_index+1][column_index]
    ## diagonal down right is one row down and one column right
    if row_index + 1 < num_rows and column_index + 1 < num_columns:
      ddr = self.seating[row_index+1][column_index+1]

    return tuple([dul, up, dur, left, right, ddl, down, ddr])

  def calculate_seating_iteration_revised(self):
    """
    Adjacent squares now consider line of sight
    """
    new_seating = list()
    for i, row in enumerate(self.seating):
      new_row = ""
      for j, seat in enumerate(row):
        ## don't process the floor
        if seat == SeatType.FLOOR:
          new_row += SeatType.FLOOR
          continue

        los = self._get_seat_in_los(i, j)

        if seat == SeatType.EMPTY:
          ## count the number of occupied seats in adjacent spots
          ## if none are occupied, seat becomes occupied
          if los.count(SeatType.OCCUPIED) == 0:
            new_row += SeatType.OCCUPIED
          else:
            new_row += seat
        elif seat == SeatType.OCCUPIED:
          ## count number of occupied seats in adjacent spots
          ## if more than 4, seat becomes empty
          if los.count(SeatType.OCCUPIED) >= 5:
            new_row += SeatType.EMPTY
          else:
            new_row += seat
        else:
          raise Exception(f"Unknown seat type {seat} at {i}x{j}")

      new_seating.append(new_row)

    return Seating(new_seating)

  def _get_seat_in_los(self, row_index, column_index):
    """
    Helper function to get seats that are in line of sight

    Line of sight is determined by a line of slope 1 in the direction
    this behavior can be replicated by adjusting the row and column
    index by 1 in the direction

    Returns in order of 
    1. diagonal up left
    2. up
    3. diagonal up right
    4. left
    5. right
    6. diagonal down left
    7. down
    8. diagonal down right
    """
    dul = None ## diagonal up left
    up = None
    dur = None ## diagonal up right
    left = None
    right = None
    ddl = None ## diagonal down left
    down = None
    ddr = None ## diagonal down right

    num_rows, num_columns = self.get_dimension()

    def is_seat(seat):
      return seat == SeatType.OCCUPIED or seat == SeatType.EMPTY

    ## diagonal up left is one row up and one column left
    ## we keep going until we either see nothing to the edge
    ## or we see a seat
    row_offset = 1
    column_offset = 1
    while row_index - row_offset >= 0 and column_index - column_offset >= 0:
      seat = self.seating[row_index - row_offset][column_index - column_offset]
      if is_seat(seat):
        dul = seat
        break
      row_offset += 1
      column_offset += 1
  
    ## up is one row up
    row_offset = 1
    while row_index - row_offset >= 0:
      seat = self.seating[row_index - row_offset][column_index]
      if is_seat(seat):
        up = seat
        break
      row_offset += 1

    ## digonal up right is one row up and one column right
    row_offset = 1
    column_offset = 1
    while row_index - row_offset >= 0 and \
      column_index + column_offset < num_columns:
      seat = self.seating[row_index - row_offset][column_index + column_offset]
      if is_seat(seat):
        dur = seat
        break
      row_offset += 1
      column_offset += 1

    ## left is one column left
    column_offset = 1
    while column_index - column_offset >= 0:
      seat = self.seating[row_index][column_index - column_offset]
      if is_seat(seat):
        left = seat
        break
      column_offset += 1

    ## right is one column right
    column_offset = 1
    while column_index + column_offset < num_columns:
      seat = self.seating[row_index][column_index + column_offset]
      if is_seat(seat):
        right = seat
        break
      column_offset += 1

    ## diagonal down left is one row down and one column left
    row_offset = 1
    column_offset = 1
    while row_index + row_offset < num_rows and column_index - column_offset >= 0:
      seat = self.seating[row_index + row_offset][column_index - column_offset]
      if is_seat(seat):
        ddl = seat
        break
      row_offset += 1
      column_offset += 1

    ## down is one row down
    row_offset = 1
    while row_index + row_offset < num_rows:
      seat = self.seating[row_index + row_offset][column_index]
      if is_seat(seat):
        down = seat
        break
      row_offset += 1

    ## diagonal down right is one row down and one column right
    row_offset = 1
    column_offset = 1
    while row_index + row_offset < num_rows and \
       column_index + column_offset < num_columns:
      seat = self.seating[row_index + row_offset][column_index + column_offset]
      if is_seat(seat):
        ddr = seat
        break
      row_offset += 1
      column_offset += 1

    return tuple([dul, up, dur, left, right, ddl, down, ddr])

  def get_dimension(self):
    """
    Helper function gets the dimension of the seating

    Returns (row, column)
    """
    return (len(self.seating), len(self.seating[0]))

  def count_occupied(self):
    """
    Helper function to get number of occupied seats
    """
    occupied_count = 0
    for row in self.seating:
      occupied_count += row.count(SeatType.OCCUPIED)

    return occupied_count

  def __eq__(self, seating):
    """
    Override to help determine if seating state changed
    """
    if not isinstance(seating, Seating) or \
       self.get_dimension() != seating.get_dimension():
      return False

    for i in range(self.get_dimension()[0]):
      if self.seating[i] != seating.seating[i]:
        return False

    return True
    
  def __str__(self):
    """
    This helps visualize the seating chart
    """
    return "\n".join(self.seating)

class SeatType:
  EMPTY = "L"
  OCCUPIED = "#"
  FLOOR = "."

if __name__ == "__main__":
  seat_chart = list()

  with open("input/input.txt", "r") as f:
    for line in f:
      line = line.strip()

      seat_chart.append(line)

  seating = Seating(seat_chart)
  next_seating = seating.calculate_seating_iteration()

  while next_seating != seating:
    seating = next_seating
    next_seating = next_seating.calculate_seating_iteration()

  print(f"Part 1 solution is {next_seating.count_occupied()}")

  seating = Seating(seat_chart)
  next_seating = seating.calculate_seating_iteration_revised()

  while next_seating != seating:
    seating = next_seating
    next_seating = next_seating.calculate_seating_iteration_revised()

  print(f"Part 2 solution is {next_seating.count_occupied()}")
