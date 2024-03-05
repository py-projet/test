FROM ubuntu:22.04
WORKDIR /projet
RUN apt-get -y update && \
    apt-get install -y python3-pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py model.pkl ./
CMD ["streamlit", "run", "app.py"]