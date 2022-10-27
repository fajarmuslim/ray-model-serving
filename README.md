# ray-model-serving

## How to run
1. Install all the dependencies
```bash
pip3 install -r requirements.txt
```
2. Run with this following command
```bash
serve run app.main:iris
```
Those command will run API server and serve on the http://127.0.0.1:8000/ port

## How to test the API
Use this python file
```python
import requests

sample_request_input = {
    "sepal_length": 1.2,
    "sepal_width": 1.0,
    "petal_length": 1.1,
    "petal_width": 0.9,
}
response = requests.get("http://localhost:8000/", json=sample_request_input)
print(response.text)
```

The above command will return this result `{'result': 0}`