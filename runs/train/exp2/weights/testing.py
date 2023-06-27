convert2version5 = True
if convert2version5:
    from torch.jit.mobile import (
        _backport_for_mobile,
        _get_model_bytecode_version,
    )

    MODEL_INPUT_FILE = "yolov8/best.torchscript.ptl"
    MODEL_OUTPUT_FILE = "yolov8/best_5.torchscript.ptl"

    print("model version", _get_model_bytecode_version(f_input=MODEL_INPUT_FILE))

    _backport_for_mobile(f_input=MODEL_INPUT_FILE, f_output=MODEL_OUTPUT_FILE, to_version=5)

    print("new model version", _get_model_bytecode_version(MODEL_OUTPUT_FILE))

