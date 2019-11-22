from setuptools import setup, find_packages
import versioneer

########## dependencies ##########

install_requires = []

examples = [
    'numpy',
    'holoviews',
    'matplotlib',
    'bokeh',
]

tests = [
    'flake8',
    'nbsmoke >=0.2.6',
    'pytest >=2.8.5',
]

extras_require = {
    'tests': tests,
    'examples': examples,
    'doc': examples + [
        'nbsite >=0.6.1',
        'tornado<6',
        'selenium',
    ],
    'tests_extra': tests + [
        'pytest-mpl'  # only available on pip and conda-forge
    ],
    'build': [
        'setuptools',
        'wheel',
    ]
}

extras_require['all'] = sorted(set(sum(extras_require.values(), [])))

setup(
    name='contrib_colormaps',
    description='Contributed colormaps',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='CC-BY License',
    classifiers=[
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 5 - Production/Stable",
    ],
    author="PyViz Developers",
    author_email="jsignell@gmail.com",
    maintainer="Julia Signell",
    maintainer_email="jsignell@gmail.com",
    url="https://contrib_colormaps.pyviz.org",
    project_urls = {
        "Bug Tracker": "http://github.com/pyviz/contrib_colormaps/issues",
        "Documentation": "https://contrib_colormaps.pyviz.org",
        "Source Code": "http://github.com/pyviz/contrib_colormaps",
    },
    include_package_data=True,
    packages=find_packages(),
    python_requires=">=2.7",
    install_requires=install_requires,
    extras_require=extras_require,
)
