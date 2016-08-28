#!/usr/bin/env python

from stegolib.main import *
import pytest


class TestRotClass:
    def test_rot_n(self):
        with pytest.raises(ValueError):
            rotN(-26, '')

    def test_rot_value(self):
        assert rotN(1, 'ABC xyz') == 'BCD yza'
