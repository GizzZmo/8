#!/bin/bash
# Comprehensive test script for OSI simulation

# Enable strict error handling
set -e  # Exit immediately if a command exits with a non-zero status
set -u  # Treat unset variables as an error
set -o pipefail  # Return value of a pipeline is the status of the last command to exit with a non-zero status

# Function to run a test and capture output
run_test() {
    local test_name="$1"
    local test_cmd="$2"
    local grep_pattern="$3"
    
    echo "$test_name"
    echo "--------------------------------"
    echo "Running: $test_cmd"
    
    # Run command and capture output (disable error handling temporarily)
    set +e
    local output
    output=$(eval "$test_cmd" 2>&1)
    local exit_code=$?
    set -e
    
    # Check if test passed
    if [ $exit_code -eq 0 ] && echo "$output" | grep -E "$grep_pattern" > /dev/null; then
        echo "$output" | grep -E "$grep_pattern"
        echo "✓ $test_name PASSED"
        echo ""
        return 0
    else
        echo "✗ $test_name FAILED" >&2
        echo "Command failed with exit code: $exit_code" >&2
        echo "Full output:" >&2
        echo "$output" >&2
        echo "" >&2
        return 1
    fi
}

echo "======================================"
echo "OSI Blockchain Simulation Test Suite"
echo "======================================"
echo ""

cd osi_blockchain_simulation

# Run all tests
run_test "Test 1: Basic Text Transmission" \
    "python main_simulation.py --data 'Test Message'" \
    "(Original Data|Final Data Received|COMPLETE)"

run_test "Test 2: Encrypted Transmission" \
    "python main_simulation.py --data 'Encrypted' --encrypt" \
    "(Encrypted Payload|Decrypting|Original Data|Final Data)"

run_test "Test 3: Signed Transmission" \
    "python main_simulation.py --data 'Signed' --sign" \
    "(Signed Payload|Signature verified|Final Data)"

run_test "Test 4: Blockchain Transaction" \
    "python main_simulation.py --blockchain" \
    "(sender|receiver|amount|Final Data)"

run_test "Test 5: Combined (Encrypt + Sign)" \
    "python main_simulation.py --data 'Secret' --encrypt --sign" \
    "(Encrypted|Signed|Decrypting|verified|Final)"

echo "======================================"
echo "All Tests Complete!"
echo "======================================"
