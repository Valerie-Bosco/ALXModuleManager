from typing import Any, Optional

from .__module_manager_internals import ModuleManager


class ALXModuleManager(ModuleManager):

    def __init__(
            self,
            path: str,
            bl_info: dict,
            init_globals: dict[str, Any],
            folder_blacklist: Optional[set[str]] = None,
            file_blacklist: Optional[set[str]] = None,
            mute: bool = True,
    ):

        super().__init__()
        self.module_path = path[0]
        self.bl_info = bl_info
        self.init_globals = init_globals

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
        super().unregister_module()
