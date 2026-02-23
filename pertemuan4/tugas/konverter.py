from kurs import kurs

def convert(nilai,cr1,cr2):
    kursa = kurs()
    return nilai * (kursa[cr1][cr2])
