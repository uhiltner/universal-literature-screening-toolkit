#!/bin/bash

#
# ULST Test Runner Script (Unix/Linux/macOS)
#
# Runs the comprehensive test suite using the isolated venv at ~/.uls_env.
# This validates all 38 tests covering edge cases, core functionality, and integration scenarios.
#
# Usage:
#   ./scripts/run_tests.sh [OPTIONS]
#
# Options:
#   -v, --verbose     Show detailed test output (-v flag)
#   -c, --coverage    Generate coverage report (requires pytest-cov)
#   -x, --fail-fast   Stop after first failure (-x flag)
#   -s, --specific    Run only specific test file (e.g., "test_validator.py")
#   -h, --help       Show this help message
#
# Examples:
#   ./scripts/run_tests.sh                           # Run all tests
#   ./scripts/run_tests.sh -v                       # Verbose output
#   ./scripts/run_tests.sh -s test_validator.py     # Run specific tests
#   ./scripts/run_tests.sh -x -v                    # Stop on first failure with details
#

set -euo pipefail

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
GRAY='\033[0;90m'
NC='\033[0m' # No Color

# Output functions
info() { echo -e "${CYAN}[INFO]${NC} $1"; }
ok() { echo -e "${GREEN}[ OK ]${NC} $1"; }
error() { echo -e "${RED}[ERR ]${NC} $1"; }
test_msg() { echo -e "${YELLOW}[TEST]${NC} $1"; }

# Default values
VERBOSE=false
COVERAGE=false
FAIL_FAST=false
SPECIFIC=""

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -c|--coverage)
            COVERAGE=true
            shift
            ;;
        -x|--fail-fast)
            FAIL_FAST=true
            shift
            ;;
        -s|--specific)
            SPECIFIC="$2"
            shift 2
            ;;
        -h|--help)
            echo "ULST Test Runner - Run comprehensive test suite"
            echo ""
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  -v, --verbose     Show detailed test output"
            echo "  -c, --coverage    Generate coverage report"
            echo "  -x, --fail-fast   Stop after first failure"
            echo "  -s, --specific    Run specific test file"
            echo "  -h, --help        Show this help message"
            echo ""
            echo "Examples:"
            echo "  $0                              # Run all tests"
            echo "  $0 -v                           # Verbose output"
            echo "  $0 -s test_validator.py -v      # Run specific tests"
            exit 0
            ;;
        *)
            error "Unknown option: $1"
            echo "Use -h or --help for usage information"
            exit 1
            ;;
    esac
done

# Check virtual environment
VENV_PATH="$HOME/.uls_env"
PYTHON_EXE="$VENV_PATH/bin/python"

if [[ ! -f "$PYTHON_EXE" ]]; then
    error "Python venv not found at $VENV_PATH. Please run ./scripts/setup_unix.sh first."
    exit 1
fi

# Find repository root and tests directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
TESTS_DIR="$REPO_ROOT/tests"

if [[ ! -d "$TESTS_DIR" ]]; then
    error "Tests directory not found at $TESTS_DIR"
    exit 1
fi

# Build pytest command
PYTEST_ARGS=("-m" "pytest")

# Add test target
if [[ -n "$SPECIFIC" ]]; then
    TEST_TARGET="$TESTS_DIR/$SPECIFIC"
    if [[ ! -f "$TEST_TARGET" ]]; then
        error "Specific test file not found: $TEST_TARGET"
        exit 1
    fi
    PYTEST_ARGS+=("$TEST_TARGET")
    test_msg "Running specific tests: $SPECIFIC"
else
    PYTEST_ARGS+=("$TESTS_DIR")
    test_msg "Running full test suite (38 tests)"
fi

# Add options
if [[ "$VERBOSE" == true ]]; then
    PYTEST_ARGS+=("-v")
    info "Verbose output enabled"
fi

if [[ "$COVERAGE" == true ]]; then
    PYTEST_ARGS+=("--cov=scripts")
    info "Coverage reporting enabled"
fi

if [[ "$FAIL_FAST" == true ]]; then
    PYTEST_ARGS+=("-x")
    info "Fail-fast mode enabled"
fi

info "Test configuration:"
echo -e "  ${GRAY}Python:    $PYTHON_EXE${NC}"
echo -e "  ${GRAY}Tests:     $TESTS_DIR${NC}"
echo -e "  ${GRAY}Command:   python ${PYTEST_ARGS[*]:2}${NC}"

echo ""
test_msg "Starting test execution..."
echo "=========================================================="

# Run the tests
"$PYTHON_EXE" "${PYTEST_ARGS[@]}"
EXIT_CODE=$?

echo "=========================================================="

if [[ $EXIT_CODE -eq 0 ]]; then
    ok "All tests passed successfully! ✅"
    info "Your toolkit installation is verified and ready for research."
else
    error "Some tests failed (exit code: $EXIT_CODE)"
    info "This may indicate installation issues or code problems."
    info "Check the test output above for specific failure details."
fi

echo ""
info "Test categories covered:"
echo -e "  ${GRAY}🔍 Search Parser:     Quoted phrases, wildcards, regex patterns${NC}"
echo -e "  ${GRAY}✅ Validator:         AND/OR logic, block combinations, edge cases${NC}"
echo -e "  ${GRAY}📄 PDF Extractor:     Capability reporting, corrupt file handling${NC}"
echo -e "  ${GRAY}📊 Report Generator:  HTML generation, file sorting, statistics${NC}"
echo -e "  ${GRAY}🔧 CLI Integration:   End-to-end workflows, error scenarios${NC}"
echo -e "  ${GRAY}🏗️  Toolkit Structure: File existence, configuration validation${NC}"

if [[ $EXIT_CODE -ne 0 ]]; then
    echo ""
    info "Troubleshooting tips:"
    echo -e "  ${GRAY}• Re-run setup: ./scripts/setup_unix.sh${NC}"
    echo -e "  ${GRAY}• Check dependencies: $PYTHON_EXE -m pip list${NC}"
    echo -e "  ${GRAY}• Run specific test: $0 -s test_name.py -v${NC}"
fi

exit $EXIT_CODE