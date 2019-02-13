import pytest

from pprint import pprint as pp
from virtbuilder import api


@pytest.mark.parametrize("fixture_filename", ["valid.yml", "minimum.yml"])
def test_validate(get_fixture, fixture_filename):
    input_file = get_fixture(fixture_filename)
    api.validate(input_file)


def test_build_image_cmd_1(load_fixture):
    data = load_fixture("minimum.yml")
    cmd = api.build_image_cmd(data, singleline=False)
    assert cmd == "\n".join(
        [
            """virt-builder \\""",
            """  ubuntu-18.04 \\""",
            """  --format qcow2 \\""",
            """  --output kmaster.qcow2 \\""",
            """  --hostname kmaster \\""",
            """  --size "12G" """.rstrip(),
        ]
    )


def test_build_image_cmd_2(load_fixture):
    data = load_fixture("valid.yml")
    cmd = api.build_image_cmd(data, singleline=False)
    assert cmd == "\n".join(
        [
            """virt-builder \\""",
            """  ubuntu-18.04 \\""",
            """  --format qcow2 \\""",
            """  --output kmaster.qcow2 \\""",
            """  --hostname kmaster \\""",
            """  --size "12G" \\""",
            """  --arch "x86_64" \\""",
            """  --no-sync \\""",
            """  --memsize "2000" \\""",
            """  --smp "2" \\""",
            """  --update \\""",
            """  --timezone "Europe/Athens" \\""",
            """  --password-crypto "sha512" \\""",
            """  --root-password "file:/home/feanor/Prog/git/virtbuilder/virtbuilder/root_password.txt" \\""",
            """  --firstboot-command "dpkg-reconfigure openssh-server" \\""",
            """  --ssh-inject "root:file:/home/feanor/.ssh/id_rsa.pub" \\""",
            """  --touch "/etc/apt/apt.conf.d/01norecommend" \\""",
            """  --append-line "/etc/apt/apt.conf.d/01norecommend:APT::Install-Recommends "0";" \\""",
            """  --append-line "/etc/apt/apt.conf.d/01norecommend:APT::Install-Suggests "0";" \\""",
            """  --install "net-tools,wget,curl,tree,ncdu,dfc,zsh,silversearcher-ag" """.rstrip(),
        ]
    )