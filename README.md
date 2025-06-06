# Kandji HW for Automation Tests 

This repo contains a UI automation framework using **Selenium + Pytest** for the Kandji web application.


## Structure of the project

- `pages/` → Page Object Model
- `tests/` → Test cases
- `utils/` → Helpers 
- `.github/workflows/` → Added a small CI tool

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


## What is tested?

- Login to the 
- Devices
- Blueprints
- Library, etc.

## Next steps

✅ Add proper authorization  
✅ Add more functinality
✅ Add test reporting (Allure, HTML)  
✅ Add parallel execution support  


