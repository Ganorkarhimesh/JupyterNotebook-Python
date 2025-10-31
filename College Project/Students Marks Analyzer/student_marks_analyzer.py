def calculate_grade(average):
    """Return grade based on average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B+"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Fail"

def analyze_marks(name, roll_no, marks):
    """Analyze marks and return results as a tuple."""
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)
    grade = calculate_grade(average)
    return (name, roll_no, marks, total, average, highest, lowest, grade)

def save_result(result):
    """Save student result to a text file."""
    with open("student_results.txt", "a") as f:
        f.write(f"Name: {result[0]}, Roll No: {result[1]}, Marks: {result[2]}, "
                f"Total: {result[3]}, Average: {result[4]:.2f}, Grade: {result[7]}\n")

print("🎓 STUDENT MARKS ANALYZER 🎓")
print("-" * 40)

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
n = int(input("Enter number of subjects: "))

marks = []
for i in range(n):
    m = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(m)

# Analyze
result = analyze_marks(name, roll_no, marks)

# Display output
print("\n📊 RESULT 📊")
print(f"Name       : {result[0]}")
print(f"Roll No    : {result[1]}")
print(f"Marks      : {result[2]}")
print(f"Total      : {result[3]}")
print(f"Average    : {result[4]:.2f}")
print(f"Highest    : {result[5]}")
print(f"Lowest     : {result[6]}")
print(f"Grade      : {result[7]}")

# Save result
save_result(result)
print("\n✅ Result saved successfully in 'student_results.txt'")
