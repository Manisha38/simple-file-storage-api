import unittest
from main import *
import os
import re

class S3Tests(unittest.TestCase):
	fname = 'file1.doc'
	setFlag("aws")

	def test_fCreate(self):
		self.assertEqual(fCreate(self.fname),"Created File")

	def test_fOpen(self):
		self.assertNotEquals(fOpen(self.fname),'File does not exists')

	def test_fOpen_file_not_present(self):
		fname2 = 'file2.doc'
		self.assertEquals(fOpen(fname2),'File does not exists')

	def test_fRename(self):
		new_fname = 'new_file.doc'
		self.assertEquals(fRename(self.fname,new_fname),'File name changed')

	def test_fname_file_not_present(self):
		fname='file2.doc'
		new_fname = 'abc.doc'
		self.assertEquals(fRename(fname,new_fname),'File does not exists')

	def test_fDelete(self):
		fname = 'new_file.doc'
		self.assertEquals(fDelete(fname),'Deleted file')


class  FsTests(unittest.TestCase):
	"""docstring for  FsTests"unittest.TestCasef __init__(self, arg):
		super( FsTests,unittest.Te
		stCase.__init__()
		self.arg = arg
	"""
	fname = 'file1.doc'
	setFlag("filesystem")

	def test_fCreate(self):
		self.assertEqual(fCreate(self.fname),"Created File")

	def test_fOpen(self):
		self.assertNotEquals(fOpen(self.fname),'File does not exists')

	def test_fOpen_file_not_present(self):
		fname2 = 'file2.doc'
		self.assertEquals(fOpen(fname2),'File does not exists')

	def test_fRename(self):
		new_fname = 'new_file.doc'
		self.assertEquals(fRename(self.fname,new_fname),'File name changed')

	def test_fname_file_not_present(self):
		fname='file2.doc'
		new_fname = 'abc.doc'
		self.assertEquals(fRename(fname,new_fname),'File does not exists')

	def test_fDelete(self):
		fname = 'new_file.doc'
		self.assertEquals(fDelete(fname),'Deleted file')


		

if __name__=='__main__':
	unittest.main()