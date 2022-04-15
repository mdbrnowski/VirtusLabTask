# VirtusLabTask

`join` command created for the recruitment task for VirtusLab.

It reads two csv files, joins them using a specified column and then writes the result to the standard output.

## Instalation

```shell
pip install git+https://github.com/mdbrnowski/VirtusLabTask/
```

## Usage

```shell
join file_path_1 file_path_2 column_name [join_type]
```

Supported types of joins: `inner`, `left`, `right`. The `inner` join is default one.

You can also redirect the program output to a file:
```shell
join file_1.csv file_2.csv column_name > file_res.csv
```

## why I did it the way I did
1. Inner join is default in SQL, so I think it's a good idea to make it default here as well.
2. Assume that the resulting file size is of the same magnitude as the input files. Then `join` can easily be done in O(n*logn) (just sort the rows and search them binary). But since we have very limited memory, it seems to me that O(n^2) is the only solution. For this reason, I decided to simply iterate through both files using two nested loops.