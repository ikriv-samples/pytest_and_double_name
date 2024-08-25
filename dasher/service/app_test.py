import sys

print(f"test_name() module name: {__name__}")
for item in sys.path:
    print("\t" + item)

from dasher.service.app import run


def test_run():
    assert run() == 0
