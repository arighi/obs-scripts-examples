import obspython as obs
import random

source_name = 'Follow'

def cycle():
    current_scene = obs.obs_scene_from_source(obs.obs_frontend_get_current_scene())
    scene_item = obs.obs_scene_find_source(current_scene, source_name)
    if scene_item is not None:
        status = not obs.obs_sceneitem_visible(scene_item)
        obs.obs_sceneitem_set_visible(scene_item, status)

def script_properties():
    props = obs.obs_properties_create()

    obs.obs_properties_add_int(props, "enabled", "Enabled",
                               0, 1, 0)
    obs.obs_properties_add_int(props, "cycle_rate", "Cycle Rate(ms)",
                               5000, 1000000, 5000)
    return props

def script_update(settings):
    obs.timer_remove(cycle)
    if obs.obs_data_get_int(settings, "enabled"):
        blink_rate = obs.obs_data_get_int(settings, "cycle_rate")
        obs.timer_add(cycle, blink_rate)
