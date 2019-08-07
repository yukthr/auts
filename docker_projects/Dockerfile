FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./awspub_server.py -e aem6lj2h0o713-ats.iot.us-east-1.amazonaws.com -r root-CA.crt -c raspberrypioffice.cert.pem -k raspberrypioffice.private.key" ]