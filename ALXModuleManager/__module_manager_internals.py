import importlib
import os
import re
from contextlib import redirect_stdout
from inspect import getmembers, isclass
from pathlib import Path

import bpy


class ModuleManager:
    module_path: str
    bl_info: dict
    mute: bool

    folder_blacklist: set[str] = {"__pycache__"}
    file_blacklist: set[str] = {"__init__"}

    __module_folders: set[Path]
    __module_files: dict[str, Path]
    __module_classes: set[
        bpy.types.Panel
        | bpy.types.UIList
        | bpy.types.Menu
        | bpy.types.Header
        | bpy.types.Operator
        | bpy.types.KeyingSetInfo
        | bpy.types.RenderEngine
        | bpy.types.AssetShelf
        | bpy.types.FileHandler
        | bpy.types.PropertyGroup
        | bpy.types.AddonPreferences
        | bpy.types.NodeTree
        | bpy.types.Node
        | bpy.types.NodeSocket
        ]

    def register_modules(self):
        addon_name = self.bl_info.get("name")
        print(
            f"----- ALX Module Manager -----\nRegistering {addon_name if addon_name is not None else "Generic Addon"} Modules"
        )

        self.__module_folders = self.gather_addon_folders(
            path=self.module_path, folder_blacklist=self.folder_blacklist
        )
        self.__module_files = self.gather_addon_files(
            folder_paths=self.__module_folders, file_blacklist=self.file_blacklist
        )

        self.import_files_to_global(
            _module_path=self.module_path,
            _mute=self.mute,
            _module_files=self.__module_files,
            _file_blacklist=self.file_blacklist,
        )

        self.execute_locals_update(
            _module_path=self.module_path,
            _mute=self.mute,
            _addon_files=self.__module_files,
            _file_blacklist=self.file_blacklist,
        )

        self.__module_classes = self.gather_classes_from_files(
            self.module_path, self.mute, self.__module_files, self.file_blacklist
        )
        self.__register_addon_classes(self.__module_classes)

    def unregister_modules(self):
        self.__unregister_addon_classes(self.__module_classes)

    def __register_addon_classes(
            self,
            addon_classes: set[
                bpy.types.Panel
                | bpy.types.UIList
                | bpy.types.Menu
                | bpy.types.Header
                | bpy.types.Operator
                | bpy.types.KeyingSetInfo
                | bpy.types.RenderEngine
                | bpy.types.AssetShelf
                | bpy.types.FileHandler
                | bpy.types.PropertyGroup
                | bpy.types.AddonPreferences
                | bpy.types.NodeTree
                | bpy.types.Node
                | bpy.types.NodeSocket
                ],
    ):
        for addon_class in addon_classes:
            try:
                if self.mute:
                    with open(os.devnull, "w") as print_discard_bin:
                        with redirect_stdout(print_discard_bin):
                            if "WorkSpaceTool" in [
                                base.__name__
                                for base in getattr(addon_class, "__bases__")
                            ]:
                                addon_class: type[bpy.types.WorkSpaceTool]
                                bpy.utils.register_tool(
                                    addon_class,
                                    after=getattr(addon_class, "after", None),
                                    separator=getattr(addon_class, "separator", False),
                                    group=getattr(addon_class, "group", False),
                                )
                            else:
                                addon_class: type[
                                    bpy.types.Panel
                                    | bpy.types.UIList
                                    | bpy.types.Menu
                                    | bpy.types.Header
                                    | bpy.types.Operator
                                    | bpy.types.KeyingSetInfo
                                    | bpy.types.RenderEngine
                                    | bpy.types.AssetShelf
                                    | bpy.types.FileHandler
                                    | bpy.types.PropertyGroup
                                    | bpy.types.AddonPreferences
                                    | bpy.types.NodeTree
                                    | bpy.types.Node
                                    | bpy.types.NodeSocket
                                    ]
                                bpy.utils.register_class(addon_class)
                else:
                    if "WorkSpaceTool" in [
                        base.__name__ for base in getattr(addon_class, "__bases__")
                    ]:
                        addon_class: type[bpy.types.WorkSpaceTool]

                        bpy.utils.register_tool(
                            addon_class,
                            after=getattr(addon_class, "after", None),
                            separator=getattr(addon_class, "separator", False),
                            group=getattr(addon_class, "group", False),
                        )
                    else:
                        addon_class: type[
                            bpy.types.Panel
                            | bpy.types.UIList
                            | bpy.types.Menu
                            | bpy.types.Header
                            | bpy.types.Operator
                            | bpy.types.KeyingSetInfo
                            | bpy.types.RenderEngine
                            | bpy.types.AssetShelf
                            | bpy.types.FileHandler
                            | bpy.types.PropertyGroup
                            | bpy.types.AddonPreferences
                            | bpy.types.NodeTree
                            | bpy.types.Node
                            | bpy.types.NodeSocket
                            ]
                        bpy.utils.register_class(addon_class)

            except Exception as error:
                if not self.mute:
                    print(error)

    def __unregister_addon_classes(self, addon_classes: set):
        for addon_class in addon_classes:
            try:
                if "WorkSpaceTool" in [base.__name__ for base in addon_class.__bases__]:
                    bpy.utils.unregister_tool(addon_class)
                else:
                    bpy.utils.unregister_class(addon_class)

            except Exception as error:
                if not self.mute:
                    print(error)

    @staticmethod
    def gather_addon_folders(path: str, folder_blacklist: set[str]):
        """
        IN path: __path__[0] from __init__ \n
        IN folder_blacklist: set[str] \n

        RETURN addon_folders: set[Path] \n
        """

        path_object: Path = Path(path[0])
        addon_folders: set[Path] = set()

        if (path_object.exists()) and (path_object.is_dir()):
            path_iter_queue: list[Path] = [path_object]

            for folder_path in path_iter_queue:
                if (
                        (folder_path.is_dir())
                        and (folder_path.exists())
                        and (folder_path not in addon_folders)
                        and (folder_path.name not in folder_blacklist)
                ):
                    addon_folders.add(folder_path)

                    for subfolder_path in folder_path.iterdir():
                        if (
                                (subfolder_path.is_dir())
                                and (subfolder_path.exists())
                                and (subfolder_path not in addon_folders)
                                and (subfolder_path.name not in folder_blacklist)
                        ):
                            path_iter_queue.append(subfolder_path)
                            addon_folders.add(subfolder_path)

        return addon_folders

    @staticmethod
    def gather_addon_files(folder_paths: set[Path], file_blacklist: set[str]):
        """
        IN folder_paths: set[Path] \n
        IN file_blacklist: set[str] \n

        RETURN addon_files: set[str] \n
        """

        addon_files: dict[str, Path] = dict()

        for folder_path in folder_paths:
            for file in folder_path.iterdir():
                if (
                        (file.is_file())
                        and (file.name not in file_blacklist)
                        and (file.suffix == ".py")
                ):
                    addon_files.update({file.name[0:-3]: folder_path})

        return addon_files

    @staticmethod
    def gather_classes_from_files(
            _module_path: str,
            _mute: bool,
            _module_files: dict[str, Path],
            _file_blacklist: set[str],
    ) -> set[
        bpy.types.Panel
        | bpy.types.UIList
        | bpy.types.Menu
        | bpy.types.Header
        | bpy.types.Operator
        | bpy.types.KeyingSetInfo
        | bpy.types.RenderEngine
        | bpy.types.AssetShelf
        | bpy.types.FileHandler
        | bpy.types.PropertyGroup
        | bpy.types.AddonPreferences
        | bpy.types.NodeTree
        | bpy.types.Node
        | bpy.types.NodeSocket
        ]:

        addon_classes: set[
            bpy.types.Panel
            | bpy.types.UIList
            | bpy.types.Menu
            | bpy.types.Header
            | bpy.types.Operator
            | bpy.types.KeyingSetInfo
            | bpy.types.RenderEngine
            | bpy.types.AssetShelf
            | bpy.types.FileHandler
            | bpy.types.PropertyGroup
            | bpy.types.AddonPreferences
            | bpy.types.NodeTree
            | bpy.types.Node
            | bpy.types.NodeSocket
            ] = set()

        if _module_files is not None:
            _module_path = Path(_module_path[0])

            addon_classes = set()

            for file_name in _module_files.keys():
                if file_name not in _file_blacklist:
                    for addon_class in getmembers(
                            globals().get(file_name),
                            isclass,
                    ):
                        addon_classes.add(addon_class[1])

            if not _mute:
                for print_class in sorted(addon_classes, key=lambda cls: cls.__name__):
                    print(print_class)

        return addon_classes

    @staticmethod
    def import_files_to_global(
            _module_path: str,
            _mute: bool,
            _module_files: dict[str, Path],
            _file_blacklist: set[str],
    ):
        __globals = globals()
        _module_path = _module_path[0]
        _module_path_object = Path(_module_path)

        for _file_name, _file_path in _module_files.items():
            if _file_name not in _file_blacklist:
                _relative_folder = _file_path.relative_to(_module_path, walk_up=False)

                _module_name = f"ALXOverHaul{'.' if str(_relative_folder) in {'', '.'} else f'.{_relative_folder}.'}{_file_name}"

                __globals[_file_name] = importlib.import_module(
                    _module_name,
                )

    @staticmethod
    def execute_locals_update(
            _module_path: str,
            _mute: bool,
            _addon_files: dict[str, Path],
            _file_blacklist: set[str],
    ):

        __globals = globals()
        _module_path = Path(_module_path[0])
        for file_name in _addon_files.keys():
            if (file_name != __name__.split(".")[-1]) and (
                    file_name not in _file_blacklist
            ):

                try:
                    file = _addon_files.get(file_name)
                    if file is not None:
                        _module_name = f"{_module_path.name}.{file.relative_to(_module_path, walk_up=False)}.{file_name}"

                        __globals[_module_name] = (
                            importlib.reload(__globals[_module_name])
                            if file_name in __globals
                            else importlib.import_module(
                                re.sub(
                                    pattern=r"[\/\\]+",
                                    repl=".",
                                    string=_module_name,
                                )
                            )
                        )

                except Exception as _error:
                    if not _mute:
                        print(f"[{file_name}] {_error}")

    # def developer_load_resources(self, icons_definitions: list[dict[str]]):
    #     """
    #     name : str [MUST BE UNIQUE]\n
    #     path : str\n [MUST BE RELATIVE TO THE FOLDER CONTAINING THE ADDON'S INIT FILE]
    #     resource_type : str ['IMAGE', 'MOVIE', 'BLEND', 'FONT']\n
    #     :icons_definitions: "name":str, "path":str, "resource_type":str
    #     """
    #     if self.__resources is None:
    #         self.__resources = previews.new()
    #
    #     name_id_pairs = {}
    #     for entry in icons_definitions:
    #
    #         if {"name", "path", "resource_type"}.issubset(set(entry.keys())):
    #             path_object = Path(
    #                 f"{self.module_path}{os.sep if self.module_path[-1] != os.sep else ''}{entry['path']}"
    #             )
    #             if (path_object.exists()) and (path_object.is_file()):
    #                 self.__resources.load(
    #                     entry["name"], str(path_object), entry["resource_type"], True
    #                 )
    #
    #             name_id_pairs.update(
    #                 {entry["name"]: self.__resources[entry["name"]].icon_id}
    #             )
    #
    #     icons_path_object = Path(f"{self.module_path}\\icons.py")
    #
    #     icons_path_object.parent.mkdir(exist_ok=True, parents=True)
    #     with icons_path_object.open("w") as icon_file:
    #         text = "icons_dictionary={\n"
    #
    #         for string in [
    #             *[
    #                 f'"{entry_name}" : {entry_id},\n'
    #                 for entry_name, entry_id in name_id_pairs.items()
    #             ],
    #             "\n}",
    #         ]:
    #             text += string
    #
    #         icon_file.write(text)
