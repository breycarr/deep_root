from light import Light

light = Light()


def test_red(capsys):
    light.red()
    captured = capsys.readouterr()
    assert captured.out == "Soil too dry\n"


def test_blue(capsys):
    light.blue()
    captured = capsys.readouterr()
    assert captured.out == "Soil too wet\n"


def test_green(capsys):
    light.green()
    captured = capsys.readouterr()
    assert captured.out == "Soil just right\n"
