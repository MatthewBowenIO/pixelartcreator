import curses, time, os, itertools, json, argparse

def openAllAnimationsInFolder(folderName):
    animation = []
    with open("logs.txt", "w") as log:
        for fileName in os.listdir(folderName):
            log.write(fileName + "\n")
            if fileName.endswith(".json"):
                with open(folderName + fileName) as ifile:
                    animation = animation + json.load(ifile).get("output")
                    ifile.close()
                animation.append([-1, -1])
        log.close()
    return animation

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ifile', help = 'Pixel art input', required = False)
    parser.add_argument('-f', '--folder', help = 'Entire animation folder', required = False)
    parser.add_argument('-s', '--speed', help = 'Animation speed', required = False)
    
    args = parser.parse_args()

    ifile = args.ifile or 'art.json'
    animSpeed = int(args.speed or 25)

    text = []
    if args.folder:
        text = openAllAnimationsInFolder(args.folder)
    else:
        with open(ifile) as ifile:
            text = json.load(ifile).get("output")
            ifile.close()

    s = curses.initscr()
    curses.curs_set(0)
    sh, sw = s.getmaxyx()

    if sh != 32 or sw != 100:
        os.execl('sh/resize.sh', '')

    w = curses.newwin(sh, sw, 0, 0)
    w.timeout(animSpeed)

    try:
        for pixel in text:
            if pixel[0] == -1:
                w.clear()
                continue
            w.getch()
            w.addch(pixel[0], pixel[1], curses.ACS_BLOCK)

        time.sleep(1)
        os.execl('sh/reset.sh', '')
    except Exception as e:
        os.execl('sh/reset.sh', '')

if __name__ == "__main__":
    main()
