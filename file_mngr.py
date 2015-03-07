import os
from keith.array_tools import array_remove_array


class My_Files(object):
	def __init__(self, root_dir):
		#make sure the directory passed is valid
		root_dir = os.path.expanduser(root_dir)
		if os.path.isdir(root_dir):
			self.root = root_dir
		else:
			raise NameError("Invalid Directory or directory doesn't exist " + root_dir)
		self.tree = os.walk(self.root)
		self.all_files = []
		self.all_dirs = []
		self.filtered_files = []
		self.all_files = self._get_all_files()
		self.all_dirs = self._get_all_directories()


	def filter_files(self, filters=[], filter_out=True):
		if not self.filtered_files:
			self.filtered_files = list(self.all_files)
		to_remove = []
		if filters:
			for level in range(0,len(self.filtered_files)):
				if self._contains(filters, self.filtered_files[level]) == filter_out:
					to_remove.append(self.filtered_files[level])
		self.filtered_files = array_remove_array(self.filtered_files, to_remove)

	def filter_dirs(self, filters=[], filter_out=True):
		if not self.filtered_dirs:
			self.filtered_dirs = list(self.all_dirs)
		to_remove = []
		if filters:
			for level in range(0,len(self.filtered_dirs)):
				if self._contains(filters, self.filtered_dirs[level]) == filter_out:
					to_remove.append(self.filtered_dirs[level])
		self.filtered_dirs = array_remove_array(self.filtered_dirs, to_remove)


	def filter_files_hidden(self):
		if not self.filtered_files:
			self.filtered_files = list(self.all_files)
		to_remove = []
		if filters:
			for level in range(0,len(self.filtered_files)):
				if self._contains(['/.'], self.filtered_files[level]):
					to_remove.append(self.filtered_files[level])
		self.filtered_files = array_remove_array(self.filtered_files, to_remove)


	def filter_dirs_hidden(self):
		if not self.filtered_dirs:
			self.filtered_dirs = list(self.all_dirs)
		to_remove = []
		if filters:
			for level in range(0,len(self.filtered_dirs)):
				if self._contains(['/.'], self.filtered_dirs[level]):
					to_remove.append(self.filtered_dirs[level])
		self.filtered_dirs = array_remove_array(self.filtered_dirs, to_remove)


	def reset_filter(self, what='all'):
		what =  what.upper()
		if what == 'ALL' or what == 'BOTH':
			self.filtered_dirs = self._get_all_directories()
			self.filtered_files = self._get_all_files()

		if what == 'FILES':
			self.filtered_files = self._get_all_files()

		if what == 'DIRS':
			self.filtered_dirs = self._get_all_directories()


	def file_name_only(self, files):
		files_list = list(files)
		for i in range(0, len(files_list)):
			files_list[i] = os.path.split(files_list[i])[1]
		return files_list

	
	def _contains(self, filters, chk_str):
		for a in filters:
			if a in chk_str:
				return True
		return False


	def _get_all_files(self):
		all_files = []
		for root, dirs, files in os.walk(self.root):
			for a in files:
				all_files.append(os.path.join(root,a))

		return all_files


	def _get_all_directories(self):
		# Get the directories in the root directory
		all_dirs = []
		for root, dirs, files in os.walk(self.root):
			for a in dirs:
				all_dirs.append(os.path.join(root,a))
		return all_dirs