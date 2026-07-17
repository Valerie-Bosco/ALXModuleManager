from pathlib import Path

from ALXModuleManager.__module_manager_internals import ModuleManager

TEST_MODULE_PATH = "E://GitHub//BlenderAddons//addons//ALXOverHaul"
TEST_ADDON_FILES = {
    "AlxOperators": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/Trash"),
    "AlxUnlockedModeling": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/UnlockedTools"
    ),
    "AlxUnlockedObjectModes": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/UnlockedTools"
    ),
    "ALX_keymaps": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul"),
    "ALX_preferences": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul"),
    "__init__": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul"),
    "ALX_Info_System": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/info_system"),
    "ALX_Info_UI": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/info_system"),
    "armature": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/mode"),
    "ALX_Armature_Conversion": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/armature_tools"
    ),
    "ALX_Armature_Merging": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/armature_tools"
    ),
    "Alx_rigging_tools": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/armature_tools"
    ),
    "unity_tools": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/armature_tools"),
    "AlxModifierOperators": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/MeshTools"
    ),
    "AlxVertexGroupTools": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/MeshTools"),
    "ALX_Normals_Tools": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/MeshTools"),
    "ALX_shapekey": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/MeshTools"),
    "ALX_ShapeKey_Generator": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/MeshTools"
    ),
    "shapekey": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/mesh"),
    "AlxConstantsDefinition": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/definitions"
    ),
    "AlxTypesDefinition": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/definitions"
    ),
    "modifiers": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/definitions"),
    "unity_definitions": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/definitions"),
    "Alx_pose_tools": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/pose_tools"),
    "AlxVMCConnection": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/VMC"),
    "Alx_weightpaint_bucket_fill": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/weight_paint_tools"
    ),
    "AlxAlexandriaNPanel": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/interface"),
    "ALX_Alexandria_General_Panel": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/interface"
    ),
    "ALX_Alexandria_Layouts": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/interface"
    ),
    "ALX_Alexandria_Selection_Pie": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/interface"
    ),
    "ALX_Shapeky_Toolset": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/interface"),
    "AlxUtilities": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/utilities"),
    "Alx_armature_utils": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/utilities"),
    "ALX_BMesh_Utils": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/utilities"),
    "ALX_Bone_Utils": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/utilities"),
    "ALX_Math_Utils": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/utilities"),
    "unity_utilities": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/utilities"),
    "Alx_OT_UI_SimpleDesigner": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/UITools"
    ),
    "AlxCallbacks": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/reorganize_later"),
    "AlxCullingShader": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/reorganize_later"
    ),
    "AlxGpuUI": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/reorganize_later"),
    "AlxJson": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/reorganize_later"),
    "AlxObjectOperator": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/reorganize_later"
    ),
    "AlxParticleTools": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/reorganize_later"
    ),
    "AlxProperties": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/reorganize_later"
    ),
    "AlxRemesher": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/reorganize_later"),
    "AlxSculptTools": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/reorganize_later"
    ),
    "AlxStanfordBatchExporter": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/reorganize_later"
    ),
    "AlxUVRetopology": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/reorganize_later"
    ),
    "AlxVisibilityOperators": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/reorganize_later"
    ),
    "ALX_Handlers": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/reorganize_later"),
    "Alx_keymaps": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/reorganize_later"),
    "Alx_STAL_GPU_utils": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/reorganize_later"
    ),
    "AlxSculptWrap": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/SculptTools"),
    "ALXFusionTextures": Path(
        "E:/GitHub/BlenderAddons/addons/ALXOverHaul/texture_tools"
    ),
    "AlxUDIMTools": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/UVTools"),
    "AlxUVSnapping": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/UVTools"),
    "AlxUVTransfer": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/UVTools"),
    "ALX_Gridify_UV": Path("E:/GitHub/BlenderAddons/addons/ALXOverHaul/UVTools"),
}


def TEST__gather_classes_from_files():
    ModuleManager().gather_classes_from_files(
        _module_path=TEST_MODULE_PATH,
        _mute=False,
        _module_files=TEST_ADDON_FILES,
        _file_blacklist=set(),
    )


def TEST_import_files_to_global():
    ModuleManager().import_files_to_global(
        _module_path=TEST_MODULE_PATH,
        _mute=False,
        _module_files=TEST_ADDON_FILES,
        _file_blacklist=set(),
    )


def TEST__execute_locals_update():
    ModuleManager().execute_locals_update(
        _module_path=TEST_MODULE_PATH,
        _mute=False,
        _addon_files=TEST_ADDON_FILES,
        _file_blacklist=set(),
    )


if __name__ == "__main__":
    TEST_import_files_to_global()
