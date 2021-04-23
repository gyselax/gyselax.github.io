#!/bin/bash

cd "$(dirname "$0")"

function finish {
  [ -d resources ] && rm -r resources
}
trap finish EXIT QUIT ABRT KILL SEGV TERM STOP
finish

hugo server --disableFastRender --i18n-warnings -p 1316
