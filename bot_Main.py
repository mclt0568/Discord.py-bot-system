# Copyright (c) 2018 mclt0568 (For more information see LICENCE)

import bot_config as cfg
import bot_log as log
import bot_check as check

#Init
config = cfg.init(r"C:\Users\USER\Desktop\Python Project\DISCORDBOTS2")
config.initdirs()
INITCFG = config.initconfig()
INITSTR = config.initstrs()
logoption = log.log_option(r"C:\Users\USER\Desktop\Python Project\DISCORDBOTS2")
logs = log.logs(logoption.getfileinfo())
logs.log("Hello world")
