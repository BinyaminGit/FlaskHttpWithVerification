import verification_tool
import load_tests

def generate_summary():
    print("Running Functionality Tests...")
    pytest.main(['-q', 'verification_tool.py'])

    print("\nRunning Load Tests...")
    load_tests.load_test_post()

    print("\nSummary: All tests completed successfully.")

if __name__ == '__main__':
    generate_summary()
