from types import Optional

import subprocess

import pytest

from brownie.network import history
from brownie.network.web3 import web3
import subprocess

class TenderlyManager:

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(
        item: pytest.Item, call: pytest.CallInfo[None]
    ) -> Optional[pytest.TestReport]:
        #TODO: Use tenderly CLI to send transactions to tenderly
        for tx in history:
            pass

