import evaluate_metrics
from evaluate_metrics.utils import launch_gradio_widget


module = evaluate_metrics.load("perplexity", module_type= "measurement")
launch_gradio_widget(module)
