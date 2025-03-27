"""
Setup script for the job_search package.
"""

from setuptools import setup, find_packages

setup(
    name="job_search",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "torch",
        "transformers",
        "faiss-cpu",
        "psycopg2-binary",
        "pdfplumber",
        "docx2txt",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="Job search system using FAISS and BERT embeddings",
    keywords="job search, faiss, bert, embeddings",
    python_requires=">=3.6",
)
