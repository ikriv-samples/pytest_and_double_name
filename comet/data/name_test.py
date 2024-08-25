import sys

print(f"test_name() module name: {__name__}")
for item in sys.path:
    print("\t" + item)


from comet.data.name import COMET_NAME


def test_name():
    assert COMET_NAME == "Comet"
