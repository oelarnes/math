export BASE_URL="/math"
jupyter-book build --html

SITE_DIR=/var/www/html/math
rm -rf $SITE_DIR/*
cp -r _build/html/* $SITE_DIR

echo "site deployed to $SITE_DIR"
