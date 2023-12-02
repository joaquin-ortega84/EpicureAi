import comet_ml
from ultralytics import YOLO
import os
<<<<<<<< HEAD:Project/ml_logic/train.py
from Project.params import *
========
from epicureai.params import *
>>>>>>>> API:epicureai/ml_logic/train.py
import yaml

COMETML_APIKEY="7rjl1Zsakp1QfmEObqF7Df9Hr"
experiment = comet_ml.Experiment(
    api_key=COMETML_APIKEY,
    project_name="epicureai"
)

def train_model(epochs: int = 10, img_size: int = 512, verbose=True):
    comet_ml.init()

    # Load the pre-trained model
<<<<<<< HEAD
    model = YOLO("yolov8n.pt")

=======
    model = YOLO('yolov8n.yaml').load('yolov8n.pt')
>>>>>>> dc72aa5c011ce0186812a99cc18e247d34217a41
    # Train the model
    model.train(
        data=YAML_PATH,
        epochs=NUM_EPOCHS,
        imgsz=img_size,
        save=True,
<<<<<<< HEAD
        name="yolov8_custom",
=======
        device=DEVICE,
        name="yolov8_20_epochs",
>>>>>>> api-streamlit
        verbose=verbose
    )
    # Export the model to ONNX format
    path = model.export()
    print('✅ finished with training and exported the model' )


if __name__ == "__main__":
    train_model()
