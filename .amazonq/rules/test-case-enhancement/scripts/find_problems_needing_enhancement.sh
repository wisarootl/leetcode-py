#!/bin/bash

# Find Problems Needing Test Case Enhancement
# Usage: ./find_problems_needing_enhancement.sh [threshold] [max_results]

THRESHOLD="${1:-10}"
MAX_RESULTS="${2:-20}"

echo "🔍 Finding problems with ≤$THRESHOLD test cases (showing max $MAX_RESULTS results)"
echo ""

# Run the check and format output
OUTPUT=$(poetry run python .templates/check_test_cases.py --threshold="$THRESHOLD" --max="$MAX_RESULTS")

if echo "$OUTPUT" | grep -q "Files with ≤"; then
    echo "$OUTPUT"
    echo ""

    # Extract just the problem names for easy copying
    PROBLEM_NAMES=$(echo "$OUTPUT" | grep "\.json:" | cut -d':' -f1 | sed 's/\.json$//')
    PROBLEM_COUNT=$(echo "$PROBLEM_NAMES" | wc -l | tr -d ' ')

    echo "📋 Problem names for batch processing:"
    echo "$PROBLEM_NAMES" | sed 's/^/  /'
    echo ""
    echo "📊 Total problems found: $PROBLEM_COUNT"

    if [ "$PROBLEM_COUNT" -gt 0 ]; then
        echo ""
        echo "💡 Quick commands:"
        echo "  # Enhance all found problems:"
        echo "  ./.amazonq/rules/test-case-enhancement/scripts/enhance_batch_problems.sh $PROBLEM_COUNT $THRESHOLD"
        echo ""
        echo "  # Enhance single problem:"
        echo "  ./.amazonq/rules/test-case-enhancement/scripts/enhance_single_problem.sh <problem_name>"
    fi
else
    echo "✅ No problems found needing test case enhancement (threshold: $THRESHOLD)"
fi
