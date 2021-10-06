from setuptools import setup, find_packages

setup(
    name="Wasap",
    version="1.0.0",
    author="Sukirno",
    author_email="mblonyox@gmail.com",
    description="A service to send message via Whatsapp messenger programmatically.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords=["whatsapp", "chat", "message", "web"],
    license="MIT",
    url="https://github.com/mblonyox/wasap",
    packages=find_packages(),
    python_requires=">=3.6.0",
    install_requires=["selenium", "click"],
    entry_points={
        "console_scripts": [
            "wasap-cli=wasap.cli:main",
            "wasap-service=wasap.service:main",
        ]
    }
)
