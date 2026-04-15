import os
import random

CLASSES = {'healthy': 0, 'cancer': 1}
SAMPLES_PER_CLASS = 5
READS_PER_FILE = 5000
READ_LENGTH = 100
DATA_DIR = 'data'

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def generate_sequence(is_cancer):
    bases = ['A', 'C', 'G', 'T']
    weights = [0.23, 0.27, 0.27, 0.23] if is_cancer else [0.25, 0.25, 0.25, 0.25]
    return ''.join(random.choices(bases, weights=weights, k=READ_LENGTH))

def generate_fastq():
    for class_name, label in CLASSES.items():
        for i in range(1, SAMPLES_PER_CLASS + 1):
            filename = f"{class_name}_{i:02d}.fastq"
            filepath = os.path.join(DATA_DIR, filename)
            
            with open(filepath, 'w') as f:
                for r in range(READS_PER_FILE):
                    seq_id = f"@SEQ_ID_{class_name}_{i}_{r}"
                    sequence = generate_sequence(class_name == 'cancer')
                    plus = "+"
                    quality = "".join([chr(random.randint(60, 73) if class_name == 'cancer' else random.randint(66, 73)) 
                    for _ in range(READ_LENGTH)])
                    f.write(f"{seq_id}\n{sequence}\n{plus}\n{quality}\n")
           

generate_fastq()
