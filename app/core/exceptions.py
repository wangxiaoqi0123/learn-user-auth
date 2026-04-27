class AppException(Exception):
    """
    所有异常的基类
    """

    code: str = "UNKNOWN_ERROR"
    status_code = 500
    message = "服务器内部错误"

    def __init__(self, message: str | None = None, *, field: str | None = None):
        self.message = message
        self.field = field
        super().__init__(self.message)


class TokenExpiredError(AppException):
    code = "TOKEN_EXPIRED"
    status_code = 401
    message = "Token 已过期"


class TokenInvalidError(AppException):
    code = "TOKEN_INVALID"
    status_code = 401
    message = "Token 无效"
