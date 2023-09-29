# -*- coding: utf-8 -*-
itemnew("action", "ActionPrefs",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_SYNC_DATA", True,
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Preferences Version",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Preferences Version]",
	"ACTION_EDITOR", "<>MAP_STRING_PAR",
	"ACTION_DATA/string", '5.0.11',
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Preferences Version", "MAP_STRING_PAR", '5.0.11')""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Auto Edit Near Far",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Auto Edit Near Far]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 0,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Auto Edit Near Far", "MAP_INT_PAR", 0)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Video Format",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Video Format]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 11,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Video Format", "MAP_INT_PAR", 11)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/HDR enable",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/HDR enable]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 0,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/HDR enable", "MAP_INT_PAR", 0)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/HDR color space",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/HDR color space]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 0,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/HDR color space", "MAP_INT_PAR", 0)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Time code",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Time code]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 0,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Time code", "MAP_INT_PAR", 0)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/FPS",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/FPS]",
	"ACTION_EDITOR", "<>MAP_FLOAT_PAR",
	"ACTION_DATA/float", 100,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/FPS", "MAP_FLOAT_PAR", 100)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Size X",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Size X]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 1920,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Size X", "MAP_INT_PAR", 1920)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Size Y",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Size Y]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 1080,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Size Y", "MAP_INT_PAR", 1080)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Focal length",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Focal length]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 4,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Focal length", "MAP_INT_PAR", 4)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Focal length custom",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Focal length custom]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 35,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Focal length custom", "MAP_INT_PAR", 35)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Camera Aspect Ratio",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Camera Aspect Ratio]",
	"ACTION_EDITOR", "<>MAP_FLOAT_PAR",
	"ACTION_DATA/float", 1.77778,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Camera Aspect Ratio", "MAP_FLOAT_PAR", 1.77778)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Camera Aspect Ratio Auto",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Camera Aspect Ratio Auto]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 1,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Camera Aspect Ratio Auto", "MAP_INT_PAR", 1)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Pixel Aspect Ratio",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Pixel Aspect Ratio]",
	"ACTION_EDITOR", "<>MAP_FLOAT_PAR",
	"ACTION_DATA/float", 1,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Pixel Aspect Ratio", "MAP_FLOAT_PAR", 1)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Output Fit",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Output Fit]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 2,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Output Fit", "MAP_INT_PAR", 2)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Edit Stereo",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Edit Stereo]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 0,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Edit Stereo", "MAP_INT_PAR", 0)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Program Stereo",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Program Stereo]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 0,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Program Stereo", "MAP_INT_PAR", 0)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Stereo Parallax",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Stereo Parallax]",
	"ACTION_EDITOR", "<>MAP_FLOAT_PAR",
	"ACTION_DATA/float", 0.1,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Stereo Parallax", "MAP_FLOAT_PAR", 0.1)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Near Clip Plane",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Near Clip Plane]",
	"ACTION_EDITOR", "<>MAP_FLOAT_PAR",
	"ACTION_DATA/float", 0.1,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Near Clip Plane", "MAP_FLOAT_PAR", 0.1)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Far Clip Plane",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Far Clip Plane]",
	"ACTION_EDITOR", "<>MAP_FLOAT_PAR",
	"ACTION_DATA/float", 12000,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Far Clip Plane", "MAP_FLOAT_PAR", 12000)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Default Timeline length",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Default Timeline length]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 5,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Default Timeline length", "MAP_INT_PAR", 5)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Default Timeline linearity",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Default Timeline linearity]",
	"ACTION_EDITOR", "<>MAP_FLOAT_PAR",
	"ACTION_DATA/float", 1,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Default Timeline linearity", "MAP_FLOAT_PAR", 1)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/SetAutoBox",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/SetAutoBox]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 1,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/SetAutoBox", "MAP_INT_PAR", 1)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/ModelAutobox",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/ModelAutobox]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 0,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/ModelAutobox", "MAP_INT_PAR", 0)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Time 24H",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Time 24H]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 1,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Time 24H", "MAP_INT_PAR", 1)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Time Pad Zero",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Time Pad Zero]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 1,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Time Pad Zero", "MAP_INT_PAR", 1)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Preview Render Mode",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Preview Render Mode]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 0,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Preview Render Mode", "MAP_INT_PAR", 0)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/JumpTake Mode",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/JumpTake Mode]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 0,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/JumpTake Mode", "MAP_INT_PAR", 0)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Use Alphanumeric Pages",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Use Alphanumeric Pages]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 0,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Use Alphanumeric Pages", "MAP_INT_PAR", 0)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/PVW Follow Selected",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/PVW Follow Selected]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 0,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/PVW Follow Selected", "MAP_INT_PAR", 0)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/X Drag",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/X Drag]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 1,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/X Drag", "MAP_INT_PAR", 1)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Edit Plane",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Edit Plane]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 1,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Edit Plane", "MAP_INT_PAR", 1)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Edit Size",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Edit Size]",
	"ACTION_EDITOR", "<>MAP_FLOAT_PAR",
	"ACTION_DATA/float", 10,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Edit Size", "MAP_FLOAT_PAR", 10)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Tally enable",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Tally enable]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 0,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Tally enable", "MAP_INT_PAR", 0)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Open and send mode",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Open and send mode]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 0,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Open and send mode", "MAP_INT_PAR", 0)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/IP",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/IP]",
	"ACTION_EDITOR", "<>MAP_STRING_PAR",
	"ACTION_DATA/string", '127.0.0.1',
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/IP", "MAP_STRING_PAR", '127.0.0.1')""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Port",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Port]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 6000,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Port", "MAP_INT_PAR", 6000)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/sharedLight1DefaultPos",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/sharedLight1DefaultPos]",
	"ACTION_EDITOR", "<>MAP_VECTOR_PAR",
	"ACTION_DATA/float3", (7.5, -7.5, 5),
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/sharedLight1DefaultPos", "MAP_VECTOR_PAR", (7.5, -7.5, 5))""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/sharedLight2DefaultPos",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/sharedLight2DefaultPos]",
	"ACTION_EDITOR", "<>MAP_VECTOR_PAR",
	"ACTION_DATA/float3", (-10, -8, 6),
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/sharedLight2DefaultPos", "MAP_VECTOR_PAR", (-10, -8, 6))""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/sharedLight3DefaultPos",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/sharedLight3DefaultPos]",
	"ACTION_EDITOR", "<>MAP_VECTOR_PAR",
	"ACTION_DATA/float3", (0, 4, 5),
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/sharedLight3DefaultPos", "MAP_VECTOR_PAR", (0, 4, 5))""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/EditColor",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/EditColor]",
	"ACTION_EDITOR", "<>MAP_COLOR_PAR",
	"ACTION_DATA/Color4", (0, 0, 0, 0),
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/EditColor", "MAP_COLOR_PAR", (0, 0, 0, 0))""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Presentation Auto Slide Out",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Presentation Auto Slide Out]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 0,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Presentation Auto Slide Out", "MAP_INT_PAR", 0)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Presentation Next Is Step",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Presentation Next Is Step]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 0,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Presentation Next Is Step", "MAP_INT_PAR", 0)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Teleprompter Auto Next",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Teleprompter Auto Next]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 0,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Teleprompter Auto Next", "MAP_INT_PAR", 0)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Teleprompter Auto Next Stay",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Teleprompter Auto Next Stay]",
	"ACTION_EDITOR", "<>MAP_FLOAT_PAR",
	"ACTION_DATA/float", 1,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Teleprompter Auto Next Stay", "MAP_FLOAT_PAR", 1)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Preferences/Teleprompter Auto Next Loop",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "map[<>Preferences/Teleprompter Auto Next Loop]",
	"ACTION_EDITOR", "<>MAP_INT_PAR",
	"ACTION_DATA/integer", 0,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>Preferences/Teleprompter Auto Next Loop", "MAP_INT_PAR", 0)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/ipfmode",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_SYNC_DATA", True,
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/ipfmode/IPFMODE_PALETTE_COLORS",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "modes[<>ipfmode]",
	"ACTION_EDITOR", "<>IPFMODE_PALETTE_COLORS",
	"ACTION_DATA/lfloat", [\
		[1, 1, 1, 1], \
		[0.857143, 0.857143, 0.857143, 1], \
		[0.714286, 0.714286, 0.714286, 1], \
		[0.571429, 0.571429, 0.571429, 1], \
		[0.428571, 0.428571, 0.428571, 1], \
		[0.285714, 0.285714, 0.285714, 1], \
		[0.142857, 0.142857, 0.142857, 1], \
		[0, 0, 0, 1], \
		[0.5, 0, 0, 1], \
		[0.5, 0.375, 0, 1], \
		[0.25, 0.5, 0, 1], \
		[0, 0.5, 0.125, 1], \
		[0, 0.5, 0.5, 1], \
		[0, 0.125, 0.5, 1], \
		[0.25, 0, 0.5, 1], \
		[0.5, 0, 0.375, 1], \
		[1, 0, 0, 1], \
		[1, 0.75, 0, 1], \
		[0.5, 1, 0, 1], \
		[0, 1, 0.25, 1], \
		[0, 1, 1, 1], \
		[0, 0.25, 1, 1], \
		[0.5, 0, 1, 1], \
		[1, 0, 0.75, 1], \
		[1, 0.34, 0.34, 1], \
		[1, 0.835, 0.34, 1], \
		[0.67, 1, 0.34, 1], \
		[0.34, 1, 0.505, 1], \
		[0.34, 1, 1, 1], \
		[0.34, 0.505, 1, 1], \
		[0.67, 0.34, 1, 1], \
		[1, 0.34, 0.835, 1], \
		[1, 0.67, 0.67, 1], \
		[1, 0.9175, 0.67, 1], \
		[0.835, 1, 0.67, 1], \
		[0.67, 1, 0.7525, 1], \
		[0.67, 1, 1, 1], \
		[0.67, 0.7525, 1, 1], \
		[0.835, 0.67, 1, 1], \
		[1, 0.67, 0.9175, 1]],
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>ipfmode", "IPFMODE_PALETTE_COLORS", [[1, 1, 1, 1], [0.857143, 0.857143, 0.857143, 1], [0.714286, 0.714286, 0.714286, 1], [0.571429, 0.571429, 0.571429, 1], [0.428571, 0.428571, 0.428571, 1], [0.285714, 0.285714, 0.285714, 1], [0.142857, 0.142857, 0.142857, 1], [0, 0, 0, 1], [0.5, 0, 0, 1], [0.5, 0.375, 0, 1], [0.25, 0.5, 0, 1], [0, 0.5, 0.125, 1], [0, 0.5, 0.5, 1], [0, 0.125, 0.5, 1], [0.25, 0, 0.5, 1], [0.5, 0, 0.375, 1], [1, 0, 0, 1], [1, 0.75, 0, 1], [0.5, 1, 0, 1], [0, 1, 0.25, 1], [0, 1, 1, 1], [0, 0.25, 1, 1], [0.5, 0, 1, 1], [1, 0, 0.75, 1], [1, 0.34, 0.34, 1], [1, 0.835, 0.34, 1], [0.67, 1, 0.34, 1], [0.34, 1, 0.505, 1], [0.34, 1, 1, 1], [0.34, 0.505, 1, 1], [0.67, 0.34, 1, 1], [1, 0.34, 0.835, 1], [1, 0.67, 0.67, 1], [1, 0.9175, 0.67, 1], [0.835, 1, 0.67, 1], [0.67, 1, 0.7525, 1], [0.67, 1, 1, 1], [0.67, 0.7525, 1, 1], [0.835, 0.67, 1, 1], [1, 0.67, 0.9175, 1]])""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/ipfmode/IPFMODE_PICKSHOWNAMES",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "modes[<>ipfmode]",
	"ACTION_EDITOR", "<>IPFMODE_PICKSHOWNAMES",
	"ACTION_DATA/boolean", False,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>ipfmode", "IPFMODE_PICKSHOWNAMES", False)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/ipfmode/IPFMODE_GRAPHICS_BOX_LINES",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "modes[<>ipfmode]",
	"ACTION_EDITOR", "<>IPFMODE_GRAPHICS_BOX_LINES",
	"ACTION_DATA/boolean", True,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>ipfmode", "IPFMODE_GRAPHICS_BOX_LINES", True)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/ipfmode/IPFMODE_TIMECODE_FPS",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "modes[<>ipfmode]",
	"ACTION_EDITOR", "<>IPFMODE_TIMECODE_FPS",
	"ACTION_DATA/float", 100,
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", """itemset("<>ipfmode", "IPFMODE_TIMECODE_FPS", 100)""",
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Edit",
	"ACTION_SYNC_DATA", True,
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/Edit/PIPE_TELEPROMPTER_FILE",
	"ACTION_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"ACTION_ITEM", "pipe[<>Edit]",
	"ACTION_EDITOR", "<>PIPE_TELEPROMPTER_FILE",
	"ACTION_DATA/File", '.\\..\\..\\_assets\\prompter.txt',
	"ACTION_SYNC_DATA", True,
	"ACTION_CODE", ('itemset("<>Edit", "PIPE_TELEPROMPTER_FILE", \'C:\\\\Users\\\\aciborro\\\\AppData\\\\Roaming\\\\Brainstorm\\\\VSet\\\\tmp\\\\prompter.txt\')'),
	"ACTION_IGNORE_PAUSE", False)

itemnew("action", "ActionPrefs/VSetLocal",
	"ACTION_SYNC_DATA", True,
	"ACTION_IGNORE_PAUSE", False)

