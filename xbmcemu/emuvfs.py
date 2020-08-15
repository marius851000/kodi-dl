class File:
    def __init__(self, instance, filepath, mode):
        if instance.is_real_path(filepath):
            self.file = open(instance.get_real_path(filepath), mode)
        else:
            raise "{} can't be opened yet".format(filepath)

    def read(self):
        return self.file.read()

    def close(self):
        return self.file.close()
