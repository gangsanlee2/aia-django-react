FROM mysql:5.7
RUN apt update -y  \
    && apt install -y mysql-server-5.7  \
    && apt install --no-install-recommends -y tzdata  \
    && apt clean \