from base64 import b64decode
from os import getenv

CBHDSYS = getenv(
    "CBHDSYS",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL2hpZGFnYW5zL0NpbGlrLVVib3Q=").decode("utf-8"),
)
