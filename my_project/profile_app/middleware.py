import time, datetime
from profile_app.models import Logger
from profile_app import model_choices as mch


class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.current_time = datetime.datetime.now()
        t1 = time.time()
        response = self.get_response(request)
        t2 = time.time()

        Logger.objects.create(
            path=request.path,
            method=mch.METHOD_CHOICES_REVERSED[request.method],
            time_delta=t2 - t1
        )

        return response
