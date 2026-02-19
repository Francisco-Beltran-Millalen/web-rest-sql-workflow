# Entity Map

## Overview

This document captures the conceptual entities and their relationships, without implementation details.

---

## Entities

[List of all entities discovered]

### Core Entities

- **[Entity 1]**: [Brief description of what it represents]
- **[Entity 2]**: [Brief description]
- **[Entity 3]**: [Brief description]

### Supporting Entities

- **[Entity 4]**: [Brief description]
- **[Entity 5]**: [Brief description]

---

## Relationships

[How entities connect to each other]

| Entity A | Relationship | Entity B | Cardinality |
|----------|--------------|----------|-------------|
| [Entity] | [verb phrase] | [Entity] | 1:1 / 1:many / many:many |
| [Entity] | [verb phrase] | [Entity] | 1:1 / 1:many / many:many |

### Relationship Descriptions

- **[Entity A] → [Entity B]**: [Description in plain language]
- **[Entity A] → [Entity B]**: [Description]

---

## Entity Map (Textual)

```
[Entity 1]
 ├── [relationship] → [Entity 2] (cardinality)
 ├── [relationship] → [Entity 3] (cardinality)
 └── [relationship] → [Entity 4] (cardinality)

[Entity 2]
 └── [relationship] → [Entity 5] (cardinality)

[Entity 3]
 └── [relationship] → [Entity 5] (cardinality)
```

---

## Ownership & Lifecycle

[What happens when entities are created/deleted]

| If This Is Deleted | What Happens To Related Entities |
|--------------------|----------------------------------|
| [Entity] | [Entity B] is also deleted / orphaned / preserved |
| [Entity] | [Description] |

---

## Observations

[Any notes about boundaries, coupling, or design considerations]

- [Observation 1]
- [Observation 2]

---

*Generated: [Date]*
*Stage: 2-1 - Entity & UI Sketching*
*Input: use-cases.md*
