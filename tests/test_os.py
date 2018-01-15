import pytest
import lib.os as o

def test_uname():
    assert o.uname() == "Linux"

def test_whoami():
    assert o.whoami() == "peter"

