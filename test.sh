#!/bin/bash

if ! type jq > /dev/null; then
    echo "Install 'jq' in your path from https://stedolan.github.io/jq/"
    exit 1
fi

TOKEN=$(curl -X GET 'http://localhost/api/auth/token?key=user&secret=pass' | jq -r '.token')

if "${TOKEN}" == ""; then
    echo "Error getting a token"
    exit 1
fi

curl -H "token: ${TOKEN}" -X POST "http://localhost/api/data/accounts?name=google&valuation=99999&employees=3000" | jq
curl -H "token: ${TOKEN}" -X POST "http://localhost/api/data/accounts?name=yunatech&valuation=1&employees=1" | jq

curl -H "token: ${TOKEN}" -X GET "http://localhost/api/data/accounts" | jq

echo "*** test complete ***"
