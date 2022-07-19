# Generate the Python Eliona API client #

The OpenAPI specification can be used to generate the go source code. To do this, you can use one of the [OpenAPI Generators](https://openapi-generator.tech/). The following instruction uses the JAR-based generator.

At first, download the [Generator Jar](https://openapi-generator.tech/docs/installation#jar) file: `https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/6.0.0/openapi-generator-cli-6.0.0.jar` to any directory outside the go-eliona project. Also, Java 8 runtime at a minimum is required.

Then you can generate the go client, with the following command. Note, that you configure the package name for the generated files to `eliona-api`. The `.openapi-generator-ignore` file defines files that should not be generated again.

```bash
java -jar openapi-generator-cli-6.0.0.jar generate \
  -g python \
  -i https://raw.githubusercontent.com/eliona-smart-building-assistant/eliona-api/develop/eliona-api-v2.yaml \
  -o ./ \
  --additional-properties="packageName=io.eliona.api_client,projectName=Python Eliona API client,packageVersion=1.0.0"
```