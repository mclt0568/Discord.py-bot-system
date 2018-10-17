# Copyright (c) 2018 mclt0568 (For more information see LICENCE)
import sys
import bot_config as cfg
from time import gmtime, strftime
from datetime import datetime

class log_option:
	def __init__ (self,_path):
		global INITCFG
		config = cfg.init(_path)
		INITCFG = config.initconfig()
		self.path = _path
	"""settings about the logs"""
	def set_bracket(self,open_bracket:str,close_bracket:str):
		"""the breakets while displaing the time, date, information etc"""
		global BRACKETS
		BRACKETS = [open_bracket,close_bracket]
		return BRACKETS
	def set_filenames(self,filename_prefix:str,filename_suffix):
		"""the prefix and suffix of the file name that saves the logs to"""
		global FILENAME
		FILENAME = [filename_prefix,filename_suffix]
		return FILENAME
	def set_writemode(self,mode="a",encoding="utf8"):
		"""set the write mode for log files"""
		global WRITEMODE
		WRITEMODE = {
			"mode":mode,
			"encoding":encoding
		}
		return WRITEMODE
	def getfileinfo(self):
		global INITCFG
		fileinfo = [self.path,INITCFG["logcount"]]
		return fileinfo
class logs:
	def __init__(self,fileinfo,_BRACKETS=["[","]"],_FILENAME=["BOT_LOG",".txt"],_WRITEMODE={"mode":"a","encoding":"utf8"}):
		self.BRACKETS = _BRACKETS
		self.FILENAME = _FILENAME
		self.WRITEMODE = _WRITEMODE
		self.FILEINFO = fileinfo
		self.count = self.update_file()
	def update_file(self):
		try:
			with open(self.FILEINFO[0]+"\\logs\\"+self.FILEINFO[1],"r") as a:
				data = str(int(a.read())+1)
			with open(self.FILEINFO[0]+"\\logs\\"+self.FILEINFO[1],"w+") as a:
				a.write(data)
			return str(int(data)-1)
		except Exception:
			with open(self.FILEINFO[0]+"\\logs\\"+self.FILEINFO[1],"w+") as a:
				a.write("0")
			return 0
	def log(self,text,tags:list=[]):
		time_now =  self.BRACKETS[0]+str(datetime.now())+self.BRACKETS[1]
		prefix = ""
		prefix += (time_now+self.BRACKETS[0]+"LOG"+self.BRACKETS[1])
		for item in tags:
			prefix += self.BRACKETS[0]+item+self.BRACKETS[1]
		output_text = prefix + text + "\n"
		sys.stdout.write(output_text)
		filename = self.FILENAME[0] + str(self.count) + self.FILENAME[1]
		with open(self.FILEINFO[0]+"\\logs\\"+filename,self.WRITEMODE["mode"],encoding=self.WRITEMODE["encoding"]) as w:
			w.write(output_text)
	def log_error(self,text,tags:list=[]):
		time_now =  self.BRACKETS[0]+str(datetime.now())+self.BRACKETS[1]
		prefix = ""
		prefix += (time_now+self.BRACKETS[0]+"ERROR"+self.BRACKETS[1])
		for item in tags:
			prefix += self.BRACKETS[0]+item+self.BRACKETS[1]
		output_text = prefix + text + "\n"
		sys.stdout.write(output_text)
		filename = self.FILENAME[0] + str(self.count) + self.FILENAME[1]
		with open(self.FILEINFO[0]+"\\logs\\"+filename,self.WRITEMODE["mode"],encoding=self.WRITEMODE["encoding"]) as w:
			w.write(output_text)
	def log_warn(self,text,tags:list=[]):
		time_now =  self.BRACKETS[0]+str(datetime.now())+self.BRACKETS[1]
		prefix = ""
		prefix += (time_now+self.BRACKETS[0]+"WARN"+self.BRACKETS[1])
		for item in tags:
			prefix += self.BRACKETS[0]+item+self.BRACKETS[1]
		output_text = prefix + text + "\n"
		sys.stdout.write(output_text)
		filename = self.FILENAME[0] + str(self.count) + self.FILENAME[1]
		with open(self.FILEINFO[0]+"\\logs\\"+filename,self.WRITEMODE["mode"],encoding=self.WRITEMODE["encoding"]) as w:
			w.write(output_text)
	def log_event(self,text,tags:list=[]):
		time_now =  self.BRACKETS[0]+str(datetime.now())+self.BRACKETS[1]
		prefix = ""
		prefix += (time_now+self.BRACKETS[0]+"EVENT"+self.BRACKETS[1])
		for item in tags:
			prefix += self.BRACKETS[0]+item+self.BRACKETS[1]
		output_text = prefix + text + "\n"
		sys.stdout.write(output_text)
		filename = self.FILENAME[0] + str(self.count) + self.FILENAME[1]
		with open(self.FILEINFO[0]+"\\logs\\"+filename,self.WRITEMODE["mode"],encoding=self.WRITEMODE["encoding"]) as w:
			w.write(output_text)
if __name__ == "__main__":
	print("Please import to other file.")
	input("Press Enter to Exit...")
