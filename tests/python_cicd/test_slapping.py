# Importing this way is possible because we created installable package with setuptools.
import pytest

from python_cicd.slap_that_like_button import slap_many, LikeState


def test_empty_slap():
    assert slap_many(LikeState.empty, "") is LikeState.empty


def test_single_slap():
    assert slap_many(LikeState.empty, "l") is LikeState.liked
    assert slap_many(LikeState.empty, "d") is LikeState.disliked


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("l", LikeState.liked),
        ("d", LikeState.disliked),
        ("ld", LikeState.disliked),
        ("dl", LikeState.liked),
        ("ldd", LikeState.empty),
        ("lldd", LikeState.empty),
        ("ddl", LikeState.liked),
    ],
)
def test_many_slaps(test_input, expected):
    """
    Parametrized version of test case. First argument is the input, second is the expected output
    the same parameters should be passed to the test function.
    """

    assert slap_many(LikeState.empty, test_input) is expected


@pytest.mark.skip(reason="Not implemented yet")
def test_regex_slaps():
    assert slap_many(LikeState.empty, "[ld]*ddl") is LikeState.liked


def test_divide_by_zero_no_raises():
    """
    Error handling test case. We expect ZeroDivisionError to be raised.
    """
    with pytest.raises(ZeroDivisionError):
        return 1 / 0


def test_many_slaps_bad_practice():
    assert slap_many(LikeState.empty, "ll") is LikeState.empty
    assert slap_many(LikeState.empty, "dd") is LikeState.empty
    assert slap_many(LikeState.empty, "ld") is LikeState.disliked
    assert slap_many(LikeState.empty, "dl") is LikeState.liked
    assert slap_many(LikeState.empty, "ldd") is LikeState.empty
    assert slap_many(LikeState.empty, "lldd") is LikeState.empty
    assert slap_many(LikeState.empty, "ddl") is LikeState.liked


def test_print(capture_stdout):
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"
