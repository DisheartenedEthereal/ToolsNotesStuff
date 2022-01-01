import json
import matplotlib.pyplot as plt
SWEARS = ["کص","کیر","fuck","ass","cunt","nigga","dick","pussy","خایه","جنده","فاحشه","خراب"]
JESUS = ["jesus","خدا","پروردگار","جیزز"]
class data:
    def __init__(self, file):
        f = open(file, 'r')
        data = f.read()
        f.close()
        self.artist_names = {}
        self.audio_count = 0
        self.video_count = 0
        self.text_count = 0
        self.picture_count = 0
        self.swear_count = 0
        self.jesus_count = 0
        self.total_word_count = 0
        self.isADogshitKpoper = False
        self.all_texts = []
        self.data = json.loads(data)
        for item in self.data["messages"]:
            try:
                if item["media_type"] == "audio_file":
                    self.audio_count += 1
                    if item["performer"] == "BTS" or item["performer"] == "EXO":
                        self.isADogshitKpoper = True
                    self.dealWithArtists(item["performer"])
                elif item["media_type"] == "video_file":
                    self.video_count += 1
            except KeyError:
                try:
                    if item["photo"] == "(File not included. Change data exporting settings to download.)" :
                        self.picture_count += 1
                except KeyError:
                    self.text_count += 1
                    self.all_texts.append(item["text"])
        self.CheckForSwears()
        self.CheckForGod()
        print("Audio files:", self.audio_count)
        print("Video files:", self.video_count)
        print("Picture files:", self.picture_count)
        print("Text files:", self.text_count)
        print("Swear words:", self.swear_count)
        print("God count: ", self.jesus_count)
        self.plotSwearRatio()
        self.plotMessageRatio()
        self.plotArtists()
    def CheckForSwears(self):
        for text in self.all_texts:
            self.total_word_count += 1
            for swear in SWEARS:
                if swear in text:
                    self.swear_count += 1
    def CheckForGod(self):
        for text in self.all_texts:
            self.total_word_count += 1
            for god in JESUS:
                if god in text:
                    self.jesus_count += 1
    def dealWithArtists(self,artist):
        if artist in self.artist_names:
            self.artist_names[artist] += 1
        else:
            self.artist_names[artist] = 1
    def plotArtists(self):
        labels = []; sizes = []
        for x, y in self.artist_names.items():
            labels.append(x)
            sizes.append(y)
        plt.figure(figsize=(20,20),dpi=250)
        plt.pie(sizes, labels=labels,textprops={'fontsize': 5})
        plt.axis('equal')
        plt.savefig('artists.png')
        plt.figure().clear()
    def plotSwearRatio(self):

        labels = 'Swear', 'God', 'Normal'
        sizes = [self.swear_count, self.jesus_count , self.total_word_count - self.swear_count - self.jesus_count]
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        explode = (0, 0.1, 0)
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=False, startangle=90)
        plt.axis('equal')
        plt.title('Swear to word ratio')
        plt.savefig('pie.png')
        plt.figure().clear()
    def plotMessageRatio(self):
        labels = 'Audio', 'Video', 'Text', 'Picture'
        sizes = [self.audio_count, self.video_count, self.text_count, self.picture_count]
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        explode = (0, 0.1, 0,0)
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=False, startangle=90)
        plt.axis('equal')
        plt.title('Message ratio')
        plt.savefig('messages.png')
        plt.figure().clear()






data = data('result.json')
