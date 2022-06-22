import evaluate_metrics
from evaluate_metrics.utils import launch_gradio_widget


module = evaluate_metrics.load("text_duplicates")
launch_gradio_widget(module)
