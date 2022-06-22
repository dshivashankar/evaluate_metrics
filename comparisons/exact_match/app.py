import evaluate_metrics
from evaluate_metrics.utils import launch_gradio_widget


module = evaluate_metrics.load("exact_match", module_type="comparison")
launch_gradio_widget(module)
