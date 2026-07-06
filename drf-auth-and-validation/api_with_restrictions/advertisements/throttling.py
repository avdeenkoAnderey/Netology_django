from rest_framework.throttling import SimpleRateThrottle

class AnonRateThrottle(SimpleRateThrottle):
    scope = 'anon'
    rate = '10/min'

class UserRateThrottle(SimpleRateThrottle):
    scope = 'user'
    rate = '20/min'
