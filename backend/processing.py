def format_data(data):
    data["Gender"] = data["Gender"].replace({"Male": 0, "Female": 1})
    return data