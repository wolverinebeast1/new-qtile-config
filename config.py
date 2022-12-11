# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    #Window management stuff
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    #Key binding to launch programs
    #File manager
    Key([mod], "e", lazy.spawn("pcmanfm")),
    #Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="alacritty"),
    #Launch rofi
    Key([mod], "m", lazy.spawn("rofi -show run")),
    #Launch Firefox
    Key([mod], "b", lazy.spawn("brave")),

    #Switch between keyboards
    Key([mod] , "0" , lazy.spawn("setxkbmap ru")),
    Key([mod] , "y" , lazy.spawn("setxkbmap es")),


]

groups = [Group(i) for i in ["   " , "   " , "   " , "   " , "  "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layout_conf = {
    'border_focus': '#ffd47e',
    'border_width': 2,
    'margin': 10


}


layouts = [
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=17,
    padding=10,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [


                widget.GroupBox(
                    foreground=["#ABB2BF", "#ABB2BF"],
                    background=["#0f101a","#0f101a"],
                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=12,
                    padding_x=9,
                    borderwidth=1,
                    active=["#f1ffff","#f1ffff"],
                    inactive=["#4c566a","#4c566a"],
                    rounded=True,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border=[],
                    this_current_screen_border=["#1e2127","#1e2127"],
                    this_screen_border=["#353c4a","#353c4a"],
                    other_current_screen_border=["#0f101a","#0f101a"],
                    other_screen_border=["#0f101a","#0f101a"],
                    disable_drag=True
                ),
                
                
               
                widget.WindowName(
                    foreground=["#F07178","#F07178"],
                    background=["#0f101a","#0f101a"],
                    fontsize=13,
                    font='UbuntuMono Nerd Font',
                    
                ),
               




                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ), 
                
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(
                    background=["#0f101a","#0f101a"],
                    foreground=["#f1ffff", "#f1ffff"],
                ),
                #Keyboard layout
                widget.TextBox(
                    text="",
                    foreground=["#ff0000", "#ff0000"],
                    padding=5,
                    background=["#0f101a","#0f101a"],
                ),
                widget.Net(
                    foreground=["ffff00", "ffff00"],
                    background=["#0f101a","#0f101a"],
                ),
                widget.OpenWeather(
                    location='Torrevieja',
                    format='{location_city}:{temp}',
                    foreground=["#00ff00","#00ff00"],
                    background=["#0f101a","#0f101a"],
                    fontsize=14
                    
                ),
                widget.TextBox(
                    text="",
                    background=["#0f101a","#0f101a"],
                ),


                
                widget.KeyboardLayout(
                    configured_keyboards=['es'],
                    foreground=["#ffffff","#ffffff"],
                    background=["#0f101a","#0f101a"],
                    fontsize=15
                    ),
                #powerline
                 widget.TextBox(
                    text="",
                    fontsize=42,
                    padding=-3,
                    background=["#0f101a","#0f101a"],
                    foreground=["#353c4a","#353c4a"],
                    ),


                widget.CurrentLayoutIcon(
                    scale=0.55,
                    foreground=["#1e90ff","#1e90ff"],
                    background=["#353c4a","#353c4a"],

                 ),


                widget.CurrentLayout(
                    
                    foreground=["#ffffff","#ffffff"],
                    background=["#353c4a","#353c4a"],
                    fontsize=15
                 ),

 

               #powerline     
                widget.TextBox(
                        text="",
                        fontsize=42,
                        padding=-4,
                        foreground=["#000000","#000000"],
                        background=["#353c4a","#353c4a"],
                    ),
                    #Clock icon
                widget.TextBox(
                        text="",
                        background=["#000000","#000000"],
                        foreground = ["#f1ffff", "#f1ffff"], 
                        padding=5
                        ),
                    #Clock Widget
                widget.Clock(
                    background=["#000000","#000000"],
                    foreground = ["#f1ffff", "#f1ffff"], 
                    format='%d/%m/%Y - %H:%M ',
                    fontsize=15,
                    padding=5,
                    
                    ),
            ],
            30,
            opacity=0.9
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
