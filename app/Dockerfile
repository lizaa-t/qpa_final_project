FROM python:3.9

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/qpa_final_project/"
ENV PYTHONUNBUFFERED 1
ENV DB_USER qpa
ENV DB_PASSWORD qpafinalproject
ENV APP_DIR /usr/src/qpa_final_project/app/

RUN mkdir -p /usr/src/qpa_final_project/
WORKDIR /usr/src/qpa_final_project/app/

COPY . /usr/src/qpa_final_project/app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
