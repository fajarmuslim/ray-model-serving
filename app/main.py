from ray import serve
from typing import Dict, List
from joblib import load
from app.schemas.iris import IrisRequest
from app.utils.constant import MODEL_PATH

@serve.deployment()
class IrisPredictor:
    def __init__(self, *args, **kwargs):
        self.model = load(MODEL_PATH)


    async def __call__(self, request: IrisRequest) -> Dict[str, List[int]]:
        json_request =  await request.json()
        formatted_features = [[json_request['sepal_length'],json_request['sepal_width'],json_request['petal_length'],json_request['petal_width']]]
        result = self.model.predict(formatted_features)
        print({"result": result.tolist()[0]})
        return {"result": result.tolist()[0]}




iris = IrisPredictor.bind(http_adapter=IrisRequest)
