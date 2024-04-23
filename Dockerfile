ARG x=python
FROM ${x}
WORKDIR /test
COPY paragraphs.txt .
COPY cloudnlt.py .
RUN pip install nltk
RUN python -m nltk.downloader stopwords punkt
CMD python cloudnlt.py