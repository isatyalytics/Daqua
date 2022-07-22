import os
from setuptools import setup, find_packages

# Read the contents of README file
source_root = os.path.abspath(".")
with open(os.path.join(source_root, "README.md")) as f:
    long_description = f.read()

version = "0.0.1.1"

print("-------------------------")
print(find_packages("daqua"))
print("-------------------")

setup(
    version=version,
    name="daqua",
    author="",
    author_email="",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url="",
    license="MIT",
    description="",
    python_requires=">=3.6",
    install_requires=["numpy", "pandas"],
    extras_require={
        "notebook": []
    },
    package_data={
        "pandas_profiling": [],
    },
    include_package_data=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering",
        "Framework :: IPython",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "daqua = daqua.api.api:Main"
        ]
    },
    options={"bdist_wheel": {"universal": True}},
)
