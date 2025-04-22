# Join - Task Management API

A Django REST API for task and contact management with user authentication.

## Features

- User authentication (register, login, guest login)
- Task management with kanban board categories (Todo, In Progress, Await Feedback, Done)
- Contact management
- RESTful API endpoints

## Technologies

- Django 5.2
- Django REST Framework 3.16.0
- Token-based authentication
- SQLite database

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/mneisens/Join_Backend
   cd join
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints



### Contacts

- `GET /api/contacts/` - List all contacts
- `POST /api/contacts/` - Create a new contact
- `GET /api/contacts/{id}/` - Retrieve a contact
- `PUT /api/contacts/{id}/` - Update a contact
- `DELETE /api/contacts/{id}/` - Delete a contact

### Tasks

- `GET /api/tasks/` - List all tasks
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/{id}/` - Retrieve a task
- `PUT /api/tasks/{id}/` - Update a task
- `DELETE /api/tasks/{id}/` - Delete a task
- `GET /api/tasks/by_kanban_category/` - Get tasks grouped by kanban category
- `PATCH /api/tasks/{id}/update_category/` - Update the kanban category of a task

## Data Models

### User
Standard Django user model with authentication capabilities.

### Contact
- User (ForeignKey)
- Name
- Email
- Phone (optional)
- Color (optional)
- Initials (optional)
- Created At

### Task
- User (ForeignKey)
- Header
- Description
- Due Date
- Priority (urgent, medium, low)
- Category (Technical Task, User Story)
- Kanban Category (Todo, InProgress, AwaitFeedback, Done)
- Assigned To (ManyToMany to Contact, optional)
- Created At

### Subtask
- Task (ForeignKey)
- Subtask
- Done (Boolean)

## Authentication

The API uses token-based authentication. Include the token in the Authorization header:

```
Authorization: Token <your-token>
```

## Frontend Integration

The API supports Cross-Origin Resource Sharing (CORS) for localhost:5501 for frontend integration.

## Demo Data

Guest users automatically receive demo contacts and tasks for testing purposes.

## License

[Add your license information here]
