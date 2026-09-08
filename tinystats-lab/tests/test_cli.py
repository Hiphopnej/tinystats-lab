from click.testing import CliRunner
from tinystats.cli import cli

def test_cli_mean_and_median():
    r = CliRunner().invoke(cli, ["mean", "1", "2", "3"])
    assert r.exit_code == 0
    assert r.output.strip() == "2.0"

    r2 = CliRunner().invoke(cli, ["median", "1", "3"])
    assert r2.exit_code == 0
    assert r2.output.strip() == "2.0"

    r3 = CliRunner().invoke(cli, ["mean"])
    assert r3.exit_code == 2

    r4 = CliRunner().invoke(cli, ["median"])
    assert r4.exit_code == 2