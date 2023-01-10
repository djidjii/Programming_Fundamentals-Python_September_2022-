# import re
#
# text = input()
# pattern = r"(#|$|%|\*|&)([A-Za-z])+(\1)=(\d+)!!(\w*)"
# result = re.search(pattern, text)
#
#
# print(result.groups(1))
#
# # %GiacomoAgostini%=7!!hbqw
# # &GeoffDuke*=6!!vjh]zi
# # JoeyDunlop=10!!lkd,rwazdr
# # Mike??Hailwood=5!![pliu
# # #SteveHislop#=16!!df%TU[Tj(h!!TT[S

class EventTracker:

    def __init__(self):
        self.api_url = "https://www.pythonmorsels.com/making-singletons/"

    def track(self):
        print(f"TODO track event at {self.api_url}")
