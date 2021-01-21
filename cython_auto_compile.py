import argparse, os
from subprocess import Popen
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Turn a normal python file into a cython optimised one')
    parser.add_argument("file", metavar='F', type=str, help='file to run compilation on')
    parser.add_argument("data", metavar='D', type=str, help='file with arguments to run script with')
    args = parser.parse_args()
    x = 3
    with open(args.file, "a") as f:
        f.write("\nfor i in [s for s in dir() if not '__' in s]: print(i, eval('type(%s)'%i))")
    variables = {}
    #p = Popen([command], shell=True)
    with open(args.data, "r") as f:
        for line in f.readlines():
            command = "python %s/%s %s" % (os.getcwd(), args.file, line)
            p = os.popen(command)

            for i in p.readlines():
                var_name, var_type = i.split(" ")[0], i.split(" ")[2].replace("'", "").replace(">", "").replace("\n", "")
                if var_type not in ["int", "str", "list", "dict"]:
                    continue
                #Check if the var_name exists in variables
                if variables.get(var_name, ''):
                    # If it does, check if it matches var type
                    if variables.get(var_name) != var_type:
                        # If it doesn't match var type, set it to false (cannot be static type)
                        variables[var_name] = False
                # If the var type is false, it means it failed our previous check, dont add.
                # If its not false, assume its a new var and add.
                elif variables.get(var_name) != False:
                    variables[var_name] = var_type
        print(variables)
    # Add CDEFs
    with open(args.file+"x", "a") as optimised_file:
        with open(args.file, "r") as f:
            for line in f.readlines():
                print(line.replace(" ", ""))
                no_whitespace = line.replace(" ", "")
                leading_whitespace = len(line)-len(line.lstrip(' '))
                leading_whitespace = ' '*leading_whitespace
                for key in variables.keys():
                    if no_whitespace.startswith(key+"=") and variables[key] != False:
                        line = leading_whitespace+"cdef %s %s" % (variables[key], line.lstrip(' '))
                optimised_file.write(line)
