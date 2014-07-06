
import numpy
import sys
import textwrap

def directions(degrees):
	if degrees == 0:
		return "You are going East"
	elif degrees == 90:
		return "You are going North"
	elif degrees == 180:
		return "You are going West"
	elif degrees == 270:
		return "You are going South"
	directions = [["North ","East "],["North ","West "],["South ", "West "],["South ", "East "]]
	main_dir = int(degrees/90)
	if degrees<90 or (degrees>180 and degrees<270):
		if degrees%90>45:
			num_say = int(numpy.reciprocal(round((90-(degrees%90)))/90)/2)
			if num_say == 0:
				num_say = 1
			return "You are going " + directions[main_dir][0] * num_say + directions[main_dir][1]
		else:
			num_say = int(numpy.reciprocal(round((degrees%90))/90)/2)
			if num_say == 0:
				num_say = 1
			return "You are going " + directions[main_dir][0] + directions[main_dir][1] * num_say
	else:
		if degrees%90>45:
			num_say = int(numpy.reciprocal(round((90-(degrees%90)))/90)/2)
			if num_say == 0:
				num_say = 1
			return "You are going " + directions[main_dir][0] + directions[main_dir][1] * num_say
		else:
			num_say = int(numpy.reciprocal(round((degrees%90))/90)/2)
			if num_say == 0:
				num_say = 1
			return "You are going " + directions[main_dir][0] * num_say + directions[main_dir][1]
	
def cowsay(str, length=40):
    return build_bubble(str, length) + build_cow()

def build_cow():
    return """
         \   ^__^ 
          \  (oo)\_______
             (__)\       )\/\\
                 ||----w |
                 ||     ||
    """

def build_bubble(str, length=40):
    bubble = []

    lines = normalize_text(str, length)

    bordersize = len(lines[0])

    bubble.append("  " + "_" * bordersize)

    for index, line in enumerate(lines):
        border = get_border(lines, index)

        bubble.append("%s %s %s" % (border[0], line, border[1]))

    bubble.append("  " + "-" * bordersize)

    return "\n".join(bubble)

def normalize_text(str, length):
    lines  = textwrap.wrap(str, length)
    maxlen = len(max(lines, key=len))
    return [ line.ljust(maxlen) for line in lines ]

def get_border(lines, index):
    if len(lines) < 2:
        return [ "<", ">" ]
    elif index == 0:
        return [ "/", "\\" ]
    elif index == len(lines) - 1:
        return [ "\\", "/" ]
    else:
        return [ "|", "|" ]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: '%s string'" % sys.argv[0]
        sys.exit(0)
    print cowsay(directions(float(sys.argv[1])))