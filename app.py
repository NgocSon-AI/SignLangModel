from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image
import torch

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load YOLO model (YOLOv5 hoặc YOLOv8 đều được)
model = torch.hub.load('./yolov5', 'custom', path='yolov5/yolov5s.pt', source='local', force_reload=True)

model.conf = 0.5

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    img_data = data['image'].split(",")[1]
    img_bytes = base64.b64decode(img_data)
    img = Image.open(BytesIO(img_bytes)).convert("RGB")

    # Convert to OpenCV
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Run YOLO
    results = model(frame)
    pred = results.pandas().xyxy[0]

    if len(pred) > 0:
        label = pred.iloc[0]['name']
    else:
        label = "No sign detected"

    return JSONResponse({"label": label})
