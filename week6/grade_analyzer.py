# Week 6 - Student Grade Analyzer

student_records = []
stats = {}

print("=== GRADE ANALYZER ===\n")

# Collect data
for i in range(1, 7):
    name = input(f"Student {i} name: ")
    score = int(input(f"Student {i} score: "))
    student_records.append((name, score))
    print()

# extract scores
scores = [score for name, score in student_records]

# Statistics
stats["highest"] = max(scores)
stats["lowest"] = min(scores)
stats["average"] = sum(scores) / len(scores)

# unique scores
unique_scores = set(scores)

# grade distribution
grade_distribution = {}
for score in scores:
    grade_distribution[score] = grade_distribution.get(score, 0) + 1

# Output
print("\n=== STUDENT RECORDS ===")
for i, (name, score) in enumerate(student_records, 1):
    print(f"{i}. {name}: {score}")

print("\n=== CLASS STATISTICS ===")
print(f"Highest Score: {stats['highest']}")
print(f"Lowest Score: {stats['lowest']}")
print(f"Average Score: {stats['average']:.2f}")

print("\n=== UNIQUE SCORES ===")
print(unique_scores)
print(f"Total unique scores: {len(unique_scores)}")

print("\n=== GRADE DISTRIBUTION ===")
for score, count in grade_distribution.items():
    print(f"Score {score}: {count} students")
