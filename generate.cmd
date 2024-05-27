docker run --rm ^
    -v "%cd%":/local ^
    openapitools/openapi-generator-cli:v6.0.1 ^
    generate ^
    -g python ^
    --git-user-id eliona-smart-building-assistant ^
    --git-repo-id python-eliona-api-client ^
    -i https://raw.githubusercontent.com/eliona-smart-building-assistant/eliona-api/main/openapi.yaml ^
    -o /local ^
    --additional-properties="packageName=eliona.api_client,packageVersion=2.6.11,projectName=Python Eliona API client"

:: There is an ivalid import that we cannot avoid in this version of Openapi generator. Let's just remove it.
SET "FILE_PATH=.\eliona\api_client\api\assets_api.py"
SET "INVALID_IMPORT=from eliona.api_client.model.str_none_type import StrNoneType"

IF EXIST "%FILE_PATH%" (
  powershell -Command "(Get-Content -path %FILE_PATH% -Raw) -replace '%INVALID_IMPORT%', '' | Set-Content -Path %FILE_PATH%"
  ECHO Invalid import removed from %FILE_PATH%
) ELSE (
  ECHO File %FILE_PATH% does not exist.
)
