def print_joined(file_1, file_2, col1_idx, col2_idx, num_col1, num_col2, join_type):

    with open(file_1) as f1:
        print(f1.readline().strip(), end=',')
    with open(file_2) as f2:
        print(f2.readline().strip())

    if join_type == 'right':
        file_1, file_2 = file_2, file_1
        col1_idx, col2_idx = col2_idx, col1_idx
        num_col1, num_col2 = num_col2, num_col1

    with open(file_1) as f1:
        f1.readline()
        while line_1 := f1.readline().strip():
            cells_1 = line_1.split(',')
            with open(file_2) as f2:
                f2.readline()
                anything = False
                while line_2 := f2.readline().strip():
                    cells_2 = line_2.split(',')
                    if cells_1[col1_idx] == cells_2[col2_idx]:
                        anything = True
                        if join_type == 'right':
                            print(f'{line_2},{line_1}')
                        else:
                            print(f'{line_1},{line_2}')
                if not anything:
                    if join_type == 'right':
                        print(f"{',' * num_col2}{line_1}")
                    elif join_type == 'left':
                        print(f"{line_1}{',' * num_col2}")
