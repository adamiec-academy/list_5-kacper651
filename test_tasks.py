import pytest
from test_data import LONGEST_WORD_DATA, UNIQUE_DATA, REVERSED_WORDS_DATA, TOWER_OF_HANOI_DATA


def _data_args(data):
    if not data:
        return
    size = len(data[0])
    names = []
    for entry in data:
        name = []
        for arg in range(size - 1):
            name.append(str(entry[arg]))
        names.append(", ".join(name))
    return names


def test_task_1_longest_word():
    from task_1 import longest_word
    word = longest_word()
    assert len(word) == 29
    assert longest_word() in LONGEST_WORD_DATA


@pytest.mark.parametrize("arg, expected_output", UNIQUE_DATA, ids=_data_args(UNIQUE_DATA))
def test_task_2_unique(arg, expected_output):
    from task_2 import unique
    assert unique(arg) == expected_output


def test_task_3_dot_image():
    file = open("task_3.py", "r", encoding="utf-8")
    assert file.readline().strip() != "# Remove this comment to confirm that this task is done"


def test_task_4_reversed_words():
    from task_4 import reversed_words
    assert reversed_words() == REVERSED_WORDS_DATA


@pytest.mark.parametrize("n, source, dest, aux, expected_output", TOWER_OF_HANOI_DATA, ids=_data_args(TOWER_OF_HANOI_DATA))
def test_task_5_tower_of_hanoi(capfd, n, source, dest, aux, expected_output):
    with capfd.disabled():
        from task_5 import tower_of_hanoi
    tower_of_hanoi(n, source, dest, aux)
    actual_output, _ = capfd.readouterr()
    assert actual_output == expected_output
