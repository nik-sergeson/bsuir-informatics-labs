from django.dispatch import Signal

proposal_closed = Signal(providing_args=["proposal"])
request_closed = Signal(providing_args=["request"])