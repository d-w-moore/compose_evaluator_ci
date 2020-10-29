FROM ubuntu:18.04
RUN  apt update 
RUN  apt install -y python
COPY eval.py /
CMD  python /eval.py "$PARAMETER_EXPR" /output/result
