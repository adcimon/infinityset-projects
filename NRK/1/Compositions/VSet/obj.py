# -*- coding: utf-8 -*-
itemnew("obj", "/",
	"OBJ_TYPE", "Group",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': False, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_PRESENTER_PROD_IN", "TimelineIn",
	"OBJ_PRESENTER_PROD_OUT", "TimelineOut",
	"OBJ_PRESENTER_PROD_RUN_DESCEND", False,
	"OBJ_PRESENTER_FOLDER", "Journalist",
	"OBJ_CONFINE_BOX_MIN", (-8.88889, 0, -5),
	"OBJ_CONFINE_BOX_MAX", (8.88889, 0, 5),
	"OBJ_CAM_IDS", [\
13],
	"OBJ_CAM_ID_MODE", "Unselect",
	"OBJ_TRANSPARENCY_CULLS", True,
	"OBJ_EXTRA_REFS", ['VSet[VSet1]'])

itemnew("obj", "/Reflection",
	"OBJ_TYPE", "Group",
	"OBJ_REFTYPE", "DeleteMe",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': False, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_REFLECTOR_BYPASS", True,
	"OBJ_CLIPX1", "VSet1Reflection",
	"OBJ_CLICKABLE", False,
	"OBJ_CAM_IDS", [\
14],
	"OBJ_CAM_ID_MODE", "Select",
	"OBJ_SCALE", (1, 1, -1),
	"OBJ_ALPHA_MODE", "AlphaClear")

