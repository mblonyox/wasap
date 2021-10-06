from setuptools import setup, find_packages

setup(
    name="Wasap",
    version="1.0.0",
    url="https://github.com/mblonyox/wasap",
    author="Sukirno",
    author_email="mblonyox@gmail.com",
    description="A service to send message via Whatsapp messenger programmatically.",
    packages=find_packages(),
    install_requires=["selenium", "click"],
    entry_points={
        "console_scripts": [
            "wasap-cli=wasap.cli:main",
            "wasap-service=wasap.service:main",
        ]
    }
)
