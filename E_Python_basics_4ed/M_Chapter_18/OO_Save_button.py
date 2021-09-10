"""Challenge: Return of the Poet 18.10"""

from tkinter.filedialog import asksaveasfilename


def save_button():
    """This function save the poem to a text file"""
    import OO_Visual_layout_Challenge as layout
    file_path = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        initialfile="My_poem"
    )

    if not file_path:
        return
    with open(file_path, mode="w") as output:
        text = layout.lbl_poem["text"]
        output.write(text)
"""
blood,end,flame
burns,mixes,passes
bloody,madly,wisful
onto,,within
terribly"""