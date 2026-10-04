export BASE_URL="/math"

PRE_PIDS=$(pgrep -f 'node.*server\.js|jupyter_server' | sort -n || true)
jupyter-book build --html --execute --ci
POST_PIDS=$(pgrep -f 'node.*server\.js|jupyter_server' | sort -n || true)

# Kill any servers that appeared during the build — pre-existing dev servers survive
comm -13 <(echo "$PRE_PIDS") <(echo "$POST_PIDS") | xargs -r kill 2>/dev/null || true

SITE_DIR=/var/www/html/math
rm -rf $SITE_DIR/*
cp -r _build/html/* $SITE_DIR
cp ../notes/*.html $SITE_DIR

echo "site deployed to $SITE_DIR"
