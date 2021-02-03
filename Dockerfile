FROM ubuntu:18.04
MAINTAINER 'lixin' lixin@moviebook.cn

WORKDIR /home/

# 重型任务区
# 阿里源[无奈脸]
COPY conf/sources.list /etc/apt/sources.list
# 豆瓣源
# COPY命令中不能使用`~`定位主目录
COPY conf/pip.conf /root/.pip/pip.conf

# python
RUN deps='python3.6-dev python3-pip'; \
    set -x \
    && apt-get update && apt-get install -y $deps --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# opencv
RUN deps='libsm6 libxext6 libxrender1'; \
    set -x \
    && apt-get update && apt-get install -y $deps --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN deps='setuptools wheel'; \
    set -x \
    && pip3 install $deps

# dlib
RUN deps='build-essential libgtk-3-dev libboost-all-dev'; buildDeps='cmake' \
    set -x \
    && apt-get update && apt-get install -y $deps $buildDeps --no-install-recommends \
    && pip3 install dlib==19.17.0 \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove $buildDeps

# 轻型任务区
EXPOSE 5000

COPY requirements.txt .
RUN pip3 install -r requirements.txt

# 常变任务区
COPY . /home/
ENTRYPOINT ["bash"]
