# Copyright (c) 2018 mclt0568 (For more information see LICENCE)

#INITCFGS = configs
#INITSTRS = strings

import os

class init:
	"""init the files for configs and logs, create them if exist"""
	def __init__(self,PATH):
		global path
		os.chdir(PATH)
		path = PATH
		self.initlicense()
	def initdirs(self):
		"""create the path of configs and logs if they not exist"""
		global path
		if not os.path.exists(path+"\\configs"):
			os.mkdir(path+"\\configs")
		if not os.path.exists(path+"\\logs"):
			os.mkdir(path+"\\logs")
	def initconfig(self):
		"""init read and return as {} the config at path\\configs\\config"""
		global path,INITCFG
		INITCFG = {}
		raw_configs= {"banlist":"banlist.cfg","sudoers":"sudoers.cfg","afklist":"afklist.cfg","afksplit":"","string":"string.cfg","stringsplit":"","logcount":"logcount.cfg","init_dev_mode":"false","init_state_call":"false","init_state_sudo":"false","init_playing_string":""}
		try:
			with open(path+"\\configs\\configs.cfg","r",encoding="utf8") as a:
				data = a.read().split('\n')
				for item in data:
					if item.isspace():
						pass
					elif item.find(": ")==-1:
						pass
					else:
						spliteditem = item.split(": ")
						INITCFG[spliteditem[0]] = spliteditem[1]
			return INITCFG
		except FileNotFoundError:
			with open(path+"\\configs\\configs.cfg","w+",encoding="utf8") as a:
				a.write("banlist: banlist.cfg2\nsudoers: sudoers.cfg\nafklist: afklist.cfg\nafksplit: \nstring: string.cfg\nstringsplit: \nlogcount: logcount.cfg\ninit_dev_mode: false\ninit_state_call: false\ninit_state_sudo: false\ninit_playing_string: ")
			return raw_configs
		#except Exception as e:
		#	print("Error on writting file 'Config.cfg',",str(e))
		#	print(e.__traceback__.tb_frame.f_code.co_consts[0],"at file",e.__traceback__.tb_frame.f_code.co_filename)
		#	print("returning raw configs")
		#	return raw_configs
	def initstrs(self,file_name=None,break_char=None):	
		"""init and return the strings(path from config.cfg, default at //configs//string.cfg) that might needed by the bot"""
		global INITCFG,INITSTRS,break_for_strings
		raw_strings={
			"MESSAGE_CALLING":["剛剛有人叫我嗎？","是在叫我嗎？","我聽到了有人在叫我.w."],
			"MESSAGE_NOTCALLING":["已經取消喚醒了！"],
			"MESSAGE_BYE":["Bye","拜拜~","再見"],
			"MESSAGE_COUNTDOWN":["計時開始","倒計時開始"],
			"MESSAGE_DONE_COUNTDOWN":["時間到","嗶嗶嗶嗶~"],
			"MESSAGE_DONTUNDERSTAND":["看不懂","什麼鬼","我覺得不行"],
			"MESSAGE_HEATS":["1","這隻竹鼠好像中暑了，這樣下去不行，不如我們...","我勸你善良","不如我們..."],
		}
		if not ("INITCFG" in globals()):
			path_for_strings = "string.cfg"
		elif "string" in INITCFG:
			path_for_strings = INITCFG["string"]
		else:
			path_for_strings = "string.cfg"
		if not ("INITCFG" in globals()):
			break_for_strings = ""
		elif "string" in INITCFG:
			break_for_strings = INITCFG["stringsplit"]
		else:
			break_for_strings = ""
		if file_name != None:
			path_for_strings = file_name
		if break_char != None:
			break_for_strings = break_char
		try:
			INITSTRS = {}
			with open(path+"\\configs\\"+path_for_strings,"r",encoding="utf8") as a:
				data = a.read().split('\n')
				for item in data:
					if item.isspace():
						pass
					elif item.find(break_for_strings)==-1:
						pass
					else:
						spliteditem = item.split(break_for_strings)
						INITSTRS[spliteditem[0]] = []
						index = 1
						for item in spliteditem:
							if index == 1:
								index += 1
							else:
								INITSTRS[spliteditem[0]].append(item)
			return INITSTRS
		except FileNotFoundError:
			with open(path+"\\configs\\"+path_for_strings,"w+",encoding="utf8") as a:
				a.write("MESSAGE_CALLING剛剛有人叫我嗎？是在叫我嗎？我聽到了有人在叫我.w.\nMESSAGE_NOTCALLING已經取消喚醒了！\nMESSAGE_BYEBye拜拜~再見\nMESSAGE_COUNTDOWN計時開始倒計時開始\nMESSAGE_DONE_COUNTDOWN時間到嗶嗶嗶嗶~\nMESSAGE_DONTUNDERSTAND看不懂什麼鬼我覺得不行\nMESSAGE_HEATS1這隻竹鼠好像中暑了，這樣下去不行，不如我們...我勸你善良不如我們...")
			return raw_strings
		#except Exception as e:
		#	print("Error on writting file 'Config.cfg',",str(e))
		#	print(e.__traceback__.tb_frame.f_code.co_consts[0],"at file",e.__traceback__.tb_frame.f_code.co_filename)
		#	print("returning raw configs")
		#	return raw_configs
	def initlicense(self):
		"""check if license is exist"""
		global path
		license_content = '/nMIT License/n/nCopyright (c) 2018 mclt0568/n/nPermission is hereby granted, free of charge, to any person obtaining a copy/nof this software and associated documentation files (the "Software"), to deal/nin the Software without restriction, including without limitation the rights/nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell/ncopies of the Software, and to permit persons to whom the Software is/nfurnished to do so, subject to the following conditions:/n/nThe above copyright notice and this permission notice shall be included in all/ncopies or substantial portions of the Software./n/nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR/nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,/nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE/nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER/nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,/nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE/nSOFTWARE.'
		Licence_exist = not (os.path.isfile(path+"\\LICENSE"))
		if Licence_exist:
			with open(path+"\\LICENSE","w+") as w:
				w.write(license_content)
			print("Please Read the 'LICENSE' before using")
		else:
			with open(path+"\\LICENSE","r",encoding="utf8") as w:
				data = w.read()
			if data != license_content:
				print("Please DO NOT CHANGE the 'LICENSE' file.")
				with open(path+"\\LICENSE","w+") as w:
					w.write(license_content)
			print("Please Read the 'LICENSE' before using")

if __name__ == "__main__":
	print("Please import to other file.")
	input("Press Enter to Exit...")