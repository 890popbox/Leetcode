import datetime
from dateutil.relativedelta import relativedelta


# Check if the given is palindrome excluding spacing
def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

# Short python code to take all the dates from now to 10,000 days in the future and
# write them to a file if they are a Palindrome. Short amount of days for space however 1mil+ if easily doable
print('\n   US                UK\n')
print('mm/dd/yyyy        dd/mm/yyyy\n')
filetowritehandler = open('palindromeDates.txt', "w")  # Write mode
filetowritehandler.write('A list of Palindrome Dates from now to ~10,000 days in future\n')
filetowritehandler.write('   US                UK\n')
filetowritehandler.write('mm/dd/yyyy        dd/mm/yyyy\n' + '\n')

# using time to make this easier
for abc in range(1, 10000):
    time_now_plus_abc = datetime.datetime.now() + relativedelta(days=abc)
    date_formatedus = time_now_plus_abc.strftime("%m%d%Y")
    date_formateduk = time_now_plus_abc.strftime("%d%m%Y")
    data_us = (date_formatedus if isPalindrome(date_formatedus) else '        ')
    data_uk = (date_formateduk if isPalindrome(date_formateduk) else '        ')
    if data_us != '        ' or data_uk != '        ':
        line = data_us + '          ' + data_uk
        print(line)
        filetowritehandler.write(line + '\n')
filetowritehandler.close()
