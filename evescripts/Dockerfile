FROM amazonlinux
COPY requirements.txt /tmp/
COPY . /gcp
RUN yum update -y && yum install python3 -y && yum install python3-pip -y && yum install vim -y
RUN pip3 install --requirement /tmp/requirements.txt
RUN export GOOGLE_APPLICATION_CREDENTIALS="/gcp/credentials.json"
