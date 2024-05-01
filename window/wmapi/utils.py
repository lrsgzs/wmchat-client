def get_url_params(**kwargs):
    params = ""
    for key, value in kwargs.items():
        params += f"{key}={value}&"
    return params[:-1]
