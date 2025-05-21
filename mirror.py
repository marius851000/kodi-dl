import os
import xbmcemu
import tempfile
import json
import subprocess
import shutil

try:
    from urllib import quote
except:
    from urllib.parse import quote

class DataToDownload:
    def __init__(self, listitem, url):
        self.listitem = listitem
        self.url = url

def quote_folder(text):
    return quote(text, safe=" ")


def get_listitem_data_to_download(to_download, listitem):
    name_prefix = "d_" + get_subfolder_name(listitem) + "_"
    if listitem.path:
        to_download[name_prefix + "content.main"] = listitem.path

    sub_nb = 0
    for subtitle_url in listitem.subtitles:
        if subtitle_url != None:
            to_download[name_prefix + "content.sub.{}".format(sub_nb)] = subtitle_url
        sub_nb += 1

    for art_category in listitem.arts:
        art_url = listitem.arts[art_category]
        to_download[name_prefix + "art.{}".format(art_category)] = art_url


def get_subfolder_name(listitem):
    return listitem.label

def save_to_folder(kodi, dest_folder, url, sub_content_from_parent=None, skip=[]):
    data_file = os.path.join(dest_folder, "data.json")
    if os.path.isfile(data_file):
        return

    if url in skip:
        return

    print("will save the folder {}".format(dest_folder))
    print("downloading {}".format(url))
    if not os.path.isdir(dest_folder): #for py2
        os.makedirs(dest_folder)

    to_download = dict()

    result = kodi.run_url(url)
    for sub_content in result.sub_content:
        sub_folder_name = quote_folder(get_subfolder_name(sub_content["listitem"]))
        get_listitem_data_to_download(to_download, sub_content["listitem"])
        save_to_folder(kodi, os.path.join(dest_folder, "sf_" + sub_folder_name), sub_content["url"], sub_content, skip)

    if result.resolved_listitem != None:
        to_save = result.resolved_listitem
        if to_save.label == None:
            to_save.label = sub_content_from_parent["listitem"].label
        get_listitem_data_to_download(to_download, to_save)
        to_save.pretty_print("\t")

    for name in to_download:
        tmp_file = os.path.join(dest_folder, "tmp.tmp")
        url_to_download = to_download[name]

        print("downloading {}".format(url_to_download))
        #wget.download(url_to_download, tmp_file)
        #try to find the file extension
        if "." in url_to_download:
            url_splited_dot = url_to_download.split(".")
            extension = None
            if len(url_splited_dot) >= 2:
                potential_extension = url_splited_dot[-1]
                if "/" in potential_extension:
                    pass
                elif len(potential_extension) >= 10:
                    pass
                else:
                    extension = potential_extension
        if extension == None:
            raise BaseException("unable to find the extension of the file at {}".format(url_to_download))

        dest_file = os.path.join(dest_folder,quote_folder(name+".")+extension)

        subprocess.check_call(["wget", url_to_download, "-O", tmp_file])
        subprocess.check_call(["mv", tmp_file, dest_file])

    # remove all remaining tmp file
    for file_name in os.listdir(dest_folder):
        if file_name.split(".")[-1] == "tmp":
            os.remove(os.path.join(dest_folder, file_name))

    dumped = json.dumps(result.to_dict(), indent=1)
    f = open(data_file, "w")
    f.write(dumped)
    f.close()

if __name__ == "__main__":
 #   DATA_FOLDER = "/home/marius/kodi-dl/mirror-test"
    kodi = xbmcemu.KodiInstance("/home/marius/.kodi")

#    save_to_folder(kodi, DATA_FOLDER, "plugin://plugin.video.needforponies/?")
#    save_to_folder(kodi, "/home/marius/kodi-dl/music-mlpfrance", "plugin://plugin.audio.mlpfrance/?", skip=[
 #       "plugin://plugin.audio.mlpfrance/?action=list_bonus_videos&section_nb=7",
#       "plugin://plugin.audio.mlpfrance/?action=list_albums&page=loe"
#    ])
    #TODO: rm -rf **/tmp.*.tmp
    save_to_folder(kodi, "/home/marius/kodi-dl/ponylife", "plugin://plugin.video.mlpfrance/?action=list_episodes&season=ponylife")
