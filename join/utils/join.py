def join(file_1, file_2, col1_idx, col2_idx, join_type):
    with open(file_1) as f1:
        f1.readline()
        while line_1 := f1.readline().strip():
            cells_1 = line_1.split(',')
            with open(file_2) as f2:
                f2.readline()
                while line_2 := f2.readline().strip():
                    cells_2 = line_2.split(',')
                    if cells_1[col1_idx] == cells_2[col2_idx]:
                        print(f'{line_1},{line_2}')
