#!/usr/bin/python3
""" this module contains class BaseModel that defines all common attributes/methods for other classes"""

from datetime import datetime
import uuid


class BaseModel:
	""" class that defines all common attributes/methods for other classes"""
	def __init__(self, id, created_at, updated_at):
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = created_at
	
	def __str__(self):
		""" Returns a string represantation of BaseModel"""
		return f"[{self.class name}] ({self.id}) {self.__dict__}"
	
	def save(self):
		self.updated_at = datetime.now
	
	def to_dict(self):
		mydict_ = self.__dict__.copy()
		mydict_("__class__") = self.__class__.name
		mydict_("created_at") = mydict_("created_at").isoformat()
		mydict_("updated_at") = mydict_("updated_at").isoformat()
	    return mydict_

	