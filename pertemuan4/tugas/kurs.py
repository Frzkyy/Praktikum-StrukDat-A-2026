def kurs():
    return {
        "EUR": {
            "USD": 1.08,
            "SGD": 1.45,
            "JPY": 160,
            "IDR": 19995
        },
        "USD": {
            "EUR": 1/1.08,
            "SGD": 1.34,
            "JPY": 148,
            "IDR": 16875
        },
        "SGD": {
            "EUR": 1/1.45,
            "USD": 1/1.34,
            "JPY": 108,
            "IDR": 13360
        },
        "JPY": {
            "EUR": 1/160,
            "USD": 1/148,
            "SGD": 1/108,
            "IDR": 109
        },
        "IDR": {
            "EUR": 1/19995,
            "USD": 1/16875,
            "SGD": 1/13360,
            "JPY": 1/109
        }
    }

def kurs_table():
    return {"Kode":["USD", "EUR", "SGD", "JPY"], "Kurs":[16.875, 19.995, 13.360, 109]} 