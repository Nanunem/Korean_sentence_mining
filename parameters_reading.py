class ReadingParamFile:
    """
    Object reads the file parameters.txt to get the date,
    choice of download
    """
    def __init__(self, day_mining):
        self.day_mining = day_mining

    def reading(self):
        choice = []
        dates_requested = []
        create_deck_answer = ""

        with open(self.day_mining, "r") as Input:
            for line in Input:
                if "#" not in line and "Create" not in line:
                    if not line.strip() :
                        pass
                    else:
                        line = line.strip()
                        line = line.split()
                        dates_requested.append(line[0].strip())
                        choice.append(line[-1].strip())
                elif "Create" in line:
                    line = line.strip()
                    line = line.split("?")
                    create_deck_answer = line[-1]
        return dates_requested, choice, create_deck_answer