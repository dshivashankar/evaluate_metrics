import sys

import evaluate_metrics
from evaluate_metrics.utils import launch_gradio_widget


sys.path = [p for p in sys.path if p != "/home/user/app"]
module = evaluate_metrics.load("bleurt")
sys.path = ["/home/user/app"] + sys.path

launch_gradio_widget(module)
