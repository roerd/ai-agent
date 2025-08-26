from functions.write_file import write_file


def main():
    print('write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum"):\n====================')
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print('====================\n')

    print('write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"):\n====================')
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print('====================\n')

    print('write_file("calculator", "/tmp/temp.txt", "this should not be allowed"):\n====================')
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print('====================')


if __name__ == "__main__":
    main()
