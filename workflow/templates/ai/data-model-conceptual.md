# Data Model — Conceptual

Technology-agnostic. No SQL types, no primary keys, no timestamps.

---

## Entities

### [Entity Name]

**Description:** [What this represents in the domain]

| Attribute | Type (Generic) | Required | Description |
|-----------|---------------|----------|-------------|
| [attr] | text | Yes | [desc] |
| [attr] | number | No | [desc] |
| [attr] | boolean | Yes | [desc] |
| [attr] | date | No | [desc] |
| [attr] | enum([A], [B]) | Yes | [desc] |

**Relationships:**
- [field] → [Entity] (N:1) — [description]
- [field] → [Entity] (1:N) — [description]

---

### [Entity Name]

**Description:** [What this represents]

| Attribute | Type (Generic) | Required | Description |
|-----------|---------------|----------|-------------|
| [attr] | text | Yes | [desc] |

**Relationships:**
- [field] → [Entity] (N:M) — [description]

---

## Enums

### [EnumName]
| Value | Description |
|-------|-------------|
| [VALUE] | [Description] |
| [VALUE] | [Description] |

---

## Entity Relationship Diagram

```mermaid
erDiagram
    [EntityA] ||--o{ [EntityB] : [relationship]
    [EntityB] }o--|| [EntityC] : [relationship]
```

---

*Generated: [Date]*
*Stage: 2-2 - Data Modeling*
*Input: entity-map.md*
