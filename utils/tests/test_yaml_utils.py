import io_utils

def test_wirte():
    data = {
        "this": "is a best",
        "test": ["heih", None],
        "dd": {
            "ee": ["dd"]
        },
        "ww": [{"eeqq": "ww", "eew": 2}]
    }

    byte = io_utils.save_data(data=data, type='yaml')
    io_utils.bytes_to_file(byte, 'test.yaml')

test_wirte()