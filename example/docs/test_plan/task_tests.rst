==========
Task Tests
==========

This document contains test cases for task management functionality.

Task CRUD Tests
===============

.. test:: Create Task
   :id: TC_TASK_001
   :status: verified
   :tags: tasks, crud, positive
   :priority: high
   :version: 1.0
   :links: REQ_TASK_001, SPEC_API_003

   **Objective**: Verify that authorized users can create tasks.

   **Preconditions**:

   * User is authenticated with Team Member role or higher
   * User has access to at least one project

   **Test Steps**:

   1. Call POST /api/v1/tasks with valid task data
   2. Verify response contains created task
   3. Retrieve task by ID to confirm persistence

   **Test Data**::

       {
           "title": "Implement user dashboard",
           "description": "Create the main user dashboard view",
           "priority": "high",
           "due_date": "2025-02-15"
       }

   **Expected Results**:

   * HTTP 201 Created response
   * Task ID is returned
   * Task can be retrieved by ID
   * Created timestamp is set
   * Status defaults to "open"

.. test:: Update Task Status
   :id: TC_TASK_002
   :status: implemented
   :tags: tasks, workflow, positive
   :priority: high
   :version: 1.0
   :links: REQ_TASK_002, SPEC_API_005

   **Objective**: Verify that task status can be updated through valid transitions.

   **Test Cases**:

   * Open -> In Progress (valid)
   * In Progress -> In Review (valid)
   * In Review -> Done (valid)
   * Done -> Closed (valid)

   **Expected Results**:

   * Each valid transition succeeds
   * Updated timestamp is modified
   * Status history is recorded

.. test:: Invalid Status Transition
   :id: TC_TASK_003
   :status: implemented
   :tags: tasks, workflow, negative
   :priority: medium
   :version: 1.0
   :links: REQ_TASK_002, SPEC_API_005

   **Objective**: Verify that invalid status transitions are rejected.

   **Test Cases**:

   * Open -> Done (skipping steps)
   * Closed -> Open (backward transition)
   * In Review -> Open (backward transition)

   **Expected Results**:

   * HTTP 422 Unprocessable Entity
   * Error message indicates invalid transition
   * Task status remains unchanged

.. test:: Delete Task
   :id: TC_TASK_004
   :status: verified
   :tags: tasks, crud, positive
   :priority: medium
   :version: 1.0
   :links: REQ_TASK_001, SPEC_API_003

   **Objective**: Verify that tasks can be deleted by authorized users.

   **Preconditions**:

   * Task exists
   * User has permission to delete (creator or admin)

   **Test Steps**:

   1. Create a test task
   2. Call DELETE /api/v1/tasks/{id}
   3. Attempt to retrieve deleted task

   **Expected Results**:

   * HTTP 204 No Content on delete
   * GET request returns HTTP 404
   * Subtasks are also deleted (cascade)

Task Assignment Tests
=====================

.. test:: Assign Task to User
   :id: TC_TASK_005
   :status: verified
   :tags: tasks, assignment, positive
   :priority: high
   :version: 1.0
   :links: REQ_TASK_003, SPEC_DB_004

   **Objective**: Verify that tasks can be assigned to valid users.

   **Test Steps**:

   1. Create a task
   2. Update task with assignee user ID
   3. Verify assignment is recorded
   4. Check that assignee can view the task

   **Expected Results**:

   * Assignment succeeds
   * Assignee appears in task details
   * Notification is sent to assignee
   * Task appears in assignee's task list

.. test:: Assign Task to Invalid User
   :id: TC_TASK_006
   :status: implemented
   :tags: tasks, assignment, negative
   :priority: medium
   :version: 1.0
   :links: REQ_TASK_003, REQ_USER_003

   **Objective**: Verify that tasks cannot be assigned to unauthorized users.

   **Test Cases**:

   * Assign to non-existent user ID
   * Assign to user with Guest role (read-only)
   * Assign to deactivated user

   **Expected Results**:

   * HTTP 400 or 422 error
   * Error message indicates invalid assignee
   * Task assignment remains unchanged

Task Hierarchy Tests
====================

.. test:: Create Subtask
   :id: TC_TASK_007
   :status: implemented
   :tags: tasks, hierarchy, positive
   :priority: medium
   :version: 1.0
   :links: REQ_TASK_004, SPEC_API_003, SPEC_DB_003

   **Objective**: Verify that subtasks can be created under parent tasks.

   **Test Steps**:

   1. Create a parent task
   2. Create a subtask with parent_task_id
   3. Retrieve parent task and verify subtask relationship
   4. Retrieve subtasks via dedicated endpoint

   **Expected Results**:

   * Subtask is created with parent reference
   * Parent task shows subtask count
   * Subtasks endpoint returns child tasks
   * Hierarchy can be traversed

.. test:: Parent Status Aggregation
   :id: TC_TASK_008
   :status: in_progress
   :tags: tasks, hierarchy, workflow
   :priority: medium
   :version: 1.0
   :links: REQ_TASK_004

   **Objective**: Verify that parent task status reflects subtask status.

   **Test Scenarios**:

   * All subtasks Open -> Parent shows "Open"
   * Any subtask In Progress -> Parent shows "In Progress"
   * All subtasks Done -> Parent can be marked Done
   * Subtask reopened -> Parent status updates

   **Expected Results**:

   * Parent status automatically reflects aggregate child status
   * Parent cannot be closed while subtasks are open
   * Status changes propagate correctly

Task Search Tests
=================

.. test:: Full-Text Search
   :id: TC_TASK_009
   :status: verified
   :tags: tasks, search, positive
   :priority: medium
   :version: 1.0
   :links: REQ_TASK_007, SPEC_API_004

   **Objective**: Verify that tasks can be found via full-text search.

   **Setup**:

   * Create tasks with known titles and descriptions
   * Index tasks in search engine

   **Test Steps**:

   1. Search for term appearing in task title
   2. Search for term appearing only in description
   3. Search with partial word match
   4. Search with multiple terms

   **Expected Results**:

   * Relevant tasks are returned
   * Results are ranked by relevance
   * Response time is under 500ms
   * Pagination works correctly

.. test:: Search Performance
   :id: TC_TASK_010
   :status: open
   :tags: tasks, search, performance
   :priority: medium
   :version: 1.0
   :links: REQ_TASK_007, REQ_SYS_001

   **Objective**: Verify search performance meets requirements.

   **Setup**:

   * Database contains 1 million tasks
   * Search index is up to date

   **Test Steps**:

   1. Execute 100 search queries with varying complexity
   2. Measure response times
   3. Calculate percentile statistics

   **Expected Results**:

   * P50 response time < 200ms
   * P95 response time < 500ms
   * P99 response time < 1000ms
   * No timeouts or errors
