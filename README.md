# CD-FSOD
Here is the code for ``Cross-domain Few-shot Object Detection with Self-Ensemble and Self-Distillation''

Run the code and get the result

    ``
python train_net.py --num-gpus 4 --config-file ./configs/${dataset}/${shot}_shot.yaml 2>&1 | tee log/${dataset}/${shot}_shot.log
    ```
