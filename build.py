from imports import *
from build.challenge import *
from build.charm import *
from build.cosmetic import *
from build.dlc import *
from build.entry import *
from build.event import *
from build.item_addon_item import *
from build.item_addon import *
from build.item import *
from build.killer import *
from build.level import *
from build.map import *
from build.metadata import *
from build.offering import *
from build.outfit import *
from build.perk import *
from build.power_addon import *
from build.power import *
from build.rift import *
from build.survivor import *
from build.tome import *
from build.vignette import *
from sql.database import *

#region [1] JSON to CSV files #############################################################################

# clearFolder("./source_data/")
# challenge()
# charm()
# cosmetic()
# dlc()
# entry()
# event()
# item_addon_item()
# item_addon()
# item()
# killer()
# level()
# map()
# metadata()
# offering()
# outfit()
# perk()
# power_addon()
# power()
# rift()
# survivor()
# tome()
# vignette()

#endregion ################################################################################################

#region [2] Create schema and import CSV files ############################################################

database()

#endregion ################################################################################################

#region [3] Create dbd.db #################################################################################

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
# Competitors:  Nightlight.gg (crowd sourced)
#               Randomizer DBD
#               Perks by Daylight
#               Tricky
#
# [1] JSON to CSV files                     [✓]
# [2] Create schema and import CSV files    [ ]
# [4] Create dbd.db                         [ ]
#
###########################################################################################################