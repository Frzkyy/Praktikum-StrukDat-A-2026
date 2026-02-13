keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}
print(f"Keahlian A dan B: {keahlian_A | keahlian_B}")
print(keahlian_A)
print(f"Keahlian unik A: {keahlian_A.difference(keahlian_B)}, keahlian unik B: {keahlian_B.difference(keahlian_A)}")
if "Java" in keahlian_B:
    print("B bisa Java")
else:
    print("B tidak bisa Java")