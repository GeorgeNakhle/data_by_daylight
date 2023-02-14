from imports import *
from build.metadata import *
from build.survivor import *
from build.killer import *

clearFolder("./source_data/")
createMetadataCSV()
createSurvivorCSV()
createKillerCSV()


###########################################################################################################
# Source: https://github.com/gatheringhallstudios/MHWorldData
# DB Model: https://lucid.app/lucidchart/9bb20e80-bc4d-4554-b7de-69b98f221707/edit?view_items=vfXvHWz-LJRf&invitationId=inv_6be87b84-7a83-4069-a5f2-9a2da022a2b1
#
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# Use https://dbd.tricky.lol/api for everything that you can
# Default images: https://packs.dbdicontoolbox.com/Dead-By-Daylight-Default-Icons.zip
#
# XAMPP -> MySQL Workbench
###########################################################################################################