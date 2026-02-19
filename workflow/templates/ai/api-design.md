# API Design

---

## Conventions

- **Base URL:** `/api/v1`
- **Auth:** `Authorization: Bearer <token>`
- **Content-Type:** `application/json`
- **Errors:** `{ "error": { "code": "ERROR_CODE", "message": "Human-readable message" } }`

---

## HTTP Status Codes

| Status | When |
|--------|------|
| 200 OK | GET, PATCH, PUT success |
| 201 Created | POST success |
| 204 No Content | DELETE success |
| 400 Bad Request | Validation error |
| 401 Unauthorized | Missing/invalid auth |
| 403 Forbidden | Insufficient permissions |
| 404 Not Found | Resource not found |
| 409 Conflict | Business rule violation |

---

## Endpoints

### [Resource]

#### GET /[resource]

**Use case:** [UC name] | **Auth:** Required

**Query params:** `page` (default: 1), `per_page` (default: 20)

**Response 200:**
```json
{
  "data": [
    { "id": 1, "[field]": "[value]" }
  ],
  "meta": { "page": 1, "per_page": 20, "total": 45 }
}
```

---

#### GET /[resource]/:id

**Use case:** [UC name] | **Auth:** Required

**Response 200:**
```json
{ "id": 1, "[field]": "[value]" }
```

**Errors:** `NOT_FOUND` 404

---

#### POST /[resource]

**Use case:** [UC name] | **Auth:** Required

**Request:**
```json
{ "[field]": "[value]" }
```

**Response 201:**
```json
{ "id": 1, "[field]": "[value]" }
```

**Errors:** `VALIDATION_ERROR` 400

---

#### PATCH /[resource]/:id

**Use case:** [UC name] | **Auth:** Required

**Request:**
```json
{ "[field]": "[updated value]" }
```

**Response 200:**
```json
{ "id": 1, "[field]": "[updated value]" }
```

**Errors:** `NOT_FOUND` 404, `VALIDATION_ERROR` 400

---

#### DELETE /[resource]/:id

**Use case:** [UC name] | **Auth:** Required

**Response:** 204 No Content

**Errors:** `NOT_FOUND` 404

---

### Auth

#### POST /auth/login

**Auth:** None

**Request:**
```json
{ "email": "user@example.com", "password": "secret" }
```

**Response 200:**
```json
{ "token": "jwt-token", "user": { "id": 1, "email": "user@example.com" } }
```

**Errors:** `INVALID_CREDENTIALS` 401

---

## View-Endpoint Mapping

| View | Endpoint | Request | Response Shape |
|------|----------|---------|----------------|
| [view.html] | GET /[resource] | — | `{ data: [...], meta: {...} }` |
| [view.html] | POST /[resource] | `{ field: val }` | `{ id, field }` |
| [view.html] | PATCH /[resource]/:id | `{ field: val }` | `{ id, field }` |
| [view.html] | DELETE /[resource]/:id | — | 204 |

---

*Generated: [Date]*
*Stage: 2-3 - Endpoint Design*
*Input: use-cases.md, entity-map.md, data-model-physical.md, views/*
