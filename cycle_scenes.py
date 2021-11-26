import obspython as obs
import random

def cycle():
    current_scene = obs.obs_frontend_get_current_scene()
    if obs.obs_source_get_name(current_scene).startswith('Cycle'):
        scenes = obs.obs_frontend_get_scenes()
        cycle_scenes = []
        for s in scenes:
            if obs.obs_source_get_name(s).startswith('Cycle'):
                cycle_scenes.append(s)
        scenes.remove(current_scene)
        obs.obs_frontend_set_current_scene(random.choice(cycle_scenes))

def script_properties():
    props = obs.obs_properties_create()

    obs.obs_properties_add_int(props, "cycle_rate", "Cycle Rate(ms)",
                               5000, 1000000, 5000)
    return props

def script_update(settings):
    obs.timer_remove(cycle)
    blink_rate = obs.obs_data_get_int(settings, "cycle_rate")
    obs.timer_add(cycle, blink_rate)
