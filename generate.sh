docker run --rm \
     -v "${PWD}:/local" \
    openapitools/openapi-generator-cli:v6.0.1 \
    generate \
    -g python \
    --git-user-id eliona-smart-building-assistant \
    --git-repo-id python-eliona-api-client \
    -i https://raw.githubusercontent.com/eliona-smart-building-assistant/eliona-api/main/openapi.yaml \
    -o /local \
    --additional-properties="packageName=eliona.api_client,packageVersion=2.8.2,projectName=Python Eliona API client"

# There is an ivalid import that we cannot avoid in this version of Openapi generator. Let's just remove it.
FILE_PATH="./eliona/api_client/api/assets_api.py"
INVALID_IMPORT="from eliona.api_client.model.str_none_type import StrNoneType"

if [ -f "$FILE_PATH" ]; then
  grep -v "$INVALID_IMPORT" "$FILE_PATH" > temp_file && mv -f temp_file "$FILE_PATH"
  echo "Invalid import removed from $FILE_PATH"
else
  echo "File $FILE_PATH does not exist."
fi
