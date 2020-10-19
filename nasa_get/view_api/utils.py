def get_test_api_key():
    with open(".env", "r+") as f:
        result = f.read()
    return result
