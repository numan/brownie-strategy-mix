import pytest
import os
import subprocess


# set commandline options
def pytest_addoption(parser):
    parser.addoption(
        "--tenderly-fork-simulation",
        action="store_true",
        help="Export all tests to a Tenderly fork"
    )

    parser.addoption(
        "--tenderly-access-key",
        nargs=1,
        default=False,
        help="Load a brownie project at the given path"
    )

def pytest_configure(config):
    if config.getoption("tenderly-fork-simulation"):
        try:
            subprocess.check_output(["tenderly"])
        except:
            raise pytest.UsageError("Tenderly CLI not found. The Tenderly CLI is needed when using --tenderly-fork-simulation: https://github.com/Tenderly/tenderly-cli#installation")
        # Check if we have credentials
        tenderly_access_key = config.getoption("tenderly-access-key", os.environ.get("TENDERLY_ACCESS_KEY"))
        if not tenderly_access_key:
                raise pytest.UsageError("Need to provide Tenderly Access Key using --tenderly-access-key option or TENDERLY_ACCESS_KEY environment variable")

        try:
            subprocess.check_output([
                'tenderly',
                'login',
                '--access-key',
                tenderly_access_key,
                '--authentication-method',
                'access-key',
                '--force'])
        except:
            pytest.UsageError("Could not validate tenderly account")