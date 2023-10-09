import requests
import json
import time

import Variables

from PIL import Image
def Show():
    im = Image.open(r"{}\image.jpg".format(PATH)) 
    im.show() 


import pathlib
PATH = pathlib.Path(__file__).parent.resolve()


T_Weight = float(Variables.Weight_v())

Width = int(Variables.Width_v())
Height = int(Variables.Height_v())




BASE_URL = "https://api.luan.tools/api/tasks/"
HEADERS = {
    'Authorization': 'bearer p8q739jd8WxYUrFu5g7MRPT76TjTxgp1',
    'Content-Type': 'application/json'
}


def send_task_to_image_gen(style_id, prompt, target_img_path=None):

    post_payload = json.dumps({
        "use_target_image": bool(target_img_path)
    })
    post_response = requests.request(
        "POST", BASE_URL, headers=HEADERS, data=post_payload)
    

    if target_img_path:
        target_image_url = post_response.json()["target_image_url"]
        with open(target_img_path, 'rb') as f:
            fields = target_image_url["fields"]
            fields ["file"] = f.read()
            requests.request("POST", url=target_image_url["url"], files=fields)


    task_id = post_response.json()['id']
    task_id_url = f"{BASE_URL}{task_id}"
    put_payload = json.dumps({
        "input_spec": {
            "style": style_id,
            "prompt": prompt,
            "target_image_weight": T_Weight,
            "width": Width,
            "height": Height
    }})
    requests.request(
        "PUT", task_id_url, headers=HEADERS, data=put_payload)


    while True:
        response_json = requests.request(
            "GET", task_id_url, headers=HEADERS).json()

        state = response_json["state"]

        if state == "completed":
            r = requests.request(
                "GET", response_json["result"])
            with open("image.jpg", "wb") as image_file:
                image_file.write(r.content)
            print("Image created successfully!")

            Show()

            break

        elif state =="failed":
            print("Image generation failed")
            break

        time.sleep(3)
    
