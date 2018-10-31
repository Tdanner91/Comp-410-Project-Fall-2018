import os


def folderCrawler(folder):
    availableFiles = []
    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            if '.py' == name[-3:]:
                availableFiles.append(name)

    return availableFiles
