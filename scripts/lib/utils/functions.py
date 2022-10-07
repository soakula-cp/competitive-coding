import json
import logging
import os
import pathlib
import time
from datetime import datetime
from typing import Dict, List

import requests

from lib.utils.enums import WriteContentEnum, ApiEnum


def create_directory(dirname: str) -> bool:
    """
    Creates an empty directory
    Args:
        dirname: Name/Path of the directory

    Returns:
        True if a new directory was created else False
    """
    if not os.path.exists(dirname):
        logging.debug(f"Creating directory: '{dirname}'")
        os.makedirs(dirname)
        return True
    return False


def create_empty_file(filename: str) -> bool:
    """
    Creates an empty file
    Args:
        filename: Name/Path of the file

    Returns:
        True if a new file was created else False
    """
    if not os.path.exists(filename):
        dirname = os.path.dirname(filename)
        create_directory(dirname)
        logging.debug(f"Creating empty file: '{filename}'")
        pathlib.Path(filename).touch()
        return True
    return False


def get_response(url: str) -> str:
    """
    Retrieve response from the given URL
    Args:
        url: URL for which response is to be retrieved

    Returns:
        Response for the URL
    """
    logging.debug(f"Url: {url}")
    response = requests.get(url)
    while response.status_code == 503:
        time.sleep(1)
        response = requests.get(url)
    return response.text


def make_api_call(url: str, filename: str,
                  api_type: ApiEnum = ApiEnum.DEFAULT,
                  headers=None, data=None,
                  force: bool = False) -> dict:
    """
    Makes a network call and returns response
    Args:
        url: URL which needs to be queried
        filename: Name of the file in which the url response is cached
        api_type: Type of Api call. Default: DEFAULT
        headers: Headers required for GraphQL Api call
        data: Data for the GraphQL Api call
        force: If API call is to be made from network instead of file.
               Default: False

    Returns:
        JSON response from the API call
    """
    response = None
    if len(url) == 0:
        return {}
    if len(filename) == 0:
        force = True
    if api_type == ApiEnum.GRAPHQL:
        if headers is None or data is None:
            return {}
    current_timestamp = time.mktime(datetime.today().timetuple())
    if force or not os.path.exists(filename) or \
        (os.path.exists(filename) and
         current_timestamp - os.path.getmtime(filename) > 604800):
        logging.debug(f"Querying API: '{url}'")
        if api_type == ApiEnum.GRAPHQL:
            response = requests.post(url, headers=headers,
                                     data=data).content
        else:
            response = get_response(url)
        # Convert string response to dictionary
        response = json.loads(response)
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        with open(filename, "w") as write_file:
            json.dump(response, write_file)
    else:
        logging.debug(f"Reading API response from file: '{filename}'")
        with open(filename, "r") as read_file:
            response = json.load(read_file)
    return response


def get_filename(write_type: WriteContentEnum) -> (str, str):
    """

    Args:
        write_type: Type of the file to be written

    Returns:
        Name of the file, extension of the file
    """
    file_extension: Dict[WriteContentEnum, str] = {
        WriteContentEnum.SOLUTION: "cpp",
        WriteContentEnum.DESCRIPTION: "md",
        WriteContentEnum.TESTCASES: "txt",
    }
    return (f"{str(write_type).lower()}.{file_extension[write_type]}",
            file_extension[write_type])


def get_lines_in_a_file(path: str) -> List[str]:
    """

    Args:
        path:

    Returns:

    """
    file_handle = open(path, "r", encoding="utf-8")
    lines = file_handle.readlines()
    file_handle.close()
    return lines


def remove_comments(lines: List[str]) -> List[str]:
    if lines is None:
        return []
    cleaned_code = []
    for line in lines:
        temp_line = line.strip()
        if not (
            "//" in temp_line[:2] or "/**" in temp_line[:3] or "*" in temp_line[
                                                                      :1]):
            cleaned_code.append(line)
    return cleaned_code
