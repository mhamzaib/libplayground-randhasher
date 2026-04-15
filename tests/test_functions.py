import pytest
from randhasher.functions import HashTypes
import pandas as pd

def test_sha_generation():
    ht = HashTypes()
    df = ht.generateSha("hello")
    assert isinstance(df, pd.DataFrame)
    assert 'sha256' in df['Algo'].values

def test_no_hex_option():
    ht = HashTypes()
    df = ht.generateSha("hello", noHex=True)
    assert 'HexDigests' not in df.columns

def test_invalid_type():
    ht = HashTypes()
    result = ht.generator('invalid_hash_name', 'test')
    assert result is None