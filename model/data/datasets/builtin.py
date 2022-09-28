import os

from detectron2.data import DatasetCatalog
from detectron2.data import MetadataCatalog
from detectron2.data.datasets.coco import load_coco_json
import json
from detectron2.data.datasets import register_coco_instances

_PREDEFINED = [
    ("DIOR_train", "DIOR/train", "DIOR/annotations/train.json"),
    ("DIOR_test", "DIOR/test", "DIOR/annotations/test.json"),
    ("ArTaxOr_train", "ArTaxOr/train", "ArTaxOr/annotations/train.json"),
    ("ArTaxOr_test", "ArTaxOr/test", "ArTaxOr/annotations/test.json"),
    ("UODD_train", "UODD/train", "UODD/annotations/train.json"),
    ("UODD_test", "UODD/test", "UODD/annotations/test.json"),
    ("ChestX_train", "ChestX/train", "ChestX/annotations/train.json"),
    ("ChestX_test", "ChestX/test", "ChestX/annotations/test.json"),,
]


for shot in [1,5,10]:
    new_anns =  ("DIOR_{}shot".format(shot),
               "DIOR/train",
               "DIOR/{}_shot.json".format( shot)) 
    _PREDEFINED.append(new_anns)
  
  
    new_anns =  ("ArTaxOr_{}shot".format(shot),
    "ArTaxOr/train",
    "ArTaxOr/annotations/{}_shot.json".format(shot)) 
    _PREDEFINED.append(new_anns)
  
  
    new_anns =  ("UODD_{}shot".format(shot),
    "UODD/train",
    "UODD/annotations/{}_shot.json".format(shot)) 
    _PREDEFINED.append(new_anns)
  
  
  new_anns =  ("ChestX_{}shot".format(shot),
   "ChestX/train",
   "ChestX/annotations/{}_shot.json".format(shot)) 
  _PREDEFINED.append(new_anns)



def register_data(root):
    for name, image_dir, json_file in _PREDEFINED:
        with open(os.path.join(root, json_file), "r", encoding="utf-8") as f:
            data = json.load(f)
        classes = [i["name"] for i in data["categories"]]
        register_coco_instances(name, {}, os.path.join(root, json_file), os.path.join(root, image_dir))
        MetadataCatalog.get(name).set(thing_classes=classes)

# Register them all under "./datasets"
_root = os.getenv("DETECTRON2_DATASETS", "datasets")
register_data(_root)
