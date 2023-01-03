from src.simple_flask import *
import pytest

def test_hello_world():
    assert hello_world() == "<p>Hello, World!</p>"