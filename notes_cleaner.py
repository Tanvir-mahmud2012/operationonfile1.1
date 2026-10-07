n = int(input("How many characters to preview? "))
file = open("class_notes.txt", "r")
print(file.read(n))
file.close()
print()

file = open("class_notes.txt", "r")
lines = file.readlines()
file.close()
print("Total lines:", len(lines))
for i in range(len(lines)):
    print(f"Line {i + 1} -> {lines[i].strip()}")
print()

word = input("Skip lines starting with: ")
file = open("class_notes.txt", "r")
for line in file:
    if line.startswith(word):
        print("Skip ->", line.strip())
    else:
        print("Keep ->", line.strip())
file.close()
print()

file = open("class_notes.txt", "r")
lines = file.readlines()
file.close()
out = open("class_notes_cleaned.txt", "w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close()
print("Odd lines saved to odd-lines.txt")
