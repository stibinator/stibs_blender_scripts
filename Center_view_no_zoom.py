######################################################################################################
# datestamps the last saved version of a project, and saves it into a zip file                       #
# License: GPL v3                                                                                    #
######################################################################################################

############# Add-on description (used by Blender)
bl_info = {
    "name": "Center view",
    "description": 'Centers the 3d view without zooming',
    "author": "stib",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "View > Center view - no zoom",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "https://blob.pureandapplied.com.au/save-n-Zip",
    "category": "3D View"}

##############
import bpy, mathutils


class CENTEREVIEWNZ_OT(bpy.types.Operator):
    """Center the 3D viewport on the selected item without zooming"""
    bl_idname = "view.center_no_zoom"
    bl_label = "Center view - no zoom"
   
    def execute(self, context):
        curs = context.scene.cursor.location
        oldCurs = mathutils.Vector()
        for i in range(len(curs)):
            oldCurs[i] = curs[i]
        bpy.ops.view3d.snap_cursor_to_active()
        bpy.ops.view3d.view_center_cursor()
        context.scene.cursor.location = oldCurs
        return {'FINISHED'}
 
def draw_into_view_menu(self,context):
    self.layout.separator()
    self.layout.operator('view.center_no_zoom')

            
def register():
    bpy.utils.register_class(CENTEREVIEWNZ_OT)
    bpy.types.VIEW3D_MT_view.append(draw_into_view_menu)
    
def unregister():
    bpy.utils.unregister_class(CENTEREVIEWNZ_OT)
    bpy.types.VIEW3D_MT_view.remove(draw_into_view_menu)
    
if __name__ == "__main__":
    register()