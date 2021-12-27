class ReadingParamFile:
    """
    Object reads the file week.txt to get the date,
    choice of download
    """
    def __init__(self, day_mining):
        self.day_mining = day_mining

    def reading(self):
        choice = []
        dates_requested = []

        with open(self.day_mining, "r") as Input:
            for line in Input:
                if "#" not in line :
                    line = line.strip()
                    line = line.split()
                    dates_requested.append(line[0].strip())
                    choice.append(line[-1].strip())
        return dates_requested, choice