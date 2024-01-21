from pathlib import Path


class WrongInput(Exception):
    pass


def check_extension(file_path, extension):
    file = Path(file_path)
    return True if file.suffix.lower() == extension.lower() else False


def calc(pwd):
    try:
        extension = check_extension(pwd, '.txt')
        if extension:
            with open(pwd, 'r', encoding='utf-8') as file:
                data = file.read()
            data = data.split()
            count = len(data)
            return count
        raise WrongInput('Bad path input')
    except FileNotFoundError:
        raise WrongInput('Bad path input')


def interface():
    pwd = input()
    print(calc(pwd))


if __name__ == '__main__':
    interface()
