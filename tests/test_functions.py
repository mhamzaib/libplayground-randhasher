import pytest
import pandas
from randhasher.functions import HashTypes

@pytest.mark.sha3
def test_sha3():
    instance = HashTypes()
    assert type(instance.generateSha3(string="This works", noHex=False)) is pandas.core.frame.DataFrame
    assert instance.generateSha3(string="", noHex=False) is ValueError

 