if __name__ == "__main__":
  answers = list()

  with open("input/input.txt", "r") as f:
    answer = ""
    for line in f:
      line = line.strip()

      ## if blank line, that is end of the group's answers
      if line == "":
        ## add the group's answers to the list of answers
        answers.append(set(answer))
        answer = ""
        continue
      else:
        answer += line

  ## depending on the line ending of the input file,
  ## we might need to add the last item here
  if answer != "":
    answers.append(set(answer))

  answer_sum = 0
  for a in answers:
    answer_sum += len(a)

  print(f"Part 1 solution is {answer_sum}")

  answers = list()

  with open("input/input.txt", "r") as f:
    answer = set()
    no_intersection = False
    for line in f:
      line = line.strip()

      ## if blank line, that is end of the group's answers
      if line == "":
        ## add the group's answers to the list of answers
        answers.append(answer)
        answer = set()
        no_intersection = False
        continue

      else:
        ## if we found that intersection is impossible,
        ## keep skipping until empty line
        if no_intersection:
          continue

        if len(answer) == 0:
          answer = set(line)
        else:
          answer = answer.intersection(set(line))

        ## if after processing the sets we find no overlap,
        ## any further processing of other lines will yield no intersections
        if len(answer) == 0:
          no_intersection = True
          answer = set()

  ## depending on the line ending of the input file,
  ## we might need to add the last item here
  if answer != "":
    answers.append(answer)

  answer_sum = 0
  for a in answers:
    answer_sum += len(a)

  print(f"Part 2 solution is {answer_sum}")
