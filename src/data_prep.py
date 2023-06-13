data = [
    {'input': 'My car is Ford Focus 2014', 'expected': {'Year': '2014', 'Maker': 'Ford', 'Model': 'Focus'}, 'key': 0}, 
    {'input': 'My car is BMW X5 2017', 'expected': {'Year': '2017', 'Maker': 'BMW', 'Model': 'X5'}, 'key': 1}
        ]

import jsonlines

with jsonlines.open('input.jsonl', mode='w') as writer:
    writer.write(data)