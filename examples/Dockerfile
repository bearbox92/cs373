FROM python:3.5.2

RUN apt-get update            && \
    apt-get -y install cmake

RUN pip install --upgrade pip && \
    pip --version             && \
    pip install autopep8      && \
    pip install coverage      && \
    pip install mypy          && \
    pip install numpy         && \
    pip install pylint

CMD bash
