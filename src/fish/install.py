import string
import os
import os.path


def install(config, options):
    command = string.Template("""#!/usr/bin/env fish

complete -c main.py -f
complete -c main.py -a "(python $script --tasks)"
""")
    script_name = options.script if options.script else "main.py"
    home = os.getenv("HOME")
    plugin_dir = os.path.join(home, ".config/fish/completion")
    plugin_path = os.path.join(plugin_dir, script_name + ".fish")

    if not os.path.exists(plugin_dir):
        os.mkdir(plugin_dir)

    with open(plugin_path, "w+") as f:
        f.write(command.substitute(script=script_name))

    print("success")