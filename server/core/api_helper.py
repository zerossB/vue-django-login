def set_error(error_dict: dict, key: str, value: any):
    error_dict.setdefault(key, []).append(value)
