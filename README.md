# Ikoia Applicant System

A Django-based recruitment platform allowing candidates to apply for jobs and staff to manage applications.

## 🚀 Getting Started

### Prerequisites
*   Python 3.12 or higher
*   pip

### Installation & Bootstrap

1.  **Clone the repository** (if not already done).

2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

5.  **Create an Admin/Staff user** (to access the Staff Panel):
    ```bash
    python manage.py createsuperuser
    ```

### 🏃‍♂️ Running the Application

Start the development server:
```bash
python manage.py runserver
```

*   **Public Application**: Visit `http://127.0.0.1:8000/`
*   **Apply for Developer**: Visit `http://127.0.0.1:8000/apply/dev/`
*   **Staff Panel**: Visit `http://127.0.0.1:8000/staff_panel/` (requires login)

### 🧪 Running Tests

This project uses `pytest` for testing and `pytest-cov` for coverage reports.

**Run all tests:**
```bash
python -m pytest
```

**Run tests with coverage report:**
```bash
python -m pytest --cov=.
```

**Run tests with HTML coverage report (interactive):**
```bash
python -m pytest --cov=. --cov-report=html
# Open htmlcov/index.html in your browser
```

---

## 📂 Project Structure

*   **`applicants/`**: Public-facing app.
    *   `models.py`: Defines the `Applicant` model.
    *   `views.py`: Handles the Home page and Application Form.
    *   `forms.py`: Handles form validation (PDF checks, ID length).
*   **`staff_panel/`**: Internal management app.
    *   `views.py`: Dashboard logic to list and delete applicants.
    *   Protected by `@staff_member_required`.
*   **`tests/`**: Test suite.
    *   `test_applicants.py`: Tests for forms and public views.
    *   `test_staff_panel.py`: Tests for permissions and admin logic.
*   **`config/`**: Main Django configuration settings and URL routing.
*   **`.github/workflows/`**: CI/CD configuration to run tests on Pull Requests.

