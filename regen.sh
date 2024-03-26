#!/bin/bash

npx @openapitools/openapi-generator-cli generate -i openapi.yaml \
 --generator-name python \
 --output . \
 --package-name fleet_http_client_python \
 --additional-properties=generateSourceCodeOnly=true,apiTests=false,modelTests=false