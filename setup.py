from setuptools import setup, find_packages

version = __import__('jira2leankit', fromlist=['version', ]).version

setup(
    name="jira2leankit",
    version=version,
    author="Chris Heisel",
    author_email="chris@heisel.org",
    description=("One-way data sync from JIRA to Lean Kit Kanban"),
    long_description=open("README.md").read(),
    url="https://github.com/cmheisel/jira2leankit",
    zip_safe=False,
    include_package_data=True,
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst', '.html'],
    },
    packages=find_packages(),
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ]
)
