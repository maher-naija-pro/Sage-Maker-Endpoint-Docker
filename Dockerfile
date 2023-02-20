FROM tensorflow/serving
RUN apt-get update   

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         python3-distutils \
         python3 \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://bootstrap.pypa.io/pip/3.6/get-pip.py && python3 get-pip.py && \
    pip install --no-cache-dir numpy tensorflow flask gevent && \
        rm -rf /root/.cache



ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

COPY SRC /opt/program
WORKDIR /opt/program
ENTRYPOINT ["python3", "serve.py"]


