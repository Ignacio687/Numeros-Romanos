FROM python:3
RUN git clone https://github.com/Ignacio687/Listas-Diccionarios.git
WORKDIR /Listas-Diccionarios
RUN pip install -r requirements.txt
CMD ["python3", "-m", "unittest"]