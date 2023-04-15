from family import family
from people import people

edu = {"john": "SEUA", "jullia": "cambridge"}

for person in people:
    print(f"{person} lives with his father \"{family[person]['father']}\" and mother \"{family[person]['mother']}\"")
    print(f"education: {edu[person]}\n")
