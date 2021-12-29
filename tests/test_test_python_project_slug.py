from test_python_project_slug import make_greeting


def test_make_greeting():
    assert (
        make_greeting("Micael Jarniac")
        == "Hello, Micael Jarniac. Welcome to your new project!"
    )
