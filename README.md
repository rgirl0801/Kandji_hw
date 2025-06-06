# Kandji UI Automation Tests (Selenium + Pytest)

This repo contains a UI automation framework using **Selenium + Pytest** for the Kandji web application.

## Why Selenium + Python?

- Selenium is a proven, stable, cross-browser framework
- Pytest makes tests readable and scalable
- Works great with CI/CD pipelines

## Structure

- `pages/` → Page Object Model
- `tests/` → Test cases
- `utils/` → Helpers (config)
- `.github/workflows/` → Example GitHub Actions config

## Running Locally

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run smoke test:

    ```bash
    pytest -m smoke
    ```

## CI/CD Integration

- GitHub Actions config provided.
- Works in any pipeline: GitHub Actions, GitLab, CircleCI, Jenkins.

## What is tested?

- Login to Kandji
- Verify that Dashboard is displayed

## Next steps

✅ Add API integration using Kandji API  
✅ Add more Page Objects (Devices, Blueprints, Library, etc.)  
✅ Add test reporting (Allure, HTML)  
✅ Add parallel execution support  
✅ Use CI Secrets to manage credentials  

