import pypff
import sys

if len(sys.argv) != 3:
    print("Need to have 2 arguments: <pst file> <search term>")
    sys.exit(1)

pst_file = sys.argv[1]
search_term = sys.argv[2]

print("PST file:", pst_file)
print("Search term:", search_term)

pst = pypff.file()
pst.open(pst_file)

print("Size:", pst.get_size())
print()

msg_counter = 0

def search_dir(dir, path):
    if dir.get_display_name():
        new_path = path + u"/" + str(dir.get_display_name())
    else:
        new_path = path

    print("Searching ", new_path)

    for i in range(0, dir.get_number_of_sub_messages()):
        msg = dir.get_sub_message(i)
        try:
            if search_term in msg.get_plain_text_body():
                write_to_file(msg)
        except TypeError:
            pass

    for i in range(0, dir.get_number_of_sub_folders()):
        search_dir(dir.get_sub_folder(i), new_path)

def write_to_file(msg):
    global msg_counter
    with open("msgs/" + str(msg_counter) + ".txt", "wb") as f:
        f.write("Subject: ".encode("UTF-8"))
        f.write(msg.get_subject().encode("UTF-8"))
        f.write("\n\n".encode("UTF-8"))
        f.write(msg.get_plain_text_body().encode("UTF-8"))
    msg_counter = msg_counter + 1

search_dir(pst.get_root_folder(), u"")
