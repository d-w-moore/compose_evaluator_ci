FROM ubuntu:18.04
RUN  apt update 
RUN  apt install -y python

ARG  ARG_PLATFORM
ENV  ENV_PLATFORM=${ARG_PLATFORM}

COPY eval.py /

CMD bash -c "echo == ${ENV_PLATFORM} == >/output/result ; python /eval.py /output/result"
