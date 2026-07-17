from typing import Optional

import bpy

from .__module_manager_internals import ModuleManager

mm = None


class ALXModuleManager(ModuleManager):

    def __init__(
            self,
            path: str,
            bl_info: dict,
            mute: bool,
            folder_blacklist: Optional[set[str]] = None,
            file_blacklist: Optional[set[str]] = None,
    ):

        super().__init__()
        self.module_path = path
        self.bl_info = bl_info

        if folder_blacklist is not None:
            self.folder_blacklist |= folder_blacklist
        if file_blacklist is not None:
            self.file_blacklist |= file_blacklist

        self.mute = mute

        print(
            f"\n\n\n\n\n----- ALX Module Manager -----\nInitialized for {addon_name if (addon_name := self.bl_info.get("name")) is not None else "Generic Addon"}"
        )

    def register_modules(self):
        super().register_modules()

    def unregister_modules(self):
        super().unregister_modules()


def GET_module_manager() -> ALXModuleManager | None:
    if mm is None:
        print("ALX Module Manager not initialized")
    return mm


def GET_preferences() -> bpy.types.AddonPreferences | None:
    if bpy.context.preferences is not None:
        addon: bpy.types.Addon | list[bpy.types.Addon] = bpy.context.preferences.addons[
            __package__
        ]

        addon: bpy.types.Addon
        if addon is not None and type(addon) == bpy.types.Addon:
            return addon.preferences
    return None


def SET_module_manager(module_manager: ALXModuleManager) -> None:
    global mm
    mm = module_manager
