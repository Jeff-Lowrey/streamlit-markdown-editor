"""Smoke tests for the package skeleton."""

import streamlit_markdown_editor


def test_package_imports_and_exposes_version() -> None:
    version = streamlit_markdown_editor.__version__
    assert isinstance(version, str)
    assert version
