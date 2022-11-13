import os
from tackle import tackle


def test_eth_get_block_height(chdir, hooks_dir):
    chdir('version-fixtures')
    o = tackle('bump_version.yaml', hook_dirs=[hooks_dir])

    assert o['bump_version_minor'] == 'v0.2.0'
    assert o['bump_version_major'] == 'v1.0.0'
    assert o['bump_version_patch'] == 'v0.1.1'

