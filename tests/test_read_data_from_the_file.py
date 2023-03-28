import pytest
from main import read_data_from_the_file

def test_read_data_from_the_file(prepare_text_file):
    assert read_data_from_the_file(prepare_text_file) == ['artem', 'maksym', 'ivan', 'igor', 'vova', 'nastya', 'oleg']
