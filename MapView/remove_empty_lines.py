input_file = 'data.csv'
output_file = 'data_clean.csv'

with open(input_file, 'r', encoding='utf-8') as fin, open(output_file, 'w', encoding='utf-8') as fout:
    for line in fin:
        if line.strip():
            fout.write(line)