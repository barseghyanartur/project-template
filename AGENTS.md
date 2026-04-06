# AGENTS.md — {{ project_name }}

**Package version**: See pyproject.toml
**Repository**: https://github.com/{{ github_username }}/{{ github_repo }}
**Maintainer**: {{ author_name }} <{{ author_email }}>

This file is for AI agents and developers using AI assistants to work on or with
{{ project_name }}. It covers two distinct roles: **using** the package in application code,
and **developing/extending** the package itself.

---

## Placeholder Legend

Use these tokens throughout all files — search-and-replace to bootstrap a new project:

| Token | Example | Notes |
|---|---|---|
| `{{ project_name }}` | `my-cool-library` | kebab-case |
| `{{ package_name }}` | `my_cool_library` | Python identifier |
| `{{ ErrorBaseClass }}` | `MyLibError` | PascalCase, your exception base |
| `{{ author_name }}` | `Jane Doe` | |
| `{{ author_email }}` | `jane@example.com` | |
| `{{ github_username }}` | `janedoe` | |
| `{{ github_repo }}` | `my-cool-library` | |
| `{{ current_year }}` | `2026` | |

---

## 1. Project Mission (Never Deviate)

> {{ project_description }}

.. TODO: Replace with your project's mission statement.

- Example principle 1.
- Example principle 2.
- Example principle 3.

---

## 2. Using {{ project_name }} in Application Code

### Simple case

<!-- pytestfixture: my_fixture -->
```python name=test_simple_case
from {{ package_name }} import main_function

main_function("example input")
```

### With custom configuration

<!-- pytestfixture: my_fixture -->
```python name=test_with_config
from {{ package_name }} import MainClass

instance = MainClass(config_value=100)
result = instance.run(data)
```

### Exception handling

All {{ project_name }} exceptions inherit from `{{ ErrorBaseClass }}`:

<!-- pytestfixture: my_fixture -->
```python name=test_exception_handling
from {{ package_name }} import (
    main_function,
    {{ ErrorBaseClass }},
    SpecificError1,
    SpecificError2,
)

try:
    main_function("input")
except SpecificError1:
    ...
except SpecificError2:
    ...
except {{ ErrorBaseClass }}:
    # catch-all for any {{ project_name }} error
    ...
```

### Configuration reference

.. TODO: Document your configuration options.

| Parameter | Type | Default |
|---|---|---|
| `param1` | str | "default" |
| `param2` | int | 100 |

---

## 3. Architecture

.. TODO: Document your architecture here.

| Component | File | Purpose |
|---|---|---|
| Core | `_core.py` | Main logic |
| Module 1 | `_module1.py` | Feature X |

### Key files

| File | Purpose |
|---|---|
| `src/{{ package_name }}/_core.py` | Main implementation |
| `src/{{ package_name }}/_module1.py` | Feature X |
| `pyproject.toml` | Build and tool configuration |
| `README.rst` | Usage documentation |

---

## 4. Development Principles

.. TODO: Document your development principles.

**1. Principle one.**
    Explanation of why this principle matters.

**2. Principle two.**
    Explanation of why this principle matters.

**3. Principle three.**
    Explanation of why this principle matters.

---

## 5. Known Intentional Behaviors — Do Not Treat as Bugs

.. TODO: Document any intentional behaviors that might seem unusual.

### Behavior 1

Explanation of why this behavior is intentional.

### Behavior 2

Explanation of why this behavior is intentional.

---

## 6. Agent Workflow: Adding Features or Fixing Bugs

When asked to add a feature or fix a bug, follow these steps in order:

1. **Understand the scope** — Does the change fit the project mission?
2. **Identify the correct module** — Where should the change live?
3. **For bug fixes: write the regression test first** — The test must fail before your fix.
4. **Implement the change** in the correct file.
5. **Add/update exceptions** in `_exceptions.py` if needed.
6. **Export** new public symbols from `__init__.py` and `__all__`.
7. **Write tests:**
   - Unit test in the relevant `test_*.py` file.
   - Integration test if applicable.
   - Test for the legitimate-input happy path.
8. **Update documentation** if you modify the public API.
9. **Run tests:** `make test-env ENV=py312` or `make test` for full matrix.
10. **Run linting:** `make pre-commit`.

### Acceptable new features

.. TODO: List acceptable new features.

- Feature type A.
- Feature type B.

### Forbidden

.. TODO: List forbidden changes.

- Adding external dependencies.
- Removing core functionality.
- Weakening security defaults (if applicable).

---

## 7. Testing Rules

### All tests must run inside Docker

```sh
make test                   # full matrix (Python 3.10–3.14)
make test-env ENV=py312     # single version
make shell                  # interactive shell
```

### Test layout

```text
src/{{ package_name }}/tests/
    conftest.py          — test fixtures
    test_module1.py
    test_module2.py
```

The **root `conftest.py`** (project root) is for `pytest-codeblock` documentation
testing only. Do not add unit test fixtures there.

### Required assertions

```python
# 1. pytest.raises wraps the full operation
with pytest.raises(SpecificError):
    result = function_under_test(input_data)

# 2. Verify the error has expected properties
assert result.error_code == expected_code
```

---

## 8. Coding Conventions

Run all linting checks:

```sh
make pre-commit
```

### Formatting

- Line length: **88 characters** (ruff).
- Import sorting: `isort`.
- Target: `py310`.

### Ruff rules in effect

`B`, `C4`, `E`, `F`, `G`, `I`, `ISC`, `INP`, `N`, `PERF`, `Q`, `SIM`.

### Style

- Every non-test module must have `__all__`, `__author__`, `__copyright__`,
  `__license__` at module level.
- Type annotations on all public functions.
- Chain exceptions: `raise X(...) from exc`.

### Pull requests

Target the `dev` branch only. Never open a PR directly to `main`.

---

## 9. Prompt Templates

**Explaining usage to a user:**
> You are an expert in {{ project_name }}. Explain how to use {{ project_name }}
> for [task]. Start with secure/complete defaults. Include exception handling.

**Implementing a new feature:**
> Extend {{ project_name }} with [feature]. Follow the AGENTS.md agent workflow:
> write the regression test first, implement, add tests, update README.

**Fixing a bug:**
> Reproduce [bug] with a new test. The test must fail before the fix.
> Then fix in the correct module. Add tests asserting correct behavior
> and that legitimate use cases still work.

**Reviewing a change:**
> Review this {{ project_name }} change against AGENTS.md: Does it preserve
> core principles? Does it follow the testing and coding conventions?
