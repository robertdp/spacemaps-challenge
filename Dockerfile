FROM python:3-alpine

WORKDIR /spacemaps
COPY . .

RUN pip install micropipenv
RUN micropipenv install

ENTRYPOINT [ "python", "src/main.py" ]