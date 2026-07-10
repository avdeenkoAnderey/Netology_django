from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class Anon10PerMinute(AnonRateThrottle):
    rate = "10/min"


class User20PerMinute(UserRateThrottle):
    rate = "20/min"

