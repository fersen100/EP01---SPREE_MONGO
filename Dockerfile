FROM python:3
ADD . /todo
WORKDIR /todo

#Install pymongo
RUN pip install pymongo
    
#Install flask
RUN pip install flask

#Install requests
RUN pip install requests

#Executa script python
#COPY mongo.py /home/debian/senac_spree/
#CMD ["python3","mongo.py"]
