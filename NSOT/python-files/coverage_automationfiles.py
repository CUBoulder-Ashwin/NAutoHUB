import coverage
import unittest
import os
import webbrowser

def run_tests_with_coverage():
    # Initialize coverage for the current directory
    cov = coverage.Coverage(source=["."])
    cov.start()

    # Load tests from all test files in the current directory
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Assuming test files are named `test_<module>.py` and are in the current directory
    for filename in os.listdir("."):
        if filename.endswith(".py"):
            module_name = filename[:-3]  # Remove .py from filename
            tests = loader.loadTestsFromName(module_name)
            suite.addTests(tests)

    # Run tests and check for errors/failures
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Stop coverage and save report
    cov.stop()
    cov.save()

    # Report coverage results to console
    print("\nCoverage Summary:")
    cov.report()

    # Print overall success status
    if result.wasSuccessful():
        print("\nAll tests passed without errors.")
    else:
        print("\nSome tests failed or encountered errors.")

    # Generate HTML report and open it automatically
    cov.html_report(directory="htmlcov")
    print("HTML coverage report generated in 'htmlcov' directory.")

    # Open the HTML report in the default web browser
    html_report_path = os.path.abspath("htmlcov/index.html")
    webbrowser.open(f"file://{html_report_path}")

if __name__ == "__main__":
    run_tests_with_coverage()
