# Neo4j Cypher Guide — UZH Course Catalog

Read this guide before writing any `run_cypher_query` call.

## Graph Model

```
(:Faculty)
  ^
  |[:BELONGS_TO]
  |
(:DegreeProgram)
  ^
  |[:BELONGS_TO]
  |
(:Field) <--[:PART_OF]-- (:StudyModule)
                             |
              +--------------+---------------+
              |              |               |
        [:HAS_EVENT]   [:HAS_AREA]    <-[:HAS_TOPIC]-
              |              |               |
              v              v               |
          (:Event)       (:AREA)    (:OverarchingTopic)
              |
        [:TAUGHT_BY]
              |
              v
          (:Person)
```

**Node counts** (approximate): StudyModule 390, Event 6980, Person 347, Field 107,
OverarchingTopic 36, AREA 14, DegreeProgram 5, Faculty 1.

## Relationship Summary

| From | Rel | To | Count | Notes |
|------|-----|----|-------|-------|
| Event | TAUGHT_BY | Person | 9659 | Lecturers are linked via Event, NOT StudyModule |
| StudyModule | HAS_EVENT | Event | 6980 | |
| StudyModule | PART_OF | Field | 3646 | |
| OverarchingTopic | HAS_TOPIC | StudyModule | 694 | Topic points TO module |
| StudyModule | HAS_AREA | AREA | 406 | Label is AREA (uppercase) |
| Field | BELONGS_TO | DegreeProgram | 146 | |
| DegreeProgram | BELONGS_TO | Faculty | 5 | |

## Node Properties

### StudyModule
- `Id` — course identifier (e.g. "03SM22AOEC10")
- `SmText` — course name
- `Year` — academic year (int)
- `Session` — "003" = Autumn, "004" = Spring
- `Points` — ECTS credits (float)
- `Language` — e.g. "English", "Deutsch"
- `link` — VVZ course URL
- `Schedule` — schedule text
- `TestsDescription`, `ObjectiveDescription`, `PrecognitionDescription`
- `CommonDescription`, `MaterialDescription`, `AudienceDescription`
- `Category`, `Valid`, `Cancel`
- `*_embedding` fields exist but are auto-stripped from results

### Event
- `Evdat` — day + date string
- `EvStartTime`, `EvEndTime` — time strings
- `CatSort` — event type (lecture/exercise/etc.)
- `Room` — room name
- `Period` — period identifier
- `Id` — series identifier

### Person
- `Name` — full name of lecturer

### Field
- `Text` — field/major/minor name

### DegreeProgram
- `Text` — program name
- `Faculty` — faculty name

### OverarchingTopic
- `name` — topic name (lowercase property!)

### AREA
- `name` — area code (e.g. "BF1", "BWL3")

### Faculty
- `name` — faculty name

## Critical Patterns

### Finding lecturers for a course (MUST go via Event)

There is NO direct StudyModule-to-Person relationship.

```cypher
MATCH (sm:StudyModule)-[:HAS_EVENT]->(e:Event)-[:TAUGHT_BY]->(p:Person)
WHERE sm.Id = $courseId
RETURN DISTINCT p.Name
```

### Semester filtering

Session codes: `"003"` = Autumn (HS), `"004"` = Spring (FS).

```cypher
WHERE sm.Session = "004" AND sm.Year = 2026
```

## Working Example Queries

### 1. Count courses per semester

```cypher
MATCH (sm:StudyModule)
RETURN sm.Year, sm.Session, count(sm) AS course_count
ORDER BY sm.Year DESC, sm.Session
```

### 2. All lecturers for a specific course

```cypher
MATCH (sm:StudyModule)-[:HAS_EVENT]->(e:Event)-[:TAUGHT_BY]->(p:Person)
WHERE sm.SmText CONTAINS $courseName
RETURN DISTINCT sm.SmText, p.Name
```

### 3. Courses per topic

```cypher
MATCH (t:OverarchingTopic)-[:HAS_TOPIC]->(sm:StudyModule)
RETURN t.name AS topic, count(sm) AS course_count
ORDER BY course_count DESC
```

### 4. Courses in a specific area

```cypher
MATCH (sm:StudyModule)-[:HAS_AREA]->(a:AREA)
WHERE a.name = $areaCode
RETURN sm.SmText, sm.Points, sm.Year, sm.Session
ORDER BY sm.Year DESC
```

### 5. Lecturers teaching in multiple fields

```cypher
MATCH (sm:StudyModule)-[:HAS_EVENT]->(e:Event)-[:TAUGHT_BY]->(p:Person),
      (sm)-[:PART_OF]->(f:Field)
WITH p, collect(DISTINCT f.Text) AS fields
WHERE size(fields) > 1
RETURN p.Name, fields, size(fields) AS field_count
ORDER BY field_count DESC
```

### 6. Average ECTS by field

```cypher
MATCH (sm:StudyModule)-[:PART_OF]->(f:Field)
WHERE sm.Points IS NOT NULL
RETURN f.Text AS field, round(avg(sm.Points), 1) AS avg_ects, count(sm) AS courses
ORDER BY avg_ects DESC
```

### 7. Degree program -> fields -> courses traversal

```cypher
MATCH (dp:DegreeProgram)<-[:BELONGS_TO]-(f:Field)<-[:PART_OF]-(sm:StudyModule)
WHERE dp.Text CONTAINS $programName
RETURN dp.Text, f.Text AS field, count(sm) AS courses
ORDER BY courses DESC
```

### 8. Event schedule for a course

```cypher
MATCH (sm:StudyModule)-[:HAS_EVENT]->(e:Event)
WHERE sm.Id = $courseId
RETURN e.Evdat, e.EvStartTime, e.EvEndTime, e.Room, e.CatSort
ORDER BY e.Evdat
```

### 9. All topics with course counts

```cypher
MATCH (t:OverarchingTopic)-[:HAS_TOPIC]->(sm:StudyModule)
RETURN t.name AS topic, count(sm) AS courses
ORDER BY courses DESC
```

### 10. Courses with specific language

```cypher
MATCH (sm:StudyModule)
WHERE sm.Language = $language AND sm.Year = $year
RETURN sm.SmText, sm.Points, sm.Session
ORDER BY sm.SmText
```
