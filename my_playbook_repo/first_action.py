from robusta.api import *


@action
def my_first_action(event: PodEvent):

    pod = event.get_pod()

    # logic

    pod_name = pod.metadata.name

    # logic finish

    event.add_enrichment(MarkdownBlock(text=pod_name))
