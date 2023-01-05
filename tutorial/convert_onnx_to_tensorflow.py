import onnx

from onnx_tf.backend import prepare

onnx_model = onnx.load("onnx/yolov7_or.onnx")  # load onnx model
tf_rep = prepare(onnx_model)  # prepare tf representation
tf_rep.export_graph("saved")  # export the model