def get_all_reference_id_from_get_digital_twin_response(response):
    reference_ids = []
    for i, item in enumerate(response['digitalTwin'].properties):
        if item.property == "nnin":
            reference_ids.append(item.value)
    return reference_ids
