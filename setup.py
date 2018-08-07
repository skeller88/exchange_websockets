import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="exchange_websockets",
    # increment version according to https://semver.org/
    version="0.0.1",
    author="skeller88",
    author_email="skeller88@gmail.com",
    description="Exchange websocket clients",
    install_requires=[
        'websocket-client==0.40.0',
    ],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skeller88/exchange_websockets",
    packages=setuptools.find_packages(),
    python_requires='>=3',
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)