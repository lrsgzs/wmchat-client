from requests import get as _get
from requests import post as _post
from .utils import get_url_params

HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
}


def get(url: str, access_token: str = "", **kwargs):
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "http://" + url
    kwargs["access_token"] = access_token
    params = get_url_params(**kwargs)
    res = _get(f"{url}?{params}", headers=HEADER)
    if res.status_code != 200:
        return {"status": f"{res.status_code}ERROR", "data": None}
    else:
        return res.json()


def post(url: str, access_token: str = "", **kwargs):
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "http://" + url
    kwargs["access_token"] = access_token
    res = _post(url, data=kwargs, headers=HEADER)
    if res.status_code != 200:
        return {"status": f"{res.status_code}ERROR", "data": None}
    else:
        return res.json()
