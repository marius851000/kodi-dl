class KodiHandle:
    def __init__(self, addon):
        self.addon = addon
        self.sub_content = []
        self.finished = False
        self.resolved_listitem = None

    def add_directory_item(self, url, listitem, is_folder, total_items):
        to_add = {
            "url": url,
            "listitem": listitem,
            "is_folder": is_folder,
            "total_items": total_items
        }
        self.sub_content.append(to_add)

    def end_of_directory(self, handle, succeeded, update_listing, cache_to_disc):
        #TODO: use the 3 other value
        if not succeeded:
            raise BaseException("the listing of a directory failed")
        if update_listing:
            print("kodidl: not using a update_listing = True")
        if cache_to_disc:
            print("kodidl: not using cache_to_dict = True")
        self.finished = True

    def __str__(self):
        if self.resolved_listitem == None:
            resolved = ""
        else:
            resolved = "resolved "
        return "<{}KodiHandle with {} sub content>".format(resolved, len(self.sub_content))

    def set_resolved_url(self, succeeded, listitem):
        if not succeeded:
            raise BaseException("setting a resolved url failed")
        self.resolved_listitem = listitem

    def pretty_print(self, pre=""):
        if self.sub_content != []:
            print(pre+"sub content:")
            for sub_content in self.sub_content:
                print(pre+"\turl: {} , total_items: {} , is_folder : {}".format(sub_content["url"], sub_content["total_items"], sub_content["is_folder"]))
                print(pre+"\tlistitem:")
                sub_content["listitem"].pretty_print(pre+"\t\t")
            print(pre+"folder finished: {}".format(self.finished))
        if self.resolved_listitem != None:
            print(pre+"resolved list item:")
            self.resolved_listitem.pretty_print(pre+"\t")

    def to_dict(self):
        result = {"sub_content": []}
        if self.resolved_listitem != None:
            result["resolved_listitem"] = self.resolved_listitem.to_dict()
        for sub_content in self.sub_content:
            result["sub_content"].append({
                "url": sub_content["url"],
                "is_folder": sub_content["is_folder"],
                "total_items": sub_content["total_items"],
                "listitem": sub_content["listitem"].to_dict()
            })
        return result
