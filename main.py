import os


class SceneHandler:
    SYMBOLS_TRIGGER = (",", "...", "!", ".", "?", "…", "*", "~")
    IGNORE_PERS = ("gg", "gg_th")

    def __init__(self, dir, tag):
        self.path = os.path.join(os.getcwd(), dir)
        self.tag = tag
        os.chdir(dir)

    def process_directory(self):
        lst_files = os.listdir()
        lst_files = list(filter(lambda x: "_proc" not in x,lst_files))
        for file in lst_files:
            self.process_file(file)

    def process_file(self, file):
        with open(file, 'r') as rf:
            self.__check_path()
            with open(os.path.splitext(file)[0] + "_proc.txt", 'w+') as af:
                line = rf.readline()
                while len(line) > 0:
                    af.write(self.process_line(line))
                    line = rf.readline()
            pass

    @staticmethod
    def __check_path():
        if os.path.isdir("res"):
            os.chdir("../res")
        else:
            os.chdir("..")
            os.mkdir("res")
            os.chdir("res")

    def process_line(self, line):
        if self.__check_on_skip_lines(line):
            return line
        else:
            strt_indx = line.index('"')
            line_start, lst_line = line[:strt_indx], line[strt_indx + 1: line.rindex('"')].split()
            if len(lst_line) == 1:
                proc_line = f'{line_start}"{self.tag} {lst_line[0]} {self.tag}"\n'
            else:
                lst_line[0] = f'"{self.tag} {lst_line[0]}'
                end_indx = len(lst_line) - 1
                proc_line = []
                for word in lst_line:
                    for symb in self.SYMBOLS_TRIGGER:
                        if symb in word:
                            word = f'{word} {self.tag}'
                            proc_line.append(word)
                            break
                    else:
                        proc_line.append(word)
                end_line = proc_line[end_indx]
                if self.tag not in end_line:
                    proc_line[end_indx] = f'{end_line} {self.tag}"\n'
                else:
                    proc_line[end_indx] = f'{end_line}"\n'
                proc_line = line_start + " ".join(proc_line)
            return proc_line

    def __check_on_skip_lines(self, line):
        if not line or line == "\n":
            return True
        if line[0] in ("#", "*"):
            return True
        for ignr_pers in self.IGNORE_PERS:
            if ignr_pers in line:
                return True
        return False


scene_handler = SceneHandler("source", "[hrtimg]")

if __name__ == '__main__':
    scene_handler.process_directory()
    print("All done succesfully!!!")
