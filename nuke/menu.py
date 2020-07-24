import nuke
import nuke_utils.quickies as _quickies
import nuke_utils.callbacks as _callbacks

# Menu creation for `WGID Scripts`
__top_menu = nuke.menu("Nuke").addMenu("WDIG")


# Append Tools
__top_menu.addCommand("Set Localization/On", lambda: _quickies.set_localization(0))
__top_menu.addCommand("Set Localization/Off", lambda: _quickies.set_localization(3))
__top_menu.addCommand("Read From Write", _quickies.read_from_write, shortcut="alt+r")


nuke.callbacks.addOnCreate(_callbacks.enable_raw, nodeClass="Read")
nuke.callbacks.addOnCreate(_callbacks.enable_raw, nodeClass="Write")