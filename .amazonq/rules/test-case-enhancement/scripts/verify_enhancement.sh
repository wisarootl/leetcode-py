#!/bin/bash

# Verify Test Case Enhancement Results
# Usage: ./verify_enhancement.sh <problem_name>

PROBLEM_NAME="$1"

if [ -z "$PROBLEM_NAME" ]; then
    echo "Usage: $0 <problem_name>"
    exit 1
fi

echo "🔍 Verifying test case enhancement for: $PROBLEM_NAME"

if [ ! -d "leetcode/$PROBLEM_NAME" ]; then
    echo "❌ Problem directory not found: leetcode/$PROBLEM_NAME"
    exit 1
fi

# Count test cases
TEST_FILE="leetcode/$PROBLEM_NAME/test_solution.py"
if [ ! -f "$TEST_FILE" ]; then
    echo "❌ Test file not found: $TEST_FILE"
    exit 1
fi

echo "📊 Test case analysis:"

# Count parametrized test cases
TEST_COUNT=$(python3 -c "
import re
with open('$TEST_FILE', 'r') as f:
    content = f.read()
    matches = re.findall(r'@pytest\.mark\.parametrize.*?\[(.*?)\]', content, re.DOTALL)
    if matches:
        test_cases = matches[0].count('(')
        print(test_cases)
    else:
        print(0)
")

echo "  Total test cases: $TEST_COUNT"

if [ "$TEST_COUNT" -gt 10 ]; then
    echo "  ✅ Exceeds minimum requirement (>10)"
else
    echo "  ❌ Below minimum requirement (≤10)"
fi

# Check if tests can run (syntax check)
echo ""
echo "🔍 Syntax validation:"
if python3 -m py_compile "$TEST_FILE" 2>/dev/null; then
    echo "  ✅ Test file syntax is valid"
else
    echo "  ❌ Test file has syntax errors"
fi

# Try to run the tests (will fail if no implementation, but shows test structure)
echo ""
echo "🧪 Test structure validation:"
if make p-test PROBLEM="$PROBLEM_NAME" 2>/dev/null | grep -q "collected"; then
    COLLECTED=$(make p-test PROBLEM="$PROBLEM_NAME" 2>&1 | grep "collected" | head -1)
    echo "  ✅ Tests are discoverable: $COLLECTED"
else
    echo "  ⚠️  Could not validate test discovery (may be due to missing implementation)"
fi

echo ""
echo "📋 Enhancement summary for $PROBLEM_NAME:"
echo "  - Test cases: $TEST_COUNT"
echo "  - Meets requirement: $([ "$TEST_COUNT" -gt 10 ] && echo "✅ Yes" || echo "❌ No")"
echo "  - Syntax valid: $(python3 -m py_compile "$TEST_FILE" 2>/dev/null && echo "✅ Yes" || echo "❌ No")"
