with open("f_txt", "w") as f:
    f.write("It is a first txt\n")
with open("f_txt", "r") as f, open("s_txt", "w") as s:
    s.write(f.read())