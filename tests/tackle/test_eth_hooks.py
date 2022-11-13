import os
from tackle import tackle


def test_eth_get_block_height(chdir, hooks_dir):
    chdir('eth-fixtures')
    o = tackle('eth_get_block.yaml', hook_dirs=[hooks_dir])

    assert o['eth']['number'] == 100


def test_eth_create_account(chdir, hooks_dir):
    chdir('eth-fixtures')
    o = tackle('eth_create_account.yaml', hook_dirs=[hooks_dir])

    assert o['account']['address']
