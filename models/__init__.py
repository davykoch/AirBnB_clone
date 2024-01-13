#!/usr/bin/python3
"""This module instantiates a unique FileStorage"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
