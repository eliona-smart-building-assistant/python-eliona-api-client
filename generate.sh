docker run --rm \
     -v "${PWD}:/local" \
    openapitools/openapi-generator-cli:v6.0.1 \
    generate \
    -g python \
    --git-user-id eliona-smart-building-assistant \
    --git-repo-id python-eliona-api-client \
    -i https://raw.githubusercontent.com/eliona-smart-building-assistant/eliona-api/main/openapi.yaml \
    -o /local \
    --additional-properties="packageName=eliona.api_client,projectName=Python Eliona API client"
