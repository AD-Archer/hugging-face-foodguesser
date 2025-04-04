from setuptools import setup, find_packages

setup(
    name="food-category-classification",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.19.0",
        "matplotlib>=3.3.0",
        "pillow>=8.0.0",
        "transformers>=4.15.0",
        "torch>=1.10.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for classifying food images into categories",
    keywords="food, classification, deep-learning, image-processing",
    url="https://github.com/yourusername/food-category-classification",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
) 