from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="pylexlite",
    version="1.0",
    rust_extensions=[RustExtension("pylexlite", binding=Binding.PyO3)],
    py_modules=["pylexlite"],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
)
