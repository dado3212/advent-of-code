import math, re

def readPassport(rawPassport):
    passport = {}
    fields = re.findall(r"([^\s]*):([^\s]*)", rawPassport)
    for field in fields:
        passport[field[0]] = field[1]
    return passport

def isValid(passport):
    # ignore cid for now
    if "byr" not in passport:
        return False
    byr = int(passport["byr"])
    if byr < 1920 or byr > 2002:
        return False

    if "iyr" not in passport:
        return False
    iyr = int(passport["iyr"])
    if iyr < 2010 or iyr > 2020:
        return False

    if "eyr" not in passport:
        return False
    eyr = int(passport["eyr"])
    if eyr < 2020 or eyr > 2030:
        return False

    if "hgt" not in passport:
        return False
    hgt = re.match(r"(\d+)(in|cm)", passport["hgt"])
    if not hgt:
        return False
    hgt_unit = hgt.group(2)
    if hgt_unit == "in":
        hgt = int(hgt.group(1))
        if hgt < 59 or hgt > 76:
            return False
    elif hgt_unit == "cm":
        hgt = int(hgt.group(1))
        if hgt < 150 or hgt > 193:
            return False
    else:
        return False

    if "hcl" not in passport:
        return False
    hcl = re.match(r"^#[0-9a-f]{6}$", passport["hcl"])
    if not hcl:
        return False

    if "ecl" not in passport:
        return False
    ecl = passport["ecl"]
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    if "pid" not in passport:
        return False
    pid = passport["pid"]
    if len(pid) != 9 or not re.match(r"^\d*$", pid):
        return False

    return True

passports = []
with open("./input.txt", "r") as f:
    passport = ""
    for x in f.readlines():
        if x == "\n":
            passports.append(passport)
            passport = ""
        else:
            passport += x.replace("\n", " ")
    passports.append(passport)

passports = [readPassport(passport) for passport in passports]
valid = 0
for p in passports:
    print p
    print isValid(p)
    if isValid(p):
        valid += 1
print valid
