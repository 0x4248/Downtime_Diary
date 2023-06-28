import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Downtime Diary",
    url="https://github.com/lewisevans2007/downtime-diary/",
    author="Lewis",
    packages=["downtime"],
    install_requires=[""],
    version="0.1.0",
    license="GNU",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="A simple and lightweight downtime logger for your linux server",
)
