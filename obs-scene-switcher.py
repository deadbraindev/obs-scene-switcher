import obspython as obs
import random

# ------------------------------------------------------------


def cycle():

    scenes = obs.obs_frontend_get_scenes()
    current_scene = obs.obs_frontend_get_current_scene()
    scenes.remove(current_scene)
    
    # Jeśli są dostępne inne sceny, losujemy i ustawiamy nową scenę
    if scenes:
        new_scene = random.choice(scenes)
        obs.obs_frontend_set_current_scene(new_scene)
        print("Wybrana nowa scena:", obs.obs_source_get_name(new_scene))
    else:
        print("Brak dostępnych scen.")

# ------------------------------------------------------------


def script_properties():
    """
    Called to define user properties associated with the script. These
    properties are used to define how to show settings properties to a user.
    """
    props = obs.obs_properties_create()

    obs.obs_properties_add_int(props, "cycle_rate", "Cycle Rate in minutes",
                               1, 1440, 1)  # from 1 to 1440 minutes (1 day)
    
    return props


def script_update(settings):
    """
    Called when the script’s settings (if any) have been changed by the user.
    """

    obs.timer_remove(cycle)
    cycle_rate_minutes = obs.obs_data_get_int(settings, "cycle_rate")
    cycle_rate_ms = cycle_rate_minutes * 60 * 1000  # Convert minutes to milliseconds
    print("Cycle rate:", cycle_rate_minutes, "min (", cycle_rate_ms, "ms)")

    obs.timer_add(cycle, cycle_rate_ms)
    
def script_load(settings):
    """
    Called when the script is loaded, generally at startup or when the script
    is reloaded manually.
    """
    scenes = obs.obs_frontend_get_scenes()
    scene_names = [obs.obs_source_get_name(scene) for scene in scenes]
    print("Available scenes:", scene_names)
    obs.source_list_release(scenes)

def script_defaults(settings):
    """
    Called to set default settings.
    """
    obs.obs_data_set_default_int(settings, "cycle_rate", 1)