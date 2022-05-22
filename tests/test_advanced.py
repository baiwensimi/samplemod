# -*- coding: utf-8 -*-

from .context import sample

import pytest


def test_thoughts():
    sample.hmm()

@pytest.mark.slow
def test_slow():
    for k in range(10000):
        assert k == k
