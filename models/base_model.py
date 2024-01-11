#!/usr/bin/python3
""" this module contains class BaseModel that defines all common attributes/methods for other classes"""

import datetime
import uuid


class BaseModel:
	""" class that defines all common attributes/methods for other classes"""
	def __init__(self, id, created_at, updated_at):
		self.id = id
		self.created_at = created_at
		self.updated_at = updated_at

	@property
	def id(self):
		"""Retrieves the attribute"""
		return self.id
	
	@id.setter
	def id(self, value):
		"""Sets the attribute"""
		if type(value) is not str:
			raise TypeError("id should be a string")
		id = uuid.uuid4()
		print(id)
		self.id = value
	
	@property
	def created_at(self):
		"""Retrieves the attribute"""
		return self.created_at
	
	@created_at.setter
	def created_at(self, value):
		"""Sets the attribute"""
		if type(value) is not int:
			raise TypeError("")
		