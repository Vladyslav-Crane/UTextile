import logging

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # BLOCKED_IPS = []
        # block access for specific ips
        print('=================')
        
        # proccess_request
        try:
            response = self.get_response(request)
            # proccess response
        except Exception as e:
            # proccess_exception
            # return none - move exception further
            # return http response 
            return
        return response
