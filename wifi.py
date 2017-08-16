from subprocess import check_output


def scan():
    return check_output("iwlist wlan0 scan", shell=True)


def parse_cells(scan_output):
    cells = str(scan_output).split('          Cell ')[1:]

    for cell in cells:
        cell_lines = cell.split('\\n')
        address = cell_lines[0][14:]

        for l in cell_lines:
            t = l.strip()
            if t.startswith("ESSID"):
                yield address, t.split('ESSID:')[1].strip('"')

