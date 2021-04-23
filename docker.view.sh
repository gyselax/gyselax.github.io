#!/bin/bash

cd "$(dirname "$0")"

function finish {
  [ -d resources ] && rm -r resources
}
trap finish EXIT QUIT ABRT KILL SEGV TERM STOP
finish

docker run -p 1313:1313 "-u$(id -u):$(id -g)" --rm -it -v "$(pwd):/src" klakegg/hugo:0.81.0-ext-alpine server --disableFastRender --i18n-warnings -p 1313
