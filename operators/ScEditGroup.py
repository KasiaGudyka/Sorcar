import bpy

from bpy.types import Operator
from ..helper import sc_poll_op

class ScEditGroup(Operator):
    bl_idname = "sc.edit_group"
    bl_label = "Edit Group"

    @classmethod
    def poll(cls, context):
        return (
            sc_poll_op(context)
        )

    def execute(self, context):
        space = context.space_data
        node_tree = space.node_tree
        path = space.path
        node = path[len(path)-1].node_tree.nodes.active

        if hasattr(node, "node_tree"):
            path.append(node.node_tree, node=node)
        elif len(path) > 1:
            path.pop()
        return {"FINISHED"}