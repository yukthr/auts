from influxdb import InfluxDBClient
client = InfluxDBClient(host='192.168.0.137', port=8086)
client.switch_database('mydb')

json_body = [
    {
        "measurement": "bme",
        "tags":
            {
                "tag1" : "val1"
            },
        "fields":
            {
                "temperature" : "40"
            }
    }
]

client.write_points(json_body)
print(client.get_list_measurements())
