export BASE_URL="/math"

PRE_BUILD_PIDS=$(ss -tlnp | grep ':30[0-9][0-9]' | grep -v ':3000' | grep -oP 'pid=\K[0-9]+' | sort || true)
jupyter-book build --html --execute
POST_BUILD_PIDS=$(ss -tlnp | grep ':30[0-9][0-9]' | grep -v ':3000' | grep -oP 'pid=\K[0-9]+' | sort || true)
NEW_PIDS=$(comm -13 <(echo "$PRE_BUILD_PIDS") <(echo "$POST_BUILD_PIDS"))
if [ -n "$NEW_PIDS" ]; then
    kill $NEW_PIDS 2>/dev/null || true
fi

SITE_DIR=/var/www/html/math
rm -rf $SITE_DIR/*
cp -r _build/html/* $SITE_DIR

echo "site deployed to $SITE_DIR"
