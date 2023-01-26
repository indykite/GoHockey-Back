def get_all_reference_id_from_get_digital_twin_response(response):
    reference_ids = []
    props = response['digitalTwin']['properties']
    print("All props: %s" % props)
    for p in props:
        if p['definition']['property'] == "nnin":
            print("Found ref ID: %s" % p['objectValue']['stringValue'])
            reference_ids.append(p['objectValue']['stringValue'])
    return reference_ids
