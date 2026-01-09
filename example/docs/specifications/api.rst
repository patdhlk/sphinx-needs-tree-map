==================
API Specifications
==================

This document contains technical specifications for the Task Management System
REST API. These specifications derive from and implement the system requirements.

Authentication API
==================

.. spec:: OAuth 2.0 Authentication Flow
   :id: SPEC_API_001
   :status: verified
   :tags: api, authentication
   :priority: high
   :version: 1.0
   :links: REQ_SYS_003, REQ_USER_001

   The API shall implement OAuth 2.0 authorization code flow for user
   authentication with the following endpoints:

   * ``POST /oauth/authorize`` - Initiate authorization
   * ``POST /oauth/token`` - Exchange code for access token
   * ``POST /oauth/refresh`` - Refresh access token
   * ``POST /oauth/revoke`` - Revoke token

   Access tokens shall expire after 1 hour. Refresh tokens shall expire
   after 30 days or upon explicit revocation.

   **Response Format**::

       {
           "access_token": "eyJhbGciOiJSUzI1NiIs...",
           "token_type": "Bearer",
           "expires_in": 3600,
           "refresh_token": "dGhpcyBpcyBhIHJlZnJlc2g..."
       }

.. spec:: JWT Token Structure
   :id: SPEC_API_002
   :status: implemented
   :tags: api, authentication, jwt
   :priority: high
   :version: 1.0
   :links: REQ_SYS_003, SPEC_API_001

   Access tokens shall be signed JWTs (RS256) containing the following claims:

   * ``sub`` - User ID (UUID)
   * ``email`` - User email address
   * ``roles`` - Array of user roles
   * ``iat`` - Issued at timestamp
   * ``exp`` - Expiration timestamp
   * ``iss`` - Issuer (API domain)

   The API shall validate token signatures using the published JWKS endpoint
   at ``/.well-known/jwks.json``.

Task API
========

.. spec:: Task CRUD Endpoints
   :id: SPEC_API_003
   :status: verified
   :tags: api, tasks
   :priority: high
   :version: 1.0
   :links: REQ_TASK_001, REQ_TASK_002

   The API shall provide RESTful endpoints for task management:

   * ``GET /api/v1/tasks`` - List tasks (with pagination)
   * ``POST /api/v1/tasks`` - Create new task
   * ``GET /api/v1/tasks/{id}`` - Get task by ID
   * ``PUT /api/v1/tasks/{id}`` - Update task
   * ``DELETE /api/v1/tasks/{id}`` - Delete task
   * ``GET /api/v1/tasks/{id}/subtasks`` - List subtasks
   * ``POST /api/v1/tasks/{id}/subtasks`` - Create subtask

   All endpoints shall return JSON and use appropriate HTTP status codes.

.. spec:: Task Search Endpoint
   :id: SPEC_API_004
   :status: implemented
   :tags: api, tasks, search
   :priority: medium
   :version: 1.0
   :links: REQ_TASK_007, REQ_SYS_001

   The API shall provide a search endpoint with Elasticsearch-backed full-text
   search:

   * ``GET /api/v1/tasks/search?q={query}&filters={json}``

   **Query Parameters**:

   * ``q`` - Full-text search query
   * ``filters`` - JSON object with field filters
   * ``sort`` - Sort field and direction
   * ``page`` - Page number (default: 1)
   * ``limit`` - Results per page (default: 20, max: 100)

   Search results shall be returned within 500ms for up to 1 million tasks.

.. spec:: Task Status Transitions
   :id: SPEC_API_005
   :status: in_progress
   :tags: api, tasks, workflow
   :priority: medium
   :version: 1.0
   :links: REQ_TASK_002

   The API shall enforce task status transitions via a dedicated endpoint:

   * ``POST /api/v1/tasks/{id}/transitions``

   **Request Body**::

       {
           "to_status": "in_progress",
           "comment": "Starting work on this task"
       }

   Invalid transitions shall return HTTP 422 with error details.

User API
========

.. spec:: User Management Endpoints
   :id: SPEC_API_006
   :status: implemented
   :tags: api, users
   :priority: high
   :version: 1.0
   :links: REQ_USER_001, REQ_USER_004

   The API shall provide endpoints for user management:

   * ``POST /api/v1/users`` - Register new user
   * ``GET /api/v1/users/me`` - Get current user profile
   * ``PUT /api/v1/users/me`` - Update current user profile
   * ``GET /api/v1/users/{id}`` - Get user by ID (admin only)
   * ``GET /api/v1/users`` - List users (with pagination)

.. spec:: Role Assignment Endpoint
   :id: SPEC_API_007
   :status: open
   :tags: api, users, roles
   :priority: medium
   :version: 1.0
   :links: REQ_USER_003

   The API shall provide an admin-only endpoint for role management:

   * ``PUT /api/v1/users/{id}/roles``

   **Request Body**::

       {
           "roles": ["team_member", "project_manager"]
       }

   Only administrators may modify user roles. The system shall prevent
   removal of the last administrator role.
