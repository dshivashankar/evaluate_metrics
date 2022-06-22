import evaluate_metrics
from evaluate_metrics.utils import launch_gradio_widget


module = evaluate_metrics.load("{{ cookiecutter.namespace }}/{{ cookiecutter.module_slug }}")
launch_gradio_widget(module)