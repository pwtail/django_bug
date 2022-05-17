
def buggg(get_response):
    def middleware(request):
        response = get_response(request)
        return response

    return middleware

buggg.async_capable = True