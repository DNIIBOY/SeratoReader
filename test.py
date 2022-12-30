import LinkToPy

path_to_carabiner = "Carabiner.exe"
link = LinkToPy.LinkInterface(path_to_carabiner)
while True:
    print(link.bpm_)
