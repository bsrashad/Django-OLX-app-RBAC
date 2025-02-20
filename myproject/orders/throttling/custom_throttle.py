
from rest_framework.throttling import BaseThrottle,SimpleRateThrottle
from django.core.cache import cache

class CustomRateThrottle(BaseThrottle):
    def allow_request(self, request, view):
        ip_address = request.META.get('REMOTE_ADDR')
        print(ip_address)
        rate_limit_key = f"custom_rate_limit_{ip_address}"
        print(rate_limit_key)
        requests = cache.get(rate_limit_key, 0)
        print("request",requests)

        if requests >= 7:  
            return False

        cache.set(rate_limit_key, requests + 1, timeout=60)  
        return True

    def wait(self):
        return 60 

# class ScopedRateThrottle(SimpleRateThrottle):
#     """
#     Limits the rate of API calls by different amounts for various parts of
#     the API. Any view that has the `throttle_scope` property set will be
#     throttled. The unique cache key will be generated by concatenating the
#     user id of the request, and the scope of the view being accessed.
#     """
#     scope_attr = 'throttle_scope'

#     def __init__(self):
#         # Override the usual SimpleRateThrottle, because we can't determine
#         # the rate until called by the view.
#         pass

#     def allow_request(self, request, view):
#         # We can only determine the scope once we're called by the view.
#         self.scope = getattr(view, self.scope_attr, None)

#         # If a view does not have a `throttle_scope` always allow the request
#         if not self.scope:
#             return True

#         # Determine the allowed request rate as we normally would during
#         # the `__init__` call.
#         self.rate = self.get_rate()
#         self.num_requests, self.duration = self.parse_rate(self.rate)

#         # We can now proceed as normal.
#         return super().allow_request(request, view)

#     def get_cache_key(self, request, view):
#         """
#         If `view.throttle_scope` is not set, don't apply this throttle.

#         Otherwise generate the unique cache key by concatenating the user id
#         with the `.throttle_scope` property of the view.
#         """
#         if request.user and request.user.is_authenticated:
#             ident = request.user.pk
#         else:
#             ident = self.get_ident(request)

#         return self.cache_format % {
#             'scope': self.scope,
#             'ident': ident
#         }

