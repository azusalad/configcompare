from config import *

def get_lines(f_name):
    """get file contents and ignore comments and stuff in ignore_list"""
    # remove comments
    with open(f_name, 'r') as f:
        no_rems = [x.strip().split('//')[0] for x in f.readlines() if x[0] != '/']
    # remove stuff in ignore_list
    no_ignores = [x for x in no_rems if x.split(' ')[0] not in ignore_list]
    # remove empty lines
    return [x for x in no_ignores if x != '']

def get_commands(lines):
    """Return a dictionary of the lines of the file.  command:value"""
    commands = [x.split() for x in lines]
    command_dict = {}
    for x in commands:
        command = x[0]
        value = x[1]
        if len(x) != 2:
            # sometimes the value will have spaces in them
            if ('"' in x[1] and '"' in x[-1]) or ("'" in x[1] and "'" in x[-1]):
                value_with_spaces = list(' '.join(x[1:]))
                value_with_spaces.pop(0)
                value_with_spaces.pop(-1)
                command_dict[command] = ''.join(y for y in value_with_spaces)
            else:
                print('Warning this command does not have 2 parts, skipping: ' + ' '.join(str(y) for y in x))
        else: # check if value has quotes around or not
            if (value[0] == "'" and value[-1] == "'") or (value[0] == '"' and value[-1] == '"'):
                command_dict[command] = value[1:-1]
            else:
                command_dict[command] = value
    return command_dict

def write_header(text):
    """Make a nice header for a section"""
    a = []
    a.append('// ----------------------------------------------------------------------------\n')
    a.append('// ' + str(text) + '\n')
    a.append('// ----------------------------------------------------------------------------\n')
    return ''.join(x for x in a)

# get commands
f1 = get_commands(get_lines(f1_name))
f2 = get_commands(get_lines(f2_name))

# find differences
diff = []
f1_only = []
f2_only = [x for x in f2 if x not in f1]
for command in f1:
    if command in f2:
        if f2[command] != f1[command]:
            diff.append(command)
    else:
        f1_only.append(command)

# write differences to a file
f = open('diff.txt', 'w')
# write f1 only
f.write(write_header(f1_name + ' only'))
for command in f1_only:
    f.write(command + ' "' + str(f1[command]) + '"\n')
f.write('\n')

# write f2 only
f.write(write_header(f2_name + ' only'))
for command in f2_only:
    f.write(command + ' "' + str(f2[command]) + '"\n')
f.write('\n')

# differences
f.write(write_header(f'In both files but different values.'))
f.write('\n// Quick compare list.  Format: command "{f1_name}" "{f2_name}"\n')
for command in diff:
    f.write(f'{command} "{f1[command]}" "{f2[command]}"\n')
f.write('\n')

f.write(f'\n// Taking values from {f1_name}\n')
for command in diff:
    f.write(f'{command} "{f1[command]}"\n')
f.write('\n')

f.write(f'\n// Taking values from {f2_name}\n')
for command in diff:
    f.write(f'{command} "{f2[command]}"\n')

f.close()
