ARG x=python
FROM ${x}
WORKDIR /test
COPY paragraphs.txt .
COPY cloudnlt.py .
RUN pip install nltk
CMD python cloudnlt.py