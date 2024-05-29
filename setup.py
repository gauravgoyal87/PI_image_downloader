import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PI_image_downloader",
    version="1.1.2",
    author="Gaurav Goyal",
    author_email="gauravgoyal4000@gmail.com",
    description="Python library to download bulk images from Bing.com, modified from Guru Prasad",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gauravgoyal87/PI_image_downloader",
    keywords=['bing', 'images', 'scraping', 'image download', 'bulk image downloader',],
    packages=['bing_image_downloader'],
    classifiers=[
	"Programming Language :: Python :: 3",
	"License :: OSI Approved :: MIT License",
	"Operating System :: OS Independent",
        ]
)
