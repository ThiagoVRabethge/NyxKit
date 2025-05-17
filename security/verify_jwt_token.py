from decouple import config
from fastapi import Header, HTTPException
from jose import ExpiredSignatureError, JWTError, jwt


def handle_verify_jwt_token(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=400, detail="Invalid token format")

    token = authorization[7:]

    try:
        secret = config("SECRET")

        algorithm = config("ALGORITHM")

        payload = jwt.decode(token, secret, algorithms=[algorithm])

        return payload

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
