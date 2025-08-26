from functions.run_python_file import run_python_file


def main():
    print('run_python_file("calculator", "main.py"):\n====================')
    print(run_python_file("calculator", "main.py"))
    print('====================\n')

    print('run_python_file("calculator", "main.py", ["3 + 5"]):\n====================')
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print('====================\n')

    print('run_python_file("calculator", "tests.py"):\n====================')
    print(run_python_file("calculator", "tests.py"))
    print('====================\n')

    print('run_python_file("calculator", "../main.py"):\n====================')
    print(run_python_file("calculator", "../main.py"))
    print('====================\n')

    print('run_python_file("calculator", "nonexistent.py"):\n====================')
    print(run_python_file("calculator", "nonexistent.py"))
    print('====================')


if __name__ == "__main__":
    main()
