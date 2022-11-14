from tackle import tackle


def test_main_build(change_base_dir):
    output = tackle('build', chain='eth', network='mainnet')

    assert output['script'] == 'eth/scripts/build.sh'


def test_main_deploy(change_base_dir):
    output = tackle('deploy', chain='eth', network='mainnet', contract='bmc')

    assert output['script'] == 'eth/scripts/deploy.sh'


def test_main_build2(change_base_dir):
    output = tackle(override={'a_input': 'foo'})

    assert output['a_input'] == 'foo'
