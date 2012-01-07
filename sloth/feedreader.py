import feedparser
import re

from PyQt4 import QtCore


FILENAME_REPL = (("&amp","&"), ("[!!] ",""), (":"," "))
CRC32_RE = re.compile(".*(\([A-Fa-f0-9]{8,8}\)).*")

class FeedReader(QtCore.QObject):

    finishedLoading = QtCore.pyqtSignal([list])

    def load(self):
        dicts = []
        config = QtCore.QSettings()
        p_feed = feedparser.parse(str(config.value("feed").toString()))

        for entry in p_feed["entries"]:
            fileid = int(entry.link[-7:])
            if fileid <= config.value("lastfileid", 0):
                #logger.debug("Fileid is too low: %i" % fileid)
                continue

            filetype_re = re.compile(".*\.mkv.*")
            # If filetype_re is valid, the entry.title should be matched
            if filetype_re is not None:
                if filetype_re.match(entry.title) is None:
                    ## No match -> next entry
                    #logger.debug("%s didn't match your filetype_re" % entry.title)
                    continue

            if fileid > config.value("lastfileid", 0).toInt()[0]:
                config.setValue("lastfileid", fileid)

            # This all has to be executed whether filetype_re is None or there was
            # a match for filetype_re in entry.title
            # Clean up the name a bit
            anime = entry.title
            anime = anime.replace("[!!] ","")
            for i in FILENAME_REPL:
                anime.replace(i[0],i[1])
            anime_name = anime.split(" -")[0]
            group = anime.split("[")[-1].split("]")[0]
            episode = anime.split(" -")[1]

            text = entry.content[0]["value"].replace("\n","")
            crc = CRC32_RE.match(text)
            if crc is not None:
                crc = crc.group(1).lower()[1:9]
            else:
                continue
            dicts.append(
                     {"anime": anime_name,
                    "crc": crc,
                    "episode": episode,
                    "group": group})

        config.sync()
        self.finishedLoading.emit(dicts)
