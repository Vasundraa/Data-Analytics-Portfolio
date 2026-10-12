# Data Structure Design

The data structures are selected according to the operations required by the business rules.

## 1. Main Data Structures

| Data / Requirement | Chosen Structure | Example | Reason |
|---|---|---|---|
| All student records | Dictionary | `students = {"ST101": student_record}` | Student ID acts as a unique key and supports direct record lookup and updates. |
| One student's details | Dictionary | `{"name": "...", "department": "CSE", ...}` | Fields have meaningful names and can be updated independently. |
| Student courses | Set | `{"Python", "SQL"}` | Prevents duplicate registrations and supports set comparisons. |
| Student marks | Dictionary | `{"Python": 85, "SQL": 78}` | Maps each subject to its mark for retrieval, updates, and calculations. |
| Supported departments | Dictionary | `{"CSE": "Computer Science and Engineering"}` | Maps a short department code to its full name. |
| Department menu order | List | `depts = list(departments.keys())` | Preserves the configured order for numbered menu choices. |
| Supported courses | Tuple | `("Python", "SQL", "Excel", "Power BI")` | Represents a fixed collection of available courses. |
| Subject aggregate marks | Lists | `pythonMarks = []` | Enables `sum`, `len`, and `max` calculations for a subject. |
| Temporary groups of student IDs | Sets | `{sid for sid, student in students.items() ...}` | Enables intersection, difference, union, symmetric difference, and disjointness checks. |
| Temporary reports/results | Lists and tuples | `averages = [(average, sid)]` | Supports filtering, sorting, and selecting highest/lowest results. |

## 2. Student Record Structure

Each student is stored under their ID in the `students` dictionary.

```python
students = {
    "ST101": {
        "name": "Example Student",
        "department": "CSE",
        "year": 2025,
        "email": "student@example.com",
        "phoneNumber": "9876543210",
        "attendance": 80,
        "coursesRegistered": {"Python", "SQL"},
        "marks": {"Python": 85, "SQL": 78},
        "academicStatus": "Active"
    }
}
```

The example is illustrative; the application collects the actual values from console input.

## 3. Why Not Use One Structure for Everything?

- A list of student records would require searching through records to locate a particular ID. The dictionary is a better fit because the ID is the lookup key.
- A set is suitable for course registration because duplicate courses are not allowed. A set is not suitable for marks because marks must be associated with a named subject.
- A dictionary is suitable for subject marks because it expresses the relationship between a course and its mark.
- Lists are suitable for aggregate marks because the program needs to calculate counts, sums, averages, and maximum values.
- A tuple communicates that the configured course collection is fixed during normal operation.

## 4. Set Operations for Course Overlap

Let `A` be the set of active student IDs registered for the first course and `B` the set registered for the second course.

| Requirement | Operation | Meaning |
|---|---|---|
| Students registered for both courses | `A & B` | Intersection |
| First course but not second | `A - B` | Difference |
| At least one course | `A \| B` | Union |
| Exactly one of the courses | `A ^ B` | Symmetric difference |
| Check whether groups have no common students | `A.isdisjoint(B)` | Disjointness |

Student IDs are used in these sets, not names, because names may not be unique.

## 5. Aggregate Mark Lists: Important Limitation

The subject lists (`pythonMarks`, `sqlMarks`, `excelMarks`, and `powerBIMarks`) store mark values for aggregate calculations. They do not store a link back to the student ID. The application therefore removes one occurrence of an old mark when a mark is updated, a course is removed, or a student withdraws.

Because equal mark values can occur for different students, these lists should only be treated as aggregate collections and must be kept in sync with individual student records. A future design could instead calculate aggregates directly from active student records or store student IDs alongside marks to reduce the risk of inconsistent aggregate data.

## 6. Data Lifecycle

1. Registration creates a student dictionary entry.
2. Course registration adds course names to the student's course set.
3. Mark entry stores course-to-mark mappings and updates subject aggregates.
4. Updating or removing a course adjusts the student's marks and aggregate lists.
5. Withdrawal changes `academicStatus` to `Withdrawn`, removes the student's mark values from active aggregates, and retains historical details.
6. When the program exits, in-memory records are lost because no persistent storage is implemented.
