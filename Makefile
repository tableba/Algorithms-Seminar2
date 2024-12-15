# Variables
PYTHON = python3
SRC_DIR = .
MAIN = $(SRC_DIR)/main.py
# TESTS = $(SRC_DIR)/tests/test_tasks.py

# Default target
.PHONY: run
run:
	$(PYTHON) $(MAIN)

# Run tests using unittest
.PHONY: test
test:
	$(PYTHON) -m unittest discover -s $(SRC_DIR)/tests -p "test_*.py"

# Clean up Python cache files
.PHONY: clean
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
