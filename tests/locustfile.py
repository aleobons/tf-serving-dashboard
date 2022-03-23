from locust import HttpUser, task
import os
import base64
import json


class LoadTest(HttpUser):
    host = "http://localhost"

    @task
    def predict_placa_veiculo_direct(self):
        image_path = "00011.jpg"

        with open(os.path.join('files', image_path), "rb") as image:
            encoded_input_image_string = base64.b64encode(image.read())
            input_image_string = encoded_input_image_string.decode("utf-8")

            data = [{"b64": input_image_string}]
            data = json.dumps({"instances": data})

            headers = {"content-type": "application/json"}

            url = 'http://localhost:8501/v1/models/tensorflow_model:predict'

            self.client.request("POST", url, data=data, headers=headers)
