FROM ubuntu:18.04
RUN  apt update 
RUN  apt install -y python
ARG  param_expr
ENV  EXPR_TO_EVAL="${param_expr}"
COPY eval.py /
CMD  python /eval.py $EXPR_TO_EVAL /output/result
