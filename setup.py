from setuptools import find_packages, setup

setup(
    name="datareader",
    version="0.0.0",
    license="MIT",
    description="Utility to read input data from text.",
    author="Schalk Visagie",
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=["pandas", "sqlalchemy", "psycopg2"],
)
