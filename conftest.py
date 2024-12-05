import pytest
import os
import shutil
import subprocess
from playwright.sync_api import sync_playwright
from test.page_objects.edWise.common_page import Common
import allure


@pytest.fixture(scope='session', autouse=True)
def setup_artifacts_dir():
    """Set up artifacts and allure directories."""
    artifacts_dir = "artifacts"
    allure_results_dir = os.path.join(artifacts_dir, "allure-results")
    allure_report_dir = os.path.join(artifacts_dir, "allure-report")

    # Clear and recreate the artifacts directory
    if os.path.exists(artifacts_dir):
        shutil.rmtree(artifacts_dir)
        print(f"'{artifacts_dir}' folder cleared.")

    os.makedirs(allure_results_dir)
    os.makedirs(allure_report_dir)
    print(f"'{artifacts_dir}' and its subdirectories created.")

    return allure_results_dir, allure_report_dir


@pytest.fixture(scope='session')
def browser(request):
    """Session-scoped fixture to launch a browser."""
    with sync_playwright() as p:
        # Use environment variable or default value for headless mode
        headless_mode = request.config.getoption("--headless")
        try:
            browser = p.chromium.launch(
                headless=headless_mode,
                args=['--start-maximized']
            )
            yield browser
        except Exception as e:
            print(f"Error launching browser: {e}")
            raise
        finally:
            browser.close()


@pytest.fixture(scope="function")
def page(request, browser):
    """Function-scoped fixture to create a new page."""
    context = browser.new_context()
    page = context.new_page()

    try:
        Common.load_url(page)  # Load a predefined URL
        yield page
    finally:
        context.close()


def pytest_addoption(parser):
    """Add CLI options for headless mode and Allure results directory."""
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode"
    )


def pytest_configure(config):
    """Configure pytest to store Allure results in the artifacts directory."""
    artifacts_dir = "artifacts/allure-results"
    config.option.allure_report_dir = artifacts_dir


def pytest_sessionfinish(session, exitstatus):
    """Generate the Allure report after tests complete."""
    allure_results_dir = "artifacts/allure-results"
    allure_report_dir = "artifacts/allure-report"

    # Generate Allure report
    if os.path.exists(allure_results_dir):
        try:
            subprocess.run(
                ["C:/Users/NikhilD/AppData/Roaming/npm/allure", "generate", allure_results_dir, "-o", allure_report_dir, "--clean"],
                check=True
            )
            print(f"Allure report generated at: {allure_report_dir}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to generate Allure report: {e}")
