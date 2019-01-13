from django.conf import settings

from error.models import Error


class CatchErrorMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code in settings.ERROR_STATUS_CODE:
            error_status = response.status_code
            error_text = response.reason_phrase
            obj = Error(error_status=error_status,error=error_text)
            obj.save()

            response.status_code = 200
            response.reason_phrase = 'Error'
            response.content = "{'status_code':200,'error':'Error'}"
        return response
