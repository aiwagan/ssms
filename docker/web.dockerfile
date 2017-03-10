FROM python:2.7
ADD ../ssms /ssms
WORKDIR /ssms
RUN pip install -r /ssms/requires/requirements.txt
 
