## Generation ##

### Generate Python client for Eliona API ###

To build the Python client files you have to generate it with OpenAPI generator. This client can be used to access the API with Python scripts.

The easiest way to generate the client files is to use one of the predefined generation script which use the OpenAPI Generator Docker image.

```
.\generate.cmd # Windows
./generate.sh # Linux
```

If you want to use other generators take the necessary generator options from one of the scripts. See [OpenAPI Generator documentation](https://openapi-generator.tech/docs/generators/openapi-yaml) for further details.
