import os
from urllib.parse import urlsplit, urlunsplit, urlencode


def name(result):
    """The title for this Globus Search subject"""
    return result[0]["Name"]

def description(result):
    """The description for this Globus Search subject"""
    return result[0]["Description"]

def data_category(result):
    """The DataCategory for this Globus Search subject"""
    return result[0]["DataCategory"]

def globus_app_link(result):
    """A Globus Webapp link for the transfer/sync button on the detail page"""
    # url = result[0]["url"]
    url = result[0]["Weblink"]
    parsed = urlsplit(url)
    query_params = {
        "origin_id": parsed.netloc,
        "origin_path": os.path.dirname(parsed.path),
    }
    return urlunsplit(
        ("https", "app.globus.org", "file-manager", urlencode(query_params), "")
    )


def https_url(result):
    """Add a direct download link to files over HTTPS"""
    # path = urlsplit(result[0]["url"]).path
    # return urlunsplit(("https", "g-71c9e9.10bac.8443.data.globus.org", path, "", ""))
    return result[0]["Weblink"]