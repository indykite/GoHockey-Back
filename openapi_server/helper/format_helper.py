import json
import logging

from google.protobuf.json_format import MessageToJson


def decode_response(resp):
    """
    Reformat the SDK json response from Indykite for better usage.
    Args:
      resp: The raw response via Indykite SDK

    Returns: A json dictionary or the original response if something went wrong

    """
    try:
        js = MessageToJson(resp, including_default_value_fields=True)
        js_dict = json.loads(js)
        prettify(js_dict)
        return js_dict
    except Exception as e:
        logging.info("Something went wrong with the response decode")
        return resp


def prettify(js):
    for k, v in js.items():
        if isinstance(v, type(dict())):
            prettify(v)
        elif isinstance(v, type(list())):
            for val in v:
                if isinstance(val, type(str())):
                    js[k] = format_convert(k, v)
                    pass
                elif isinstance(val, type(list())) or isinstance(val, type(float())) or isinstance(val, type(bool())):
                    pass
                else:
                    prettify(val)
        else:
            if isinstance(v, str):
                js[k] = format_convert(k, v)


def format_convert(k, v):
    try:
        if "id" in k:
            i = int(v)
            return i
    except ValueError:
        pass
    return str(v)
