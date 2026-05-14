# fsociety Prank EXE — Mr. Robot-themed prank app for Windows. Runs a fake "hacking" sequence
# Copyright (C) 2026 Danton Alexander
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see <https://www.gnu.org/licenses/>.


import tkinter as tk
import random
import textwrap

lines = [
    "Establishing secure connection...",
    "Bypassing firewall... done.",
    "Locating target files...",
    "Scanning /home/user/documents...",
    "Scanning /home/user/photos...",
    "Scanning /home/user/desktop...",
    "Generating encryption key...",
    "Initializing AES-256 cipher...",
    "Encrypting files...",
]

class FsocietyPrank:
    def __init__(self, root):
        self.root = root
        self.root.title("fsociety")
        self.root.configure(bg="black")
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: None)

        self.step = 0
        self.pct = 0
        self.blink_on = True
        self.countdown = 3

        self.ascii_label = tk.Label(root, text=textwrap.dedent("""
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XX                                                                          XX
        XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
        XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
        XX   MMMMMy''                                                    ''yMMMMM   XX
        XX   MMMy'                                                          'yMMM   XX
        XX   Mh'                                                              'hM   XX
        XX   -                                                                  -   XX
        XX                                                                          XX
        XX   ::                                                                ::   XX
        XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX
        XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
        XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
        XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
        XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX
        XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
        XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX
        XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX
        XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX
        XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX
        XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
        XX                                oo      oo                                XX
        XX           oM                 oo          oo                 Mo           XX
        XX         oMMo                M              M                oMMo         XX
        XX       +MMMM                 s              s                 MMMM+       XX
        XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX
        XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX
        XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX
        XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX
        XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX
        XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX
        XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX
        XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX
        XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX
        XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX
        XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX
        XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX
        XX   MMMMMMMM-                                                  -MMMMMMMM   XX
        XX   MMMMMMMMM                                                  MMMMMMMMM   XX
        XX   MMMMMMMMMy                                                yMMMMMMMMM   XX
        XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX
        XX                                                                          XX
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

            .o88o.                               o8o                .
            888 `"                               `"'              .o8
           o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
            888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
            888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
            888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
           o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
                                                                        .o...P'
                                                                        `XER0'
        """), fg="#00ff00", bg="black",
            font=("Courier New", 5), justify="left")
        self.ascii_label.pack(pady=(20, 10))

        self.status_label = tk.Label(root,
            text="⚠  WARNING: INITIATING IN 3...",
            fg="#ff4400", bg="black",
            font=("Courier New", 13), justify="center")
        self.status_label.pack(pady=10)

        self.progress_canvas = tk.Canvas(root, width=340, height=22,
            bg="black", highlightthickness=1, highlightbackground="#00ff00")

        self.progress_bar = self.progress_canvas.create_rectangle(
            0, 0, 0, 22, fill="#00ff00", outline="")
        self.progress_text = self.progress_canvas.create_text(
            170, 11, text="0%", fill="#00ff00",
            font=("Courier New", 10, "bold"))

        self.warning_label = tk.Label(root,
            text="⚠  YOUR FILES HAVE BEEN ENCRYPTED  ⚠",
            fg="#ff0000", bg="black",
            font=("Courier New", 18, "bold"))

        self.reveal_label = tk.Label(root,
            text="You have been pwnd by fsociety 😄",
            fg="#ffff00", bg="black",
            font=("Courier New", 13))

        self.ok_btn = tk.Button(root, text="[ I've been pwnd ]",
            fg="#00ff00", bg="black",
            font=("Courier New", 12),
            relief="ridge", bd=1, cursor="hand2",
            activebackground="#00ff00", activeforeground="black",
            command=self.show_done)

        self.done_label = tk.Label(root,
            text="Hello, friend.\nNothing has been modified.\nThis is a harmless prank\n[ mr. robot ]",
            fg="#00ff00", bg="black",
            font=("Courier New", 14), justify="center")

        self.flicker()
        self.root.after(1000, self.tick_countdown)

    def flicker(self):
        color = "#00cc00" if random.random() < 0.05 else "#00ff00"
        self.ascii_label.config(fg=color)
        self.root.after(150, self.flicker)

    def tick_countdown(self):
        self.countdown -= 1
        if self.countdown > 0:
            self.status_label.config(text=f"⚠  WARNING: INITIATING IN {self.countdown}...")
            self.root.after(1000, self.tick_countdown)
        else:
            self.status_label.config(text="", fg="#00ff00")
            self.progress_canvas.pack(pady=10)
            self.next_line()
            self.update_bar()

    def next_line(self):
        if self.step < len(lines):
            self.status_label.config(text=lines[self.step])
            self.step += 1
            self.root.after(900, self.next_line)

    def update_bar(self):
        if self.pct < 100:
            self.pct = min(100, self.pct + random.randint(1, 4))
            self.progress_canvas.coords(self.progress_bar, 0, 0, self.pct * 3.4, 22)
            self.progress_canvas.itemconfig(self.progress_text, text=f"{self.pct}%")
            self.root.after(180, self.update_bar)
        else:
            self.root.after(400, self.show_alert)

    def show_alert(self):
        self.status_label.pack_forget()
        self.progress_canvas.pack_forget()
        self.warning_label.pack(pady=30)
        self.blink_warning()
        self.root.after(2000, self.show_reveal)

    def blink_warning(self):
        color = "#ff0000" if self.blink_on else "black"
        self.warning_label.config(fg=color)
        self.blink_on = not self.blink_on
        self.root.after(500, self.blink_warning)

    def show_reveal(self):
        self.reveal_label.pack(pady=10)
        self.ok_btn.pack(pady=10)

    def show_done(self):
        self.warning_label.pack_forget()
        self.reveal_label.pack_forget()
        self.ok_btn.pack_forget()
        self.done_label.pack(pady=30)
        self.root.bind("<Escape>", lambda _: self.root.destroy())


if __name__ == "__main__":
    root = tk.Tk()
    app = FsocietyPrank(root)
    root.mainloop()
