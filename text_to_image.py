from monsterapi import client
import requests       
from PIL import Image


# Initialize the client with your API key
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImY4N2JkN2YyNmM2NzhjNTc1MThhZWQ4ZjhlNmEwZjVmIiwiY3JlYXRlZF9hdCI6IjIwMjUtMDItMDRUMTU6NDg6MjAuNzgyODk5In0.RAysRzB2dWQzbuv4zKsO4xK0kQYONQvxNGnh_g_S_ts'  # Replace 'your-api-key' with your actual Monster API key
monster_client = client(api_key)


model = 'txt2img'  # Replace with the desired model name
input_data = {
'prompt': 'detailed sketch of lion by greg rutkowski, beautiful, intricate, ultra realistic, elegant, art by artgerm',
'negprompt': 'deformed, bad anatomy, disfigured, poorly drawn face',
'samples': 2,
'steps': 50,
'aspect_ratio': 'square',
'guidance_scale': 7.5,
'seed': 2414,
            }



result = monster_client.generate(model,input_data)
img_url = result['output'][0]
file_name = "image.png"
response = requests.get(img_url)
if response.status_code==200:
    with open(file_name,'wb') as file:
      file.write(response.content)
      print("Image downloaded")     
      img = Image.open(file_name)
      img.show()
else:
    print("failed to download the image")
 