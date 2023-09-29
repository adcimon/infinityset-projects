# -*- coding: utf-8 -*-
itemnew("obj", "StormLogic",
	"OBJ_TYPE", "Group",
	"OBJ_PRESENTER_SELECTED", 0,
	"OBJ_PRESENTER_SELECT_TAKES_TRAVERSE", False,
	"OBJ_PRESENTER_FORCED_BRANCH", True,
	"OBJ_GROUP_TYPE", "Presenter")

itemnew("obj", "StormLogic/VSets",
	"OBJ_TYPE", "Group",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': False, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': False, 'Clean': False, 'ShowRef': False, 'Delete': True},
	"OBJ_PRESENTER_SELECTED", 0,
	"OBJ_PRESENTER_INSTANCE_ENABLED", False,
	"OBJ_GROUP_TYPE", "Presenter")

itemnew("obj", "StormLogic/VSets/VSet",
	"OBJ_TYPE", "Scene",
	"OBJ_CAPTIVE", {'Exclusive': False, 'Name': False, 'Show': False, 'Edit': False, 'Crypt': False, 'Share': False, 'Effect': False, 'Single': True, 'Clean': False, 'ShowRef': False, 'Delete': False},
	"OBJ_CLONE_SCENE", "<>NRK/VSet",
	"OBJ_CLONE_INSTANCE_TYPE", "Scene",
	"OBJ_PRESENTER_PROD_IN_ENABLED", False,
	"OBJ_PRESENTER_INSTANCE_ENABLED", False)

itemnew("obj", "StormLogic/WorkArea",
	"OBJ_TYPE", "Group",
	"OBJ_GROUP_TYPE", "Presenter")

