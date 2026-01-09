=======================
Database Specifications
=======================

This document contains database schema specifications for the Task Management
System, including table structures, indexes, and constraints.

User Schema
===========

.. spec:: Users Table Schema
   :id: SPEC_DB_001
   :status: verified
   :tags: database, users
   :priority: high
   :version: 1.0
   :links: REQ_USER_001, REQ_USER_004

   The ``users`` table shall store user account information::

       CREATE TABLE users (
           id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
           email VARCHAR(255) NOT NULL UNIQUE,
           password_hash VARCHAR(255) NOT NULL,
           display_name VARCHAR(100) NOT NULL,
           avatar_url VARCHAR(500),
           job_title VARCHAR(100),
           department VARCHAR(100),
           timezone VARCHAR(50) DEFAULT 'UTC',
           email_verified BOOLEAN DEFAULT FALSE,
           created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
           updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
           last_login_at TIMESTAMP WITH TIME ZONE
       );

   **Indexes**:

   * ``idx_users_email`` - Unique index on email for login lookup
   * ``idx_users_department`` - Index on department for filtering

.. spec:: User Roles Schema
   :id: SPEC_DB_002
   :status: implemented
   :tags: database, users, roles
   :priority: high
   :version: 1.0
   :links: REQ_USER_003, SPEC_DB_001

   The ``user_roles`` table shall implement many-to-many role assignments::

       CREATE TABLE roles (
           id SERIAL PRIMARY KEY,
           name VARCHAR(50) NOT NULL UNIQUE,
           description TEXT,
           permissions JSONB DEFAULT '[]'
       );

       CREATE TABLE user_roles (
           user_id UUID REFERENCES users(id) ON DELETE CASCADE,
           role_id INTEGER REFERENCES roles(id) ON DELETE CASCADE,
           granted_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
           granted_by UUID REFERENCES users(id),
           PRIMARY KEY (user_id, role_id)
       );

   Default roles: ``administrator``, ``project_manager``, ``team_member``, ``guest``

Task Schema
===========

.. spec:: Tasks Table Schema
   :id: SPEC_DB_003
   :status: verified
   :tags: database, tasks
   :priority: high
   :version: 1.0
   :links: REQ_TASK_001, REQ_TASK_002, REQ_TASK_004

   The ``tasks`` table shall store task data with self-referential hierarchy::

       CREATE TABLE tasks (
           id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
           title VARCHAR(500) NOT NULL,
           description TEXT,
           status VARCHAR(50) NOT NULL DEFAULT 'open',
           priority VARCHAR(20) NOT NULL DEFAULT 'medium',
           due_date DATE,
           parent_task_id UUID REFERENCES tasks(id) ON DELETE CASCADE,
           created_by UUID REFERENCES users(id) NOT NULL,
           created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
           updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
           closed_at TIMESTAMP WITH TIME ZONE,
           CONSTRAINT chk_priority CHECK (
               priority IN ('low', 'medium', 'high', 'critical')
           ),
           CONSTRAINT chk_status CHECK (
               status IN ('open', 'in_progress', 'in_review', 'done', 'closed')
           )
       );

   **Indexes**:

   * ``idx_tasks_status`` - For filtering by status
   * ``idx_tasks_priority`` - For filtering by priority
   * ``idx_tasks_due_date`` - For due date queries
   * ``idx_tasks_parent`` - For hierarchy traversal
   * ``idx_tasks_created_by`` - For user's created tasks

.. spec:: Task Assignments Schema
   :id: SPEC_DB_004
   :status: implemented
   :tags: database, tasks, assignment
   :priority: high
   :version: 1.0
   :links: REQ_TASK_003, SPEC_DB_003

   The ``task_assignments`` table shall support multiple assignees per task::

       CREATE TABLE task_assignments (
           task_id UUID REFERENCES tasks(id) ON DELETE CASCADE,
           user_id UUID REFERENCES users(id) ON DELETE CASCADE,
           assigned_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
           assigned_by UUID REFERENCES users(id),
           PRIMARY KEY (task_id, user_id)
       );

   **Indexes**:

   * ``idx_assignments_user`` - For user's assigned tasks lookup

.. spec:: Task Comments Schema
   :id: SPEC_DB_005
   :status: in_progress
   :tags: database, tasks, comments
   :priority: medium
   :version: 1.0
   :links: REQ_TASK_005, SPEC_DB_003

   The ``task_comments`` table shall store task comments with mentions::

       CREATE TABLE task_comments (
           id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
           task_id UUID REFERENCES tasks(id) ON DELETE CASCADE,
           author_id UUID REFERENCES users(id) NOT NULL,
           content TEXT NOT NULL,
           mentions UUID[] DEFAULT '{}',
           created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
           updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
       );

   **Indexes**:

   * ``idx_comments_task`` - For loading task comments
   * ``idx_comments_author`` - For user's comments
   * ``idx_comments_mentions`` - GIN index for mention lookups

Audit Schema
============

.. spec:: Audit Log Schema
   :id: SPEC_DB_006
   :status: open
   :tags: database, audit
   :priority: medium
   :version: 1.1
   :links: REQ_SYS_004

   The ``audit_log`` table shall track all data modifications::

       CREATE TABLE audit_log (
           id BIGSERIAL PRIMARY KEY,
           table_name VARCHAR(100) NOT NULL,
           record_id UUID NOT NULL,
           action VARCHAR(20) NOT NULL,
           old_values JSONB,
           new_values JSONB,
           user_id UUID REFERENCES users(id),
           ip_address INET,
           user_agent TEXT,
           created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
       );

   The audit log shall be append-only with no UPDATE or DELETE operations
   permitted. Partition by month for performance.
