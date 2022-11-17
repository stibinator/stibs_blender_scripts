import bpy
bl_info = {
    "name": "force_KF",
    "description": "Adds a keyframe for location and rotation, even if 'add only needed is on and the property isn't changing",
    "author": "stib",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "pose mode> pose > force_KF",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "https://blob.pureandapplied.com.au/force_KF",
    "category": "Animation",
    "bl_idname": "object.force_key_add"
}


def main(context):
    posBons = context.selected_pose_bones
    for bon in posBons:
        bon.keyframe_insert("location")
        bon.keyframe_insert("rotation_euler")


class ForceKF(bpy.types.Operator):
    """Adds a keyframe for location and rotation, even if 'add only needed' is on and the property isn't changing"""
    bl_idname = "object.force_key_add"
    bl_label = "force add key"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(ForceKF.bl_idname, text=ForceKF.bl_label)


# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(ForceKF)
    bpy.types.VIEW3D_MT_pose.append(menu_func)


def unregister():
    bpy.utils.unregister_class(ForceKF)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.force_key_add()
