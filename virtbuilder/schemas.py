import pathlib
from schema import Schema, And, Or, Use, Optional, SchemaError


def OneOf(*unique):
    def one_of(value):
        return value in set(unique)

    return one_of


definition_schema = Schema(
    {
        "build": {
            "os": And(Use(str), len),
            "version": And(str, len),
            Optional("output"): And(str, len),
            "size": And(str, len),
            "format": And(str, len, OneOf("raw", "qcow2")),
            Optional("arch"): And(str, len),
            Optional("no-sync"): And(bool),
            Optional("memsize"): And(int, lambda n: n > 1000),
            Optional("smp", default=4): And(int, lambda n: n > 1),
            # TODO Add support for --attach and --attach-format
            "config": {
                Optional("update"): And(bool),
                Optional("selinux-relabel"): And(bool),
                Optional("hostname"): And(str, len),
                Optional("timezone"): And(str, len),
                Optional("password-crypto", default="sha512"): And(
                    str, len, OneOf("md5", "sha256", "sha512")
                ),
                Optional("root-password"): And(str, len),
                Optional("provision"): [
                    Or(
                        {"append-line": And(str, len)},
                        {"chmod": And(str, len)},
                        {"copy": And(str, len)},
                        {"copy-in": And(str, len)},
                        {"delete": And(str, len)},
                        {"edit": And(str, len)},
                        {"firstboot": And(str, len)},
                        {"firstboot-command": And(str, len)},
                        {"firstboot-install": [And(str, len)]},
                        {"install": [And(str, len)]},
                        {"link": And(str, len)},
                        {"mkdir": And(str, len)},
                        {"move": And(str, len)},
                        {"password": And(str, len)},
                        {"run": And(str, len, Use(pathlib.Path), lambda p: p.exists())},
                        {"run-command": And(str, len)},
                        {"scrub": And(str, len)},
                        {"ssh-inject": And(str, len)},
                        {"touch": And(str, len)},
                        {"touch": And(str, len)},
                        {"truncate-recursive": And(str, len)},
                        {"uninstall": [And(str, len)]},
                        {"upload": And(str, len)},
                        {"write": And(str, len)},
                    )
                ],
            },
        }
    }
)
