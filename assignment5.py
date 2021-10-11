#!/bin/python3

def process_bmi(person_info):
    '''
    w: weight (kg)
    h: height (m)
    '''
    (w, h) = person_info
    bmi = w / h**2
    if bmi < 18.5:
        return "under"
    if bmi < 25:
        return "normal"
    if bmi < 30:
        return "over"
    return "obese"

if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        def parse_person(person):
            person = person.split(" ")
            return (int(person[0]), float(person[1]))
        lines = fp.readlines()

        results = list(map(lambda p: process_bmi(parse_person(p)), lines[1:]))

        print(" ".join(item for item in results))
