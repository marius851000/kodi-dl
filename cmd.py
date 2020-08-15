from xbmcemu import KodiInstance

def quick_display(this_path_data):
    if len(this_path_data.sub_content) != 0:
        print("sub content")
        for sub_content in this_path_data.sub_content:
            url = sub_content["url"]
            listitem = sub_content["listitem"]
            label = listitem.label
            print("{} : {}".format(label, url))
    if this_path_data.resolved_listitem != None:
        print("resolved content")
        this_path_data.resolved_listitem.pretty_print()


kodi = KodiInstance("/home/marius/.kodi")

running = True
path = "plugin://plugin.video.needforponies/?"
this_path_data = kodi.run_url(path)

quick_display(this_path_data)
while running:
    try:
        line = raw_input(">")
    except:
        line = input(">")
    line_splited = line.split(" ")
    if len(line) >= 1:
        command = line_splited[0]
        if command == "exit":
            running = False
        elif command == "help":
            print("accepted command")
            print("exit: exit the cmd")
            print("goto <path>: go to the selected path, and display the data here")
            print("pp : display all the data avalaible about this folder")
            print("qd : display some information about this folder (the same displayed after goto)")
        elif command == "goto":
            if len(line_splited) == 2:
                path = line_splited[1]
                this_path_data = kodi.run_url(path)
                quick_display(this_path_data)
            else:
                print("the \"goto\" command accept only 1 argument")
        elif command == "pp":
            this_path_data.pretty_print()
        elif command == "qd":
            quick_display(this_path_data)
        else:
            print("unreconized command \"{}\"".format(command))
print("exiting")
