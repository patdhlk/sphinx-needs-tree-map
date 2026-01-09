======================
Authentication Tests
======================

This document contains test cases for authentication and user management
functionality.

User Registration Tests
=======================

.. test:: Valid User Registration
   :id: TC_AUTH_001
   :status: verified
   :tags: authentication, registration, positive
   :priority: high
   :version: 1.0
   :links: REQ_USER_001, SPEC_API_006

   **Objective**: Verify that users can successfully register with valid data.

   **Preconditions**:

   * Email address is not already registered
   * System is accessible

   **Test Steps**:

   1. Navigate to registration page
   2. Enter valid email address
   3. Enter password meeting complexity requirements
   4. Enter display name
   5. Submit registration form
   6. Check email inbox for verification link
   7. Click verification link

   **Expected Results**:

   * Registration form accepts valid data
   * Verification email is sent within 1 minute
   * Account is activated after email verification
   * User can log in with registered credentials

.. test:: Invalid Email Registration
   :id: TC_AUTH_002
   :status: verified
   :tags: authentication, registration, negative
   :priority: medium
   :version: 1.0
   :links: REQ_USER_001

   **Objective**: Verify that registration rejects invalid email formats.

   **Test Data**:

   * ``invalid-email`` (no @ symbol)
   * ``user@`` (no domain)
   * ``@domain.com`` (no local part)
   * ``user@domain`` (no TLD)

   **Expected Results**:

   * Form displays validation error
   * Registration is not submitted
   * No verification email is sent

.. test:: Weak Password Rejection
   :id: TC_AUTH_003
   :status: implemented
   :tags: authentication, password, negative
   :priority: high
   :version: 1.0
   :links: REQ_USER_002

   **Objective**: Verify that weak passwords are rejected.

   **Test Data**:

   * ``short`` (less than 12 characters)
   * ``alllowercase1!`` (no uppercase)
   * ``ALLUPPERCASE1!`` (no lowercase)
   * ``NoNumbers!abc`` (no digits)
   * ``NoSpecial123abc`` (no special characters)

   **Expected Results**:

   * Each weak password is rejected
   * Specific validation message indicates the missing requirement
   * Form does not submit until password meets all requirements

Authentication Tests
====================

.. test:: Successful Login
   :id: TC_AUTH_004
   :status: verified
   :tags: authentication, login, positive
   :priority: high
   :version: 1.0
   :links: REQ_SYS_003, SPEC_API_001

   **Objective**: Verify that registered users can log in successfully.

   **Preconditions**:

   * User account exists and is verified
   * User knows correct password

   **Test Steps**:

   1. Navigate to login page
   2. Enter registered email address
   3. Enter correct password
   4. Submit login form

   **Expected Results**:

   * User is authenticated
   * Access token is returned
   * User is redirected to dashboard
   * Session is established

.. test:: Invalid Credentials Login
   :id: TC_AUTH_005
   :status: verified
   :tags: authentication, login, negative
   :priority: high
   :version: 1.0
   :links: REQ_SYS_003, SPEC_API_001

   **Objective**: Verify that login fails with invalid credentials.

   **Test Cases**:

   * Valid email, wrong password
   * Invalid email format
   * Non-existent email
   * Empty email or password

   **Expected Results**:

   * Login is rejected
   * Generic error message (does not reveal if email exists)
   * No token is issued
   * Failed attempt is logged

.. test:: Session Timeout
   :id: TC_AUTH_006
   :status: in_progress
   :tags: authentication, session, security
   :priority: medium
   :version: 1.0
   :links: REQ_SYS_005

   **Objective**: Verify that sessions expire after 30 minutes of inactivity.

   **Test Steps**:

   1. Log in successfully
   2. Wait 30 minutes without any activity
   3. Attempt to access a protected resource

   **Expected Results**:

   * Session is terminated
   * User is redirected to login page
   * Appropriate message indicates session expiration
   * User must re-authenticate

Token Management Tests
======================

.. test:: Token Refresh
   :id: TC_AUTH_007
   :status: implemented
   :tags: authentication, token, positive
   :priority: medium
   :version: 1.0
   :links: SPEC_API_001, SPEC_API_002

   **Objective**: Verify that access tokens can be refreshed.

   **Test Steps**:

   1. Obtain initial access token and refresh token
   2. Wait for access token to expire (or use nearly-expired token)
   3. Call refresh endpoint with refresh token
   4. Use new access token for API request

   **Expected Results**:

   * New access token is issued
   * New refresh token is issued (rotation)
   * Old refresh token is invalidated
   * API request succeeds with new token

.. test:: Token Revocation
   :id: TC_AUTH_008
   :status: open
   :tags: authentication, token, security
   :priority: medium
   :version: 1.0
   :links: SPEC_API_001

   **Objective**: Verify that tokens can be revoked (logout).

   **Test Steps**:

   1. Obtain access token and refresh token
   2. Call revoke endpoint with access token
   3. Attempt to use revoked access token
   4. Attempt to use associated refresh token

   **Expected Results**:

   * Revocation succeeds
   * Access token is no longer valid
   * Refresh token is no longer valid
   * API requests return 401 Unauthorized
