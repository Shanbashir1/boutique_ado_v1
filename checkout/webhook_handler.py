from django.http import HttpResponse


class StripeWH_Handler:
    """Handles Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handles a generic/unknown/unexpected webhook"""
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handles the payment_intent_succeeded webhook from stripe"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handles the payment_intent_payment_failed webhook from stripe"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)