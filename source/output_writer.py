from stadt import Stadt
import csv
import math
import numpy as np


class OutputWriter:
    _gnu_template = \
'''
# {0}
set title "{0}"
rgb (r,g,b) = int(r)*65536 + int(g)*256 + int(b)
set xrange [0:{1}]
set yrange [0:{2}]
set size ratio -1
unset key
set datafile separator whitespace
scale=200
textColor = 'black'
set multiplot layout 1,1
plot "{0}.csv" using 1:2:($3*scale):(rgb($5,$6,$7)) \\
     with circles lc rgb variable fs transparent solid 0.5, \\
     "{0}.csv" using 1:2:(sprintf("%d", $4)) with labels notitle \\
     textcolor rgb textColor
'''

    _movable_keyword = {True: 'neu', False: 'alt'}

    def __init__(self, file_out: str):
        """
        Creates OutputWriter object to write stadt config
        into a txt or csv file
        :param file_out:
        """
        self.stadt = file_out
        self.out_txt = ("output/" + file_out + ".txt")
        self.out_csv = ("output/" + file_out + ".csv")
        self.out_gnu = ("output/" + file_out + ".gnu")

    @staticmethod
    def dec_to_rgb(RGBint: int):
        """
        Converts an integer to RGB values
        :param RGBint:
        :return: (red, green, blue)
        """
        blue = RGBint & 255
        green = (RGBint >> 8) & 255
        red = (RGBint >> 16) & 255
        return red, green, blue

    def write_txt(self, s: Stadt) -> None:
        """
        Writes stadt config to txt file
        :param s: Stadt
        :return: None
        """

        out = ""
        out += "//***********************************\n"
        out += f"// Stadtplan {s.get_name()}\n"
        out += f"// {len([r for r in s.get_rettungsstationen() if not r.is_movable()])} " \
               + f"und {len([r for r in s.get_rettungsstationen() if r.is_movable()])} " \
               + f"neue Stationen\n"
        out += "//***********************************\n"
        out += f"Rettungsstellen alt: {len([r for r in s.get_rettungsstationen() if not r.is_movable()])}\n"
        out += f"Rettungsstellen neu: {len([r for r in s.get_rettungsstationen() if r.is_movable()])}\n"

        out += "\n"

        for i, r in enumerate(s.get_rettungsstationen()):
            out += f"Rettungsstelle: {i} - {OutputWriter._movable_keyword[r.is_movable()]}\n"
            out += str(r.get_position())
            out += "\nZugeordnete Stadtteile:\n"

            for count, borrow in enumerate(r.get_responsibilities()):
                out += str(borrow.get_position())
                out += " "
                count += 1
                if count % 5 == 0:
                    out += "\n"
            out += "\n"
            out += f"Gewichtete Stadtteile: {r.cum_dist()}\n"
            out += "\n"

        out += "\n"
        out += f"Gesamtstrecke: {s.get_total_distance()}"

        with open(self.out_txt, "w", newline="") as f:
            f.write(out)

    def write_csv(self, s: Stadt) -> None:
        """
        Writes stadt config to csv file
        :param s: Stadt
        :return: None
        """

        # modify and write gnuplot script for specific problem
        with open(self.out_gnu, 'w', newline='') as gnu_script:
            gnu_script.write(OutputWriter._gnu_template.format(
                s.get_name(),
                s.get_length() * 1000,
                s.get_width() * 1000
            ))
            gnu_script.close()

        # create and write CSV file to be read by Gnuplot
        with (open(self.out_csv, 'w', newline='') as csv_file):
            writer = csv.writer(csv_file, delimiter=" ")

            dec_colors = np.linspace(0x0, 0xFFFFFF,
                                   num=len(s.get_rettungsstationen()), dtype=int)

            for r, dec_color in zip(s.get_rettungsstationen(), dec_colors):
                rgb = self.dec_to_rgb(dec_color)
                for borrow in r.get_responsibilities():
                    root_u = math.sqrt(borrow.get_unfallquote()
                                       )if borrow.get_unfallquote() > 0 else 0.7

                    writer.writerow(
                        [borrow.get_position().x(),
                         borrow.get_position().y(),
                         root_u,
                         borrow.get_unfallquote(),
                         rgb[0],  # red
                         rgb[1],  # green
                         rgb[2]]  # blue
                    )
            for r in s.get_rettungsstationen():
                writer.writerow(
                    [r.get_position().x(),
                     r.get_position().y(),
                     2,
                     r.get_id(),
                     255,  # red
                     0,  # green
                     0]  # blue
                )
