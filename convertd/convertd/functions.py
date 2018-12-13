from tablib import Dataset


def load_data(filename):
    with open(filename) as f:
        raw = f.read()
        data = Dataset().load(raw)
        return data


def get_formatter(data_format):
    return str if data_format == "csv" else lambda x: json.dumps(x.dict, indent=4)
