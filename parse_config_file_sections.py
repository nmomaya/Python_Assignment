#!/usr/bin/python
import io

def parse_config_file(file_name):
    if type(file_name) != str:
        print("File Name should be a string.")
        return
    fd = io.FileIO(file_name)
    result = {}
    sections = {}
    if fd != None:
        #read first line
        line = fd.readline()
        section_name = ""
        section_start = False
        while line != b"":
            #this will ignore lines starting with "#"
            if not line.startswith(b"#"):
                #this will ignore empty lines
                if not line.startswith(b"\n"):
                    line = line[:-1] # this code removes '\n' from the line
                    if b"=" in line:
                        if b"#" in line:
                            index = line.find(b"#")
                            line = line[:index]
                        print(line)
                        pair = line.split(b"=")
                        pair[0] = pair[0].strip()
                        pair[1] = pair[1].strip()
                        result[pair[0]] = pair[1]
                    elif line.startswith(b"["):
                        if section_start == True:
                            sections[section_name] = result
                        section_name = line[1:-1]
                        section_start = True
                        result = {}
            line = fd.readline()
            if line == b"":
                if section_start:
                    sections[section_name] = result

    return sections
def main():
    file_name = input("Enter Config File Name :")
    result = parse_config_file(file_name)
    print(result)
    print(result['Headset']['HFP'])

if __name__ == "__main__":
    main()
