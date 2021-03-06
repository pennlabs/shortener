import os
import sys

from setuptools import find_packages, setup
from setuptools.command.install import install


VERSION = "0.2.1"
DESCRIPTION = open("README.md", encoding="utf-8").read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""

    description = "verify that the git tag matches our version"

    def run(self):
        tag = os.getenv("CIRCLE_TAG")

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(tag, VERSION)
            sys.exit(info)


setup(
    name="shortener",
    version=VERSION,
    packages=find_packages(exclude=["tests"]),
    url="https://github.com/pennlabs/shortener",
    project_urls={"Changelog": ("https://github.com/pennlabs/shortener/blob/master/CHANGELOG.md")},
    license="MIT",
    author="Penn Labs",
    author_email="admin@pennlabs.org",
    description="URL shortener in django",
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    install_requires=["django>=2.0.0"],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.5",
    cmdclass={"verify": VerifyVersionCommand},
)
