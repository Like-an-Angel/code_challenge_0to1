"""
File Owners - medium

Implement a group_by_owners function that:

    Accepts a dictionary containing the file owner name for each file name.

    Returns a dictionary containing a list of file names for each owner name, in any order.

For example, for dictionary:

{
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

the group_by_owners function should return

{
    'Randy': ['Input.txt', 'Output.txt'],
    'Stan': ['Code.py']
}

"""
def group_by_owners(files):
    folder = dict()
    for record in files.keys():
        # if document list for a current author exists:
        if folder.get(files[record]):
            folder[files[record]].append(record)
        else:
            folder[files[record]] = [record]
    return folder

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))
