#!/bin/bash

# Enhanced Test Case Generation Script for Single Problem
# Usage: ./enhance_single_problem.sh <problem_name>

set -e

PROBLEM_NAME="$1"

if [ -z "$PROBLEM_NAME" ]; then
    echo "Usage: $0 <problem_name>"
    exit 1
fi

echo "🚀 Enhancing test cases for: $PROBLEM_NAME"

# Step 1: Backup original problem
echo "📦 Backing up original problem..."
mkdir -p .cache/leetcode
if [ -d "leetcode/$PROBLEM_NAME" ]; then
    cp -r "leetcode/$PROBLEM_NAME" ".cache/leetcode/"
    echo "✅ Backup created"
else
    echo "❌ Problem directory not found: leetcode/$PROBLEM_NAME"
    exit 1
fi

# Step 2: Regenerate from JSON template
echo "🔄 Regenerating from enhanced JSON template..."
make p-gen PROBLEM="$PROBLEM_NAME" FORCE=1

# Step 3: Lint check
echo "🔍 Running lint check..."
if make p-lint PROBLEM="$PROBLEM_NAME"; then
    echo "✅ Lint check passed"
else
    echo "❌ Lint check failed - please fix JSON template"
    exit 1
fi

# Step 4: Preserve enhanced test file and restore original structure
echo "🔄 Preserving enhanced tests and restoring original structure..."
cp "leetcode/$PROBLEM_NAME/test_solution.py" ".temp_enhanced_test.py"
rm -rf "leetcode/$PROBLEM_NAME"
cp -r ".cache/leetcode/$PROBLEM_NAME" "leetcode/"
cp ".temp_enhanced_test.py" "leetcode/$PROBLEM_NAME/test_solution.py"
rm ".temp_enhanced_test.py"

# Step 5: Verify final state
echo "✅ Enhancement complete for: $PROBLEM_NAME"
echo "📊 Test case count verification:"
python3 -c "
import re
with open('leetcode/$PROBLEM_NAME/test_solution.py', 'r') as f:
    content = f.read()
    matches = re.findall(r'@pytest\.mark\.parametrize.*?\[(.*?)\]', content, re.DOTALL)
    if matches:
        test_cases = matches[0].count('(')
        print(f'Total test cases: {test_cases}')
    else:
        print('Could not count test cases')
"

echo "🎉 Test case enhancement completed successfully!"
