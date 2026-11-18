#!/bin/bash
# Render the Quarto site and deploy it to magic-flea.com/math
set -e
cd "$(dirname "$0")"

pdm run quarto render

# Top-level .html files on the server that the site doesn't produce are redirects to
# magic-flea.com/reports for pages that used to live here, so they're protected from --delete
rsync -a --delete --filter='P /*.html' _site/ /var/www/html/math/

echo "site deployed to /var/www/html/math"
