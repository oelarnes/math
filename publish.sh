#!/bin/bash
# Render the Quarto site and deploy it to magic-flea.com/math
set -e
cd "$(dirname "$0")"

pdm run quarto render

SITE_DIR=/var/www/html/math
rm -rf "${SITE_DIR:?}"/*
cp -r _site/* "$SITE_DIR"
# Standalone pages keep their original top-level URLs
cp ad_hoc/*.html "$SITE_DIR"

echo "site deployed to $SITE_DIR"
