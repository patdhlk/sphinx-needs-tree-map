# Task Management System - Example Documentation

This directory contains an example Sphinx documentation project that demonstrates
the **sphinx-needs-tree-map** extension for creating interactive treemap
visualizations of sphinx-needs data.

## Project Overview

The example project is a fictional "Task Management System" that includes:

- **7 System Requirements** - High-level system requirements (performance, security, scalability)
- **5 User Management Requirements** - User registration, authentication, and RBAC
- **7 Task Management Requirements** - Core task functionality
- **3 User Stories** - User-focused feature descriptions
- **7 API Specifications** - Technical API specifications
- **6 Database Specifications** - Schema design specifications
- **10 Test Cases** - Verification test cases

Total: **45+ needs** demonstrating various statuses, links, and attributes.

## Directory Structure

```
example/
├── docs/
│   ├── conf.py                    # Sphinx configuration
│   ├── index.rst                  # Main documentation index
│   ├── visualizations.rst         # Comprehensive treemap examples
│   ├── requirements/
│   │   ├── index.rst
│   │   ├── system.rst             # System requirements
│   │   ├── user_management.rst    # User requirements and stories
│   │   └── task_management.rst    # Task requirements and stories
│   ├── specifications/
│   │   ├── index.rst
│   │   ├── api.rst                # API specifications
│   │   └── database.rst           # Database schema specifications
│   └── test_plan/
│       ├── index.rst
│       ├── authentication_tests.rst
│       └── task_tests.rst
├── Makefile
├── requirements.txt
└── README.md
```

## Need Types

The example uses five need types:

| Type | Prefix | Description |
|------|--------|-------------|
| `req` | REQ_ | Requirements |
| `spec` | SPEC_ | Specifications |
| `impl` | IMPL_ | Implementations |
| `test` | TC_ | Test Cases |
| `story` | US_ | User Stories |

## Status Values

The example uses four status values:

| Status | Description |
|--------|-------------|
| `open` | Not yet started |
| `in_progress` | Work in progress |
| `implemented` | Implementation complete |
| `verified` | Tested and verified |

## Traceability

The example demonstrates traceability through link relationships:

```
User Story (US_)
    └── Requirement (REQ_)
            └── Specification (SPEC_)
                    └── Test Case (TC_)
```

## Treemap Hierarchy Modes

The example demonstrates all three hierarchy modes:

### Document Mode (`hierarchy: document`)
Organizes needs by their location in documentation:
- Documentation root
  - Document
    - Section
      - Need

### Links Mode (`hierarchy: links`)
Organizes needs by traceability relationships:
- Root requirements (no incoming links)
  - Child specifications (linked to requirements)
    - Test cases (linked to specifications)

### Type Mode (`hierarchy: type`)
Organizes needs by type and status:
- Need Type (e.g., "Requirements")
  - Status (e.g., "Open", "Verified")
    - Individual needs

## Building the Documentation

### Prerequisites

1. Python 3.9 or later
2. [uv](https://docs.astral.sh/uv/) package manager

### Install Dependencies

```bash
cd example
uv sync
```

This will install all dependencies including sphinx-needs-tree-map from the parent directory.

### Build

```bash
make html
```

The built documentation will be in `_build/html/`. Open `_build/html/index.html`
in your browser to view.

### Live Reload (Development)

For development with automatic rebuilding:

```bash
uv sync --group dev
make livehtml
```

## Key Files to Explore

1. **ubproject.toml** - sphinx-needs configuration (types, links, statuses)
2. **conf.py** - Sphinx and sphinx-needs-tree-map configuration
3. **visualizations.rst** - Comprehensive examples of all treemap options
4. **requirements/*.rst** - Examples of requirements with various statuses and links
5. **specifications/*.rst** - Derived specifications with traceability links
6. **test_plan/*.rst** - Test cases that verify requirements and specifications

## Configuration Structure

This example uses the recommended split configuration approach:

### ubproject.toml (sphinx-needs configuration)

All sphinx-needs specific settings are in `ubproject.toml`:

```toml
[needs]
id_regex = "^[A-Z]+_[A-Z]+_[0-9]+"
extra_options = ["priority", "version", "component"]

types = [
    { directive = "req", title = "Requirement", prefix = "REQ_", color = "#BFD8D2", style = "node" },
    { directive = "spec", title = "Specification", prefix = "SPEC_", color = "#FEDCD2", style = "node" },
    # ...
]

extra_links = [
    { option = "implements", incoming = "is implemented by", outgoing = "implements" },
    # ...
]

statuses = [
    { name = "open", description = "Not yet started" },
    # ...
]
```

### conf.py (Sphinx and treemap configuration)

The `conf.py` loads sphinx-needs config from TOML and sets sphinx-needs-tree-map options:

```python
# Load sphinx-needs configuration from ubproject.toml
needs_from_toml = "ubproject.toml"

# sphinx-needs-tree-map colors
needtreemap_colors = {
    "req": "#E3F2FD",
    "spec": "#FFF3E0",
    # ...
}
```

## Customization

### Modifying Need Types

Edit `types` in `ubproject.toml`:

```toml
types = [
    { directive = "req", title = "Requirement", prefix = "REQ_", color = "#BFD8D2", style = "node" },
]
```

### Treemap Colors

Edit `needtreemap_colors` in `conf.py` to change type colors:

```python
needtreemap_colors = {
    "req": "#E3F2FD",
    "spec": "#FFF3E0",
    "test": "#FFF9C4",
    "default": "#ECEFF1",
}
```

### Status Colors

Edit `needtreemap_status_colors` in `conf.py` to change status colors:

```python
needtreemap_status_colors = {
    "open": "#FFCDD2",
    "in_progress": "#FFE0B2",
    "implemented": "#C8E6C9",
    "verified": "#B2DFDB",
}
```

## License

This example is provided under the same license as the sphinx-needs-tree-map
extension.
