from setuptools import setup, find_packages

setup(
    name="arecanut_quality_classification",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "pandas",
        "numpy",
        "matplotlib",
        "Pillow",
        "streamlit",
        "setuptools"
    ],
)