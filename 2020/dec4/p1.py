import math, re

def readPassport(rawPassport):
    passport = {}
    fields = re.findall(r"([^\s]*):([^\s]*)", rawPassport)
    for field in fields:
        passport[field[0]] = field[1]
    return passport

def isValid(passport):
    # ignore cid for now
    return "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport

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
