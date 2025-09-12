#!/bin/bash

# Batch Test Case Enhancement Script
# Usage: ./enhance_batch_problems.sh [max_problems]

set -e

MAX_PROBLEMS="${1:-10}"
THRESHOLD="${2:-10}"

echo "🚀 Starting batch test case enhancement"
echo "📊 Finding problems with ≤$THRESHOLD test cases (max: $MAX_PROBLEMS)"

# Get list of problems needing enhancement
PROBLEMS=$(poetry run python .templates/check_test_cases.py --threshold="$THRESHOLD" --max="$MAX_PROBLEMS" | grep "\.json:" | cut -d':' -f1 | sed 's/\.json$//')

if [ -z "$PROBLEMS" ]; then
    echo "✅ No problems found needing test case enhancement"
    exit 0
fi

echo "📋 Problems to enhance:"
echo "$PROBLEMS" | sed 's/^/  - /'

# Create backup directory
mkdir -p .cache/leetcode

# Process each problem
SUCCESS_COUNT=0
TOTAL_COUNT=0

for PROBLEM in $PROBLEMS; do
    TOTAL_COUNT=$((TOTAL_COUNT + 1))
    echo ""
    echo "🔄 Processing problem $TOTAL_COUNT: $PROBLEM"

    # Backup original
    if [ -d "leetcode/$PROBLEM" ]; then
        cp -r "leetcode/$PROBLEM" ".cache/leetcode/"
        echo "  📦 Backed up original"
    else
        echo "  ❌ Problem directory not found: leetcode/$PROBLEM"
        continue
    fi

    # Regenerate from JSON
    if make p-gen PROBLEM="$PROBLEM" FORCE=1 > /dev/null 2>&1; then
        echo "  🔄 Regenerated from JSON"
    else
        echo "  ❌ Failed to regenerate from JSON"
        continue
    fi

    # Preserve enhanced test and restore structure
    cp "leetcode/$PROBLEM/test_solution.py" ".temp_test_$PROBLEM.py"
    rm -rf "leetcode/$PROBLEM"
    cp -r ".cache/leetcode/$PROBLEM" "leetcode/"
    cp ".temp_test_$PROBLEM.py" "leetcode/$PROBLEM/test_solution.py"
    rm ".temp_test_$PROBLEM.py"

    SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
    echo "  ✅ Enhanced successfully"
done

# Cleanup
rm -rf .cache/leetcode

echo ""
echo "🎉 Batch enhancement completed!"
echo "📊 Results: $SUCCESS_COUNT/$TOTAL_COUNT problems enhanced successfully"

# Verify results
echo ""
echo "📋 Final verification:"
poetry run python .templates/check_test_cases.py --threshold="$THRESHOLD" --max=5
