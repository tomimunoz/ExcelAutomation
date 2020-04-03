import os, fnmatch


def xlsx_searcher():
    directory = '.'
    directory_log = {0: directory}
    it = 0
    while directory != "*.xlsx":
        listOfFiles = os.listdir(directory)
        pattern = "*"
        files_list = []
        select = {}
        i = 0
        for entry in listOfFiles:
            if fnmatch.fnmatch(entry, pattern):
                i += 1
                select[i] = entry
                print(f'{i} - {select.get(i)}')

        if i == 0:
            print('No files found :(')

        if it != 0:
            i += 1
            select[i] = '️⬅️ Go back'
            print(f'{i} - {select.get(i)}')
        it += 1
        while True:
            print('----------------------------------')
            number = int(input(f'Select a number file or folder: '))
            if number > i or number < 1:
                print('Incorrect number, try again')
            if number == i and it != 1:
                directory_log[it] = directory_log[it-2]
                directory = directory_log[it]
                break
            else:
                directory = select.get(number)
                directory_log[it] = f'{directory_log[it - 1]}/{directory}'
                directory = directory_log[it]
                break
        xlsx_finder = directory[-5:]
        if xlsx_finder == '.xlsx':
            ans = input(f'Is {directory} the excel archive you want to modify? Y/N ').upper()
            if ans == 'Y' :
                break
    return directory
