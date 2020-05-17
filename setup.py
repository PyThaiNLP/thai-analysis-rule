# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
requirements = [
    "pythainlp",
    "nltk>=3.3",
]

with open("README.md", "r", encoding="utf-8-sig") as f:
    readme = f.read()

setup(
    name="ThaiAnalysisRule",
    version="0.1dev0",
    description="Thai Analysis Rule Tool",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Wannaphong Phatthiyaphaibun",
    author_email="wannaphong@kkumail.com",
    url="https://github.com/PyThaiNLP/thai-analysis-rule",
    packages=find_packages(),
    test_suite="tests",
    python_requires=">=3.6",
    package_data={
        "thaianalysisrule.corpus": [
            "ADV.txt",
            "CLAS.txt",
            "CONJ.txt",
            "DET.txt",
            "LAUX.txt",
            "N.txt",
            "NUM.txt",
            "PREP.txt",
            "RAUX.txt",
            "VATT.txt",
            "VERB.txt",
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords=[
        "pythainlp",
        "NLP",
        "natural language processing",
        "text analytics",
        "text processing",
        "localization",
        "computational linguistics",
        "ThaiNLP",
        "Thai NLP",
        "Thai language",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Thai",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing :: Linguistic",
    ],
    project_urls={
        "Source": "https://github.com/PyThaiNLP/thai-analysis-rule",
        "Bug Reports": "https://github.com/PyThaiNLP/thai-analysis-rule/issues",
    },
)