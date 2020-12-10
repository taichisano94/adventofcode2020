import re

class Passport:
  hair_color_regex = r"^#(\d|[a-f]){6}$"
  eye_color_set = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

  def __init__(self, birth_year=None, 
              issue_year=None, 
              expiration_year=None,
              height=None, 
              hair_color=None, 
              eye_color=None, 
              passport_id=None, 
              country_id=None):
    self.birth_year = birth_year
    self.issue_year = issue_year
    self.expiration_year = expiration_year
    self.height = height
    self.hair_color = hair_color
    self.eye_color = eye_color
    self.passport_id = passport_id
    self.country_id = country_id

  def is_valid_passport(self):
    return not (self.birth_year is None or 
    self.issue_year is None or 
    self.expiration_year is None or
    self.height is None or 
    self.hair_color is None or 
    self.eye_color is None or 
    self.passport_id is None)

  def validate_fields(self):
    """
    Helper function that formats fields to desired

    Typically we want to do this in the __init__ but separating
    this into a different function to differentiate part 1 and part 2

    If the field doesn't adhere to the requirements, it gets forced into None
    """
    ## birth year must be four digits; at least 1920 and at most 2002
    if self.birth_year is not None:
      try:
        byr = int(self.birth_year)
        if not (byr >= 1920 and byr <= 2002):
          self.birth_year = None
      except:
        self.birth_year = None

    ## issue year must be four digits; at least 2010 and at most 2020
    if self.issue_year is not None:
      try:
        iyr = int(self.issue_year)
        if not (iyr >= 2010 and iyr <= 2020):
          self.issue_year = None
      except:
        self.issue_year = None

    ## expiration year must be four digits; at least 2020 and at most 2030
    if self.expiration_year is not None:
      try:
        eyr = int(self.expiration_year)
        if not (eyr >= 2020 and eyr <= 2030):
          self.expiration_year = None
      except:
        self.expiration_year = None

    ## height must be a number followed by either cm or in:
    ## If cm, the number must be at least 150 and at most 193
    ## If in, the number must be at least 59 and at most 76
    if self.height is not None:
      try:
        if self.height.endswith("cm"):
          hgt = int(self.height[:-2])
          if not (hgt >= 150 and hgt <= 193):
            self.height = None
        elif self.height.endswith("in"):
          hgt = int(self.height[:-2])
          if not (hgt >= 59 and hgt <= 76):
            self.height = None
        else:
          self.height = None
      except:
        self.height = None

    ## hair color must be a # followed by exactly six characters 0-9 or a-f
    if self.hair_color is not None:
      if not re.match(Passport.hair_color_regex, self.hair_color):
        self.hair_color = None

    ## eye color must be exactly one of: amb blu brn gry grn hzl oth
    if self.eye_color is not None:
      if self.eye_color not in Passport.eye_color_set:
        self.eye_color = None

    ## passport id must be a nine-digit number, including leading zeroes
    if self.passport_id is not None and len(self.passport_id) == 9:
      try:
        int(self.passport_id)
      except:
        self.passport_id = None
    else:
      self.passport_id = None

  def __str__(self):
    return f"""Passport(
      birth_year={self.birth_year}, 
      issue_year={self.issue_year}, 
      expiration_year={self.expiration_year}, 
      height={self.height}, 
      hair_color={self.hair_color}, 
      eye_color={self.eye_color}, 
      passport_id={self.passport_id}, 
      country_id={self.country_id}
      )"""


def get_default_fields():
  """
  Helper function to reset all variables to default state

  Use it like so:
  byr, ## birth year
  iyr, ## issue year
  eyr, ## expiration year
  hgt, ## height
  hcl, ## hair color
  ecl, ## eye color
  pid, ## passport id
  cid  ## country id
  """
  return None, None, None, None, None, None, None, None

if __name__ == "__main__":
  passports = list()

  with open("input/input.txt", "r") as f:
    byr, iyr, eyr, hgt, hcl, ecl, pid, cid = get_default_fields()
    line_count = 0
    for line in f:
      line_count += 1
      line = line.strip()
      if line == "":
        ## an empty line signifies the end of the current passport iteration
        passports.append(Passport(birth_year=byr, issue_year=iyr, expiration_year=eyr,
                          height=hgt, hair_color=hcl, eye_color=ecl, 
                          passport_id=pid, country_id=cid))

        ## set everything back to default for next passport
        byr, iyr, eyr, hgt, hcl, ecl, pid, cid = get_default_fields()

        ## we don't want to execute the rest of the logic if it's an empty line
        continue


      ## extract the kvp
      info = line.split(" ")
      for kvp in info:
        kvp = kvp.split(":")
        key = kvp[0]
        value = kvp[1]

        if key == "byr":
          byr = value
        elif key == "iyr":
          iyr = value
        elif key == "eyr":
          eyr = value
        elif key == "hgt":
          hgt = value
        elif key == "hcl":
          hcl = value
        elif key == "ecl":
          ecl = value
        elif key == "pid":
          pid = value
        elif key == "cid":
          cid = value
        else:
          raise Exception(f"Unknown kvp encountered: {kvp}")

  ## make sure we get the last passport item;
  ## this part is finnicky and depends on how the input text file ends
  if byr is not None or iyr is not None or eyr is not None or \
    hgt is not None or hcl is not None or ecl is not None or \
    pid is not None or cid is not None:
      passports.append(Passport(birth_year=byr, issue_year=iyr, expiration_year=eyr,
                          height=hgt, hair_color=hcl, eye_color=ecl, 
                          passport_id=pid, country_id=cid))

  valid_count = 0
  for passport in passports:
    if passport.is_valid_passport():
      valid_count += 1

  print(f"Part 1 solution is {valid_count}")

  valid_count = 0
  for passport in passports:
    passport.validate_fields()
    if passport.is_valid_passport():
      valid_count += 1

  print(f"Part 2 solution is {valid_count}")
