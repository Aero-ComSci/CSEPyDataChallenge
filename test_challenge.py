import challengeCode

def test_string():
    assert type(challengeCode.challenge("hello")) == str

def test_int():
    assert type(challengeCode.challenge(1)) == int

def test_float():
    assert type(challengeCode.challenge(1.0)) == float

def test_bool():
    assert type(challengeCode.challenge(True)) == bool
