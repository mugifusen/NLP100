import sys

def split_file_by_lines(file_path, n):#n = 分割数
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        total_lines = len(lines)

        if n <= 0 or n > total_lines:
            print("Invalid value for N. N should be a positive integer less than or equal to the total number of lines.")
            sys.exit(1)

        chunk_size = total_lines // n
        remainder = total_lines % n

        start_idx = 0
        for i in range(n):
            end_idx = start_idx + chunk_size + (1 if i < remainder else 0)
            output_lines = lines[start_idx:end_idx]

            output_file_path = f'output_chunk_{i+1}.txt'
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.writelines(output_lines)

            start_idx = end_idx

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <N>")
        sys.exit(1)

    file_path = 'popular-names.txt'
    n = int(sys.argv[1])

    split_file_by_lines(file_path, n)
