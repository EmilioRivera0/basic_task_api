# Basic Task API

API to manage a to do tasks list.

# API Reference

#### Get all tasks

```http
  GET /api/tasks
```

#### Get informaton of the specified task

```http
  GET /api/tasks/{id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `integer` | **Required**. ID of the task to be retrieved |

#### Append a new task

```http
  POST /api/append
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | **Required**. Name of the task |

#### Delete specified task

```http
  DELETE /api/delete/{id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `integer` | **Required**. ID of the task to be removed |

#### Change the status of a task to completed (True)

```http
  PUT /api/update
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `integer` | **Required**. ID of the task to be updated |

# Deployed API

- https://task-management-api-0ds8.onrender.com/api/tasks

## Tech Stack

**Server:** Flask

## Authors

- [@EmilioRivera0](https://github.com/EmilioRivera0)
