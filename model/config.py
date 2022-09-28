from detectron2.config import CfgNode as CN


def add_kd_config(cfg):
    """
    Add config.
    """
    _C = cfg
    _C.TEST.VAL_LOSS = True

    _C.MODEL.RPN.UNSUP_LOSS_WEIGHT = 1.0
    _C.MODEL.RPN.LOSS = "CrossEntropy"
    _C.MODEL.ROI_HEADS.LOSS = "CrossEntropy"

    _C.SOLVER.IMG_PER_BATCH_LABEL = 1
    _C.SOLVER.IMG_PER_BATCH_UNLABEL = 1
    _C.SOLVER.FACTOR_LIST = (1,)

    _C.TEST.EVALUATOR = "COCOeval"

    _C.KD = CN()

    # Output dimension of the MLP projector after `res5` block
    _C.KD.MLP_DIM = 128

    # Semi-supervised training
    _C.KD.BBOX_THRESHOLD = 0.7
    _C.KD.PSEUDO_BBOX_SAMPLE = "thresholding"
    _C.KD.TEACHER_UPDATE_ITER = 1
    _C.KD.BURN_UP_STEP = 12000
    _C.KD.EMA_KEEP_RATE = 0.0
    _C.KD.LOSS_WEIGHT = 4.0
    _C.KD.LOSS_WEIGHT_TYPE = "standard"


    _C.EMAMODEL = CN()
    _C.EMAMODEL.SUP_CONSIST = True
    
