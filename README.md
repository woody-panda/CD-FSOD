# CD-FSOD
Here is the code for ``Cross-domain Few-shot Object Detection with Self-Ensemble and Self-Distillation''

[Get preprocessed data and weights pretrained on MS COCO dataset from here](URL). Run the code and get the result

    
    python train_net.py --num-gpus 4 --config-file ./configs/${dataset}/${shot}_shot.yaml 2>&1 | tee log/${dataset}/${shot}_shot.log
    
