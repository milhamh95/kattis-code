from sys import stdin

input = stdin.readline
total_courses = int(input().strip().strip())

courses = {}
for _ in range(total_courses):
    int_course = map(int, input().split())
    sorted_course = sorted(int_course)
    course_combination = tuple(sorted_course)
    courses[course_combination] = courses.get(course_combination, 0) + 1

# maximum frequency of any combination
max_freq = max(courses.values())

num_max_freq = 0
for freq in courses.values():
    if freq == max_freq:
        num_max_freq += 1

print(num_max_freq * max_freq)
