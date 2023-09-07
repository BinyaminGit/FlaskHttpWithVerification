#Flask with verification (PyTest)
This is a Python verification tool for a simulated 
e-commerce RESTful API. This tool will:

1. Test basic **CRUD** (Create, Read, Update, Delete) operations for an "item" in an e-commerce catalog.
2. Perform **load testing** on these operations.
3. Provide a **test summary** with performance metrics.
The project will consist of multiple Python files and will use Flask for the API and Pytest for testing.

##Prerequisites
1. Install Python
2. Install Flask and Pytest via pip:
```
pip install Flask pytest
```

##Project Structure
1. app.py: Contains the Flask API code.
2. verification_tool.py: Houses the verification tool code.
3. load_tests.py: Houses the performance/load tests.
4. summary.py: Generates a test summary with performance metrics.

##Instructions
Run app.py to start the Flask server.
Run summary.py to run both functionality and performance tests.
Here, summary.py acts as the driver script that runs all functionality and performance tests, providing a comprehensive summary at the end. You can further extend it to collect and analyze performance metrics over time.