from jsonschema import validate


inferenceSchema = {
    "type": "object",
    "properties": {
        "ImageString": {"type": "string"}
    },
    "required": ["ImageString"]
}


def check(data, schema):
    try:
        validate(instance=data, schema=schema)
        err = None
    except Exception as e:
        err = e.message
    return data, err