itemnew("obj", "/Reflection/Set",
	"OBJ_TYPE", "Clone",
	"OBJ_REFTYPE", "DeleteMe",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': False, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_CLONE", "/Set")

itemnew("obj", "/Set",
	"OBJ_TYPE", "Group",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': False, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_CLIPX1", "VSet1ClipZUp",
	"OBJ_CAM_IDS", [\
15],
	"OBJ_CAM_ID_MODE", "Unselect",
	"OBJ_CLIP_ON", False)

itemnew("obj", "/Set/SCENE",
	"OBJ_TYPE", "Group",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_PRESENTER_LOAD_APPLY_SELECTED", True,
	"OBJ_PRESENTER_SELECT_TAKES", "Forced",
	"OBJ_PRESENTER_INSTANCE_ENABLED", False,
	"OBJ_CLICK_SELECTABLE", False,
	"OBJ_CAM_IDS", [\
12],
	"OBJ_CAM_ID_MODE", "Unselect",
	"OBJ_TRANSPARENCY_CULLS", True,
	"OBJ_CAST_SHADOW_MODE", "Off",
	"OBJ_GROUP_TYPE", "Presenter",
	"OBJ_LOAD_MATCHES_SINGLE", True)

itemnew("obj", "/Set/RENDERMASK",
	"OBJ_TYPE", "Group",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_OVERMAT", "RenderMask",
	"OBJ_PRESENTER_LOAD_APPLY_SELECTED", True,
	"OBJ_PRESENTER_SELECT_TAKES", "Forced",
	"OBJ_PRESENTER_INSTANCE_ENABLED", False,
	"OBJ_CLICKABLE", False,
	"OBJ_CAM_IDS", [\
12],
	"OBJ_TRANSPARENCY_ON", True,
	"OBJ_TRANSPARENCY_CULLS", True,
	"OBJ_CULL", True,
	"OBJ_CAST_SHADOW_MODE", "Off",
	"OBJ_ALPHA_MODE", "AlphaGhost",
	"OBJ_LOAD_MATCHES_SINGLE", True)

itemnew("obj", "/Set/FLOOR",
	"OBJ_TYPE", "Group",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_PRESENTER_LOAD_APPLY_SELECTED", True,
	"OBJ_PRESENTER_SELECT_TAKES", "Forced",
	"OBJ_PRESENTER_INSTANCE_ENABLED", False,
	"OBJ_CAM_IDS", [\
12],
	"OBJ_CAM_ID_MODE", "Unselect",
	"OBJ_TRANSPARENCY_ON", True,
	"OBJ_TRANSPARENCY_CULLS", True,
	"OBJ_CAST_SHADOW_MODE", "Off",
	"OBJ_GROUP_TYPE", "Presenter",
	"OBJ_ALPHA_MODE", "AlphaClear",
	"OBJ_LOAD_MATCHES_SINGLE", True)

itemnew("obj", "/Set/CEILING",
	"OBJ_TYPE", "Group",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_PRESENTER_LOAD_APPLY_SELECTED", True,
	"OBJ_PRESENTER_SELECT_TAKES", "Forced",
	"OBJ_PRESENTER_INSTANCE_ENABLED", False,
	"OBJ_CAM_IDS", [\
12],
	"OBJ_CAM_ID_MODE", "Unselect",
	"OBJ_TRANSPARENCY_ON", True,
	"OBJ_TRANSPARENCY_CULLS", True,
	"OBJ_CAST_SHADOW_MODE", "Off",
	"OBJ_GROUP_TYPE", "Presenter",
	"OBJ_ALPHA_MODE", "AlphaClear",
	"OBJ_LOAD_MATCHES_SINGLE", True)

itemnew("obj", "/Set/ShadowFloor",
	"OBJ_TYPE", "Primitive",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': False, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_SCA_NEG_CULL", True,
	"OBJ_PRIM", "Set/ShadowFloor",
	"OBJ_CLICKABLE", False,
	"OBJ_CAM_IDS", [\
17],
	"OBJ_CAM_ID_MODE", "Select",
	"OBJ_DISPLACEMENT", (0, 0, 0.04),
	"OBJ_RECEIVE_SHADOW_MODE", "AllLights",
	"OBJ_CAST_SHADOW_MODE", "Off")

itemnew("obj", "/Set/LAYER",
	"OBJ_TYPE", "Group",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': False, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_PRESENTER_SELECTED", 0,
	"OBJ_PRESENTER_LOAD_APPLY_SELECTED", True,
	"OBJ_PRESENTER_SELECT_TAKES", "Forced",
	"OBJ_PRESENTER_INSTANCE_ENABLED", False,
	"OBJ_CAM_IDS", [\
12],
	"OBJ_TRANSPARENCY_CULLS", True)

itemnew("obj", "/Set/LAYER/STAND",
	"OBJ_TYPE", "Group",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_PRESENTER_LOAD_APPLY_SELECTED", True,
	"OBJ_PRESENTER_SELECT_TAKES", "Forced",
	"OBJ_PRESENTER_INSTANCE_ENABLED", False,
	"OBJ_CAM_IDS", [\
12],
	"OBJ_TRANSPARENCY_ON", True,
	"OBJ_TRANSPARENCY_CULLS", True)

itemnew("obj", "/Set/LAYER/DISPLAY",
	"OBJ_TYPE", "Group",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_PRESENTER_LOAD_APPLY_SELECTED", True,
	"OBJ_PRESENTER_SELECT_TAKES", "Forced",
	"OBJ_PRESENTER_INSTANCE_ENABLED", False,
	"OBJ_CAM_IDS", [\
12],
	"OBJ_TRANSPARENCY_CULLS", True)

itemnew("obj", "/Set/LAYER/METRIC",
	"OBJ_TYPE", "Group",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_PRESENTER_LOAD_APPLY_SELECTED", True,
	"OBJ_PRESENTER_SELECT_TAKES", "Forced",
	"OBJ_PRESENTER_INSTANCE_ENABLED", False,
	"OBJ_CAM_IDS", [\
12],
	"OBJ_TRANSPARENCY_ON", True,
	"OBJ_TRANSPARENCY_CULLS", True)

itemnew("obj", "/Set/LAYER/ATMOSPHERE",
	"OBJ_TYPE", "Group",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_PRESENTER_LOAD_APPLY_SELECTED", True,
	"OBJ_PRESENTER_SELECT_TAKES", "Forced",
	"OBJ_PRESENTER_INSTANCE_ENABLED", False,
	"OBJ_CAM_IDS", [\
12],
	"OBJ_TRANSPARENCY_ON", True,
	"OBJ_TRANSPARENCY_CULLS", True)

itemnew("obj", "/Set/LAYER/Actor0",
	"OBJ_TYPE", "Clone",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': False, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_CLONE", "<>VSet/Actor0",
	"OBJ_CLICKABLE", False,
	"OBJ_CLICK_SELECTABLE", False,
	"OBJ_MAT_COORD_SYS_FEET_DIST", 7,
	"OBJ_MAT_COORD_SYS_FEET_VERTICAL", True,
	"OBJ_MAT_COORD_SYS_FEET_MASK", True,
	"OBJ_MAT_COORD_SYS_EYE_SCALE", True,
	"OBJ_MAT_EYE_CAMERA", "<>siteActor/track1",
	"OBJ_CAM_IDS", [\
0],
	"OBJ_CAM_ID_MODE", "Select",
	"OBJ_DISPLACEMENT", (-2, -1, 0),
	"OBJ_REF_POS", (-2, -1, 0),
	"OBJ_BILLBOARD", "axial",
	"OBJ_BBOARD_KEEP", 20,
	"OBJ_BBOARD_REACH", 0.4)

itemnew("obj", "/Set/LAYER/Actor1",
	"OBJ_TYPE", "Clone",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': False, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_CLONE", "<>VSet/Actor1",
	"OBJ_CLICKABLE", False,
	"OBJ_CLICK_SELECTABLE", False,
	"OBJ_MAT_COORD_SYS_FEET_DIST", 7,
	"OBJ_MAT_COORD_SYS_FEET_VERTICAL", True,
	"OBJ_MAT_COORD_SYS_FEET_MASK", True,
	"OBJ_MAT_COORD_SYS_EYE_SCALE", True,
	"OBJ_MAT_EYE_CAMERA", "<>siteActor/track2",
	"OBJ_CAM_IDS", [\
1],
	"OBJ_CAM_ID_MODE", "Select",
	"OBJ_DISPLACEMENT", (2, -1, 0),
	"OBJ_REF_POS", (2, -1, 0),
	"OBJ_BILLBOARD", "axial",
	"OBJ_BBOARD_KEEP", 20,
	"OBJ_BBOARD_REACH", 0.4)

itemnew("obj", "/ASTON",
	"OBJ_TYPE", "Group",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_PRESENTER_LOAD_APPLY_SELECTED", True,
	"OBJ_PRESENTER_SELECT_TAKES", "Forced",
	"OBJ_PRESENTER_INSTANCE_ENABLED", False,
	"OBJ_CAM_IDS", [\
16],
	"OBJ_CAM_ID_MODE", "Unselect",
	"OBJ_TRANSPARENCY_CULLS", True,
	"OBJ_LOAD_MATCHES_SINGLE", True)

itemnew("obj", "/INPUTCATCH",
	"OBJ_TYPE", "Group",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_PRESENTER_LOAD_APPLY_SELECTED", True,
	"OBJ_PRESENTER_SELECT_TAKES", "Forced",
	"OBJ_PRESENTER_INSTANCE_ENABLED", False,
	"OBJ_CLICKABLE", False,
	"OBJ_CAM_IDS", [\
12],
	"OBJ_TRANSPARENCY_ON", True,
	"OBJ_TRANSPARENCY_CULLS", True,
	"OBJ_CAST_SHADOW_MODE", "Off",
	"OBJ_LOAD_MATCHES_SINGLE", True)

itemnew("obj", "/DRAWING",
	"OBJ_TYPE", "Group",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': True, 'Show': True, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_PRESENTER_LOAD_APPLY_SELECTED", True,
	"OBJ_PRESENTER_SELECT_TAKES", "Forced",
	"OBJ_PRESENTER_INSTANCE_ENABLED", False,
	"OBJ_CAM_IDS", [\
12],
	"OBJ_TRANSPARENCY_ON", True,
	"OBJ_TRANSPARENCY_CULLS", True,
	"OBJ_LOAD_MATCHES_SINGLE", True)

