from modules import scripts
from modules import script_callbacks
from modules.processing import Processed, process_images
from modules.shared import opts, OptionInfo

class Script(scripts.Script):
    def title(self):
        return "Default negatives"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def process(self, p):
        if opts.sd_def_neg != "":
            p.all_negative_prompts = [f"{opts.sd_def_neg}, {n}" for n in p.all_negative_prompts]

def on_before_image_saved(params : script_callbacks.ImageSaveParams):
    if opts.sd_def_neg != "":
        params.pnginfo["parameters"] = params.pnginfo["parameters"].replace(f"{opts.sd_def_neg}, ", "")
        pass

# Add option to settings
def on_ui_settings():
    opts.add_option("sd_def_neg", OptionInfo("", "Set default negatives", section=("sd", "Stable Diffusion")))

script_callbacks.on_ui_settings(on_ui_settings)
script_callbacks.on_before_image_saved(on_before_image_saved)