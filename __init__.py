import bpy
import math
import os,re
bl_info = {
    "name":"Color_helper",
    "author": "iCyP",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "3DView->UI",
    "description": "simple helper for color scheme",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}




class ICYP_PT_color_helper(bpy.types.Panel):
    bl_idname = "scene.icyp_color_helper"
    bl_label = "Color helper"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Color helper"
    
    @classmethod
    def poll(self, context):
        return True
    def draw(self, context):
        self.layout.label(text="color help")
        self.layout.prop(context.scene,"icyp_COLOR_SCHEME_PROP")
        self.layout.prop(context.scene, "icyp_color_helper_main_color")
        self.layout.prop(context.scene, "icyp_color_helper_sub1_color")
        self.layout.prop(context.scene, "icyp_color_helper_sub2_color")
        self.layout.prop(context.scene, "icyp_color_helper_sub3_color")
        self.layout.prop(context.scene, "icyp_color_helper_sub4_color")

    
# アドオン有効化時の処理
classes = [
    ICYP_PT_color_helper
    ]
    
icyp_color_scheme_type = (
    ("INV","INVERT","補色"),#(value,show_name,explanation)
    ("TRI", "TRIAD", "3分色"),
    ("QUI","QUINARY","5分色"),
    #("C2", "2chroma", ""),
    #("C3", "3chroma", ""),
    #("C4", "4chroma", ""),
    #("C5", "5chroma", "")
)

import colorsys
def change_color(self, context):
    scene = context.scene
    main_color = scene.icyp_color_helper_main_color
    scheme_type = scene.icyp_COLOR_SCHEME_PROP
    hsv_base = colorsys.rgb_to_hsv(*main_color)
    if scheme_type == "INV":
        scene.icyp_color_helper_sub1_color = colorsys.hsv_to_rgb(*[hsv_base[i] + v for i, v in enumerate([0.5, 0, 0])])
        scene.icyp_color_helper_sub2_color = [0, 0, 0]
        scene.icyp_color_helper_sub3_color = [0, 0, 0]
        scene.icyp_color_helper_sub4_color = [0, 0, 0]
        
    elif scheme_type == "TRI":
        scene.icyp_color_helper_sub1_color = colorsys.hsv_to_rgb(*[hsv_base[i] + v for i, v in enumerate([1 / 3, 0, 0])])
        scene.icyp_color_helper_sub2_color = colorsys.hsv_to_rgb(*[hsv_base[i] + v for i, v in enumerate([2 / 3, 0, 0])])
        scene.icyp_color_helper_sub3_color = [0, 0, 0]
        scene.icyp_color_helper_sub4_color = [0, 0, 0]
    elif scheme_type =="QUI":
        scene.icyp_color_helper_sub1_color = colorsys.hsv_to_rgb(*[hsv_base[i] + v for i, v in enumerate([1 / 5, 0, 0])])
        scene.icyp_color_helper_sub2_color = colorsys.hsv_to_rgb(*[hsv_base[i] + v for i, v in enumerate([2 / 5, 0, 0])])
        scene.icyp_color_helper_sub3_color = colorsys.hsv_to_rgb(*[hsv_base[i] + v for i, v in enumerate([3 / 5, 0, 0])])
        scene.icyp_color_helper_sub4_color = colorsys.hsv_to_rgb(*[hsv_base[i] + v for i, v in enumerate([4 / 5, 0, 0])])
    #以下なんか違う
    elif scheme_type =="C2":
        scene.icyp_color_helper_sub1_color = colorsys.hsv_to_rgb(*[hsv_base[i] + v for i, v in enumerate([1,0.5,1])])
        scene.icyp_color_helper_sub2_color = [0, 0, 0]
        scene.icyp_color_helper_sub3_color = [0, 0, 0]
        scene.icyp_color_helper_sub4_color = [0, 0, 0]
    elif scheme_type =="C3":
        scene.icyp_color_helper_sub1_color = colorsys.hsv_to_rgb(*[hsv_base[i] + v for i, v in enumerate([1, 1/3,1])])
        scene.icyp_color_helper_sub2_color = colorsys.hsv_to_rgb(*[hsv_base[i] + v for i, v in enumerate([1, 2/3,1])])
        scene.icyp_color_helper_sub3_color = [0, 0, 0]
        scene.icyp_color_helper_sub4_color = [0, 0, 0]
    elif scheme_type =="C4":
        scene.icyp_color_helper_sub1_color = colorsys.hsv_to_rgb(*[hsv_base[i] + v for i, v in enumerate([1, 1/4,1])])
        scene.icyp_color_helper_sub2_color = colorsys.hsv_to_rgb(*[hsv_base[i] + v for i, v in enumerate([1, 1/2,1])])
        scene.icyp_color_helper_sub3_color = colorsys.hsv_to_rgb(*[hsv_base[i] + v for i, v in enumerate([1, 3/4,1])])
        scene.icyp_color_helper_sub4_color = [0, 0, 0]
    elif scheme_type =="C5":
        scene.icyp_color_helper_sub1_color = colorsys.hsv_to_rgb(*[hsv_base[i] + v for i, v in enumerate([1, 1/5,1])])
        scene.icyp_color_helper_sub2_color = colorsys.hsv_to_rgb(*[hsv_base[i] + v for i, v in enumerate([1, 2/5,1])])
        scene.icyp_color_helper_sub3_color = colorsys.hsv_to_rgb(*[hsv_base[i] + v for i, v in enumerate([1, 3/5,1])])
        scene.icyp_color_helper_sub4_color = colorsys.hsv_to_rgb(*[hsv_base[i] + v for i, v in enumerate([1, 4/5,1])])


def register():
    bpy.types.Scene.icyp_color_helper_main_color = bpy.props.FloatVectorProperty(name="Main color", subtype="COLOR", default=[0.0, 0.0, 0.0], min=0, max=1, update=change_color)
    bpy.types.Scene.icyp_color_helper_sub1_color = bpy.props.FloatVectorProperty(name="Sub1 color", subtype="COLOR", default=[0.0, 0.0, 0.0], min=0, max=1, update=None)
    bpy.types.Scene.icyp_color_helper_sub2_color = bpy.props.FloatVectorProperty(name="Sub2 color", subtype="COLOR", default=[0.0, 0.0, 0.0], min=0, max=1, update=None)
    bpy.types.Scene.icyp_color_helper_sub3_color = bpy.props.FloatVectorProperty(name="Sub3 color", subtype="COLOR", default=[0.0, 0.0, 0.0], min=0, max=1, update=None)
    bpy.types.Scene.icyp_color_helper_sub4_color = bpy.props.FloatVectorProperty(name="Sub4 color", subtype="COLOR", default=[0.0, 0.0, 0.0], min=0, max=1, update=None)
    bpy.types.Scene.icyp_COLOR_SCHEME_PROP = bpy.props.EnumProperty(name = "Color Scheme",items = icyp_color_scheme_type,update = change_color)
    for cls in classes:
        bpy.utils.register_class(cls)
    
    
# アドオン無効化時の処理
def unregister():
    del bpy.types.Scene.icyp_COLOR_SCHEME_PROP
    del bpy.types.Scene.icyp_color_helper_sub1_color
    del bpy.types.Scene.icyp_color_helper_sub2_color
    del bpy.types.Scene.icyp_color_helper_sub3_color
    del bpy.types.Scene.icyp_color_helper_sub4_color
    del bpy.types.Scene.icyp_color_helper_main_color 
    for cls in classes:
        bpy.utils.unregister_class(cls)

    
if "__main__" == __name__:
    register()
