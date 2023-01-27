from importlib import metadata

# Current version is defined in pyproject.toml
__version__ = metadata.version(__package__)

del metadata
