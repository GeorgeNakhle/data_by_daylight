# Organize alphabetically later
from imports import *
from build.metadata import *
from build.survivor import *
from build.killer import *
from build.perk import *
from build.dlc import *
from build.offering import *
from build.map import *
from build.power import *
from build.power_addon import *
from build.event import *
from build.item import *
from build.item_addon import *
from build.item_addon_type import *
from build.tome import *
from build.challenge import *
from build.vignette import *
from build.entry import *
from build.rift import *
from build.level import *
from build.charm import *
from build.outfit import *

#region [1] #### JSON to CSV files ########################################################################

clearFolder("./source_data/")
# metadata()
# survivor()
# killer()
# perk()
# dlc()
# offering()
# map()
# power()
# power_addon()
# event()
# item()
# item_addon()
# item_addon_type()
# tome()
# challenge()
# vignette()
# entry()
# rift()
# level()
# charm()
outfit()

#endregion ################################################################################################

#region [2] #### Create schema ############################################################################

# something lol

#endregion ################################################################################################

#region [3] #### Import CSV files into schema #############################################################

# something lol

#endregion ################################################################################################

#region [4] #### Create dbd.db ############################################################################

# something lol

#endregion ################################################################################################


###########################################################################################################
#
# Source: https://github.com/gatheringhallstudios/MHWorldData
# DB Model: https://lucid.app/lucidchart/9bb20e80-bc4d-4554-b7de-69b98f221707/edit?view_items=vfXvHWz-LJRf&invitationId=inv_6be87b84-7a83-4069-a5f2-9a2da022a2b1
#
# Use https://dbd.tricky.lol/api for everything that you can!
# Default images: https://packs.dbdicontoolbox.com/Dead-By-Daylight-Default-Icons.zip
#
# XAMPP -> MySQL Workbench
# Put a try/catch somewhere
# Make table for status effects (icons in ./images)
# Make table for codes
# For cosmetic images: https://dbd.tricky.lol/cosmetics
#
# [1] JSON to CSV files
# [2] Create schema
# [3] Import CSV files into schema
# [4] Create dbd.db
#
###########################################################################################################