from setuptools import setup

setup(
	name = "Emojis",
	version = "0.2", # ?
	author = "ruby#7777",
	py_modules = ["bot", "information", "settings"],
	install_requires = [
	"aiohttp==3.6.2",
	"async-timeout==3.0.1",
	"asyncio==3.4.3",
	"attrs==20.1.0",
	"certifi==2020.6.20",
	"chardet==3.0.4",
	"discord==1.0.1",
	"discord.py==1.4.1",
	"idna==2.10",
	"multidict==4.7.6",
	"pymongo==3.11.0",
	"requests==2.24.0",
	"urllib3==1.25.10",
	"yarl==1.5.1"
	]
)
