from pytest import fixture
@fixture
def ultimate_answer():
    return 42

@fixture
def new_ultimate_answer(ultimate_answer):
    return ultimate_answer + 1

def test_ultimate_answer(ultimate_answer):
    assert ultimate_answer == 42

def test_new_ultimate_answer(new_ultimate_answer):
    assert new_ultimate_answer == 43

def test_both_answers(ultimate_answer, new_ultimate_answer):
    assert ultimate_answer == 42
    assert new_ultimate_answer == 43