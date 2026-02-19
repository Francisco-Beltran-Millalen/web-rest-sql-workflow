# Data Model — Physical (SQLite)

---

## Type Mapping

| Conceptual | SQLite |
|------------|--------|
| identifier | INTEGER PRIMARY KEY AUTOINCREMENT |
| text | TEXT |
| number (int) | INTEGER |
| number (decimal) | REAL |
| boolean | INTEGER (0=false, 1=true) |
| date/datetime | TEXT (ISO 8601) |
| enum | TEXT |

---

## Schema

### [entity] table

| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| [col] | TEXT | NOT NULL |
| [col] | INTEGER | NOT NULL DEFAULT 0 |
| [col] | TEXT | UNIQUE NOT NULL |
| created_at | DATETIME | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| updated_at | DATETIME | NOT NULL DEFAULT CURRENT_TIMESTAMP |

**Foreign keys:**
- `[col]` → `[other_table].id` (ON DELETE CASCADE)

**Indexes:**
- `idx_[entity]_[col]` on `[col]` — [reason]

---

### [entity] table

| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| [col] | TEXT | NOT NULL |
| [fk_col] | INTEGER | NOT NULL REFERENCES [other_table](id) ON DELETE RESTRICT |
| created_at | DATETIME | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| updated_at | DATETIME | NOT NULL DEFAULT CURRENT_TIMESTAMP |

**Indexes:**
- `idx_[entity]_[fk_col]` on `[fk_col]` — foreign key lookup

---

## Mock Data

Minimum 4 rows per table. See `docs/assets/schema.sql` for full INSERT statements.

---

*Generated: [Date]*
*Stage: 2-2 - Data Modeling*
*Input: data-model-conceptual.md, tech-stack.md*
