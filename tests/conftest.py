import os
import pytest


@pytest.fixture(autouse=True)
def prepare_text_file(tmp_path):
    target_file = os.path.join(tmp_path, 'test.txt')
    with open(target_file, 'w') as file:
        lines = ['artem\n',
                 'maksym\n',
                 'ivan\n',
                 'igor\n',
                 'vova\n',
                 'nastya\n',
                 'oleg'
                 ]
        file.writelines(lines)
    return target_file