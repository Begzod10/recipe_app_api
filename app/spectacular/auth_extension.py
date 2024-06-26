from drf_spectacular.contrib.rest_framework_simplejwt import SimpleJWTScheme

from app.custom_jwt.authentication import CustomJWTAuthentication


class SimpleJWTTokenUserScheme(SimpleJWTScheme):
    name = "CustomJWTAuth"
    target_class = CustomJWTAuthentication
