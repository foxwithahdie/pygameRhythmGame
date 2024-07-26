from setuptools import setup, find_packages

setup(
    name="pygameRhythmGame",
    version="3.0",
    description="Rhythm Game made in Pygame",
    author="Ramzey Burdette",
    package_dir={"pygameRhythmGame": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "pygame==2.5.2"
    ],
    extras_require={
        'dev': [
            'mypy',
            'pygame-hotreload==0.0.32',
            'black'
        ]
    }
)
