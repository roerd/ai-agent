from functions.get_file_content import get_file_content


def main():
    result = get_file_content("calculator", "lorem.txt")
    print(result[:10000])
    print(result[10000:])


if __name__ == "__main__":
    main()
