import sys
import os
from setuptools import setup
from setuptools import find_packages

exec(open(os.path.join(os.path.dirname(__file__), "mofapy2", "version.py")).read())

# Read README long description
# from pathlib import Path
# this_directory = Path(__file__).parent
# long_description = (this_directory / "README.md").read_text()


def setup_package():
    install_requires = ["pandas", "scipy", "numpy", "scikit-learn", "argparse", "h5py"]
    metadata = dict(
        name="mofapy2",
        version=__version__,
        description="Multi-Omics Factor Analysis, a statistical framework for the integration of multi-omics data",
        # long_description=long_description,
        # long_description_content_type='text/markdown',
        url="http://github.com/bioFAM/mofapy2",
        author="Ricard Argelaguet",
        author_email="ricard.argelaguet@gmail.com",
        license="LGPL-3.0",
        packages=find_packages(),
        install_requires=install_requires,
    )

    setup(**metadata)


if __name__ == "__main__":
    if sys.version_info < (2, 7):
        sys.exit("Sorry, Python < 2.7 is not supported")

    setup_package()
