# Given a date string in the form Day Month Year, where:

# Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
# Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
# Year is in the range [1900, 2100].
# Convert the date string to the format YYYY-MM-DD, where:

# YYYY denotes the 4 digit year.
# MM denotes the 2 digit month.
# DD denotes the 2 digit day.
 

# Example 1:

# Input: date = "20th Oct 2052"
# Output: "2052-10-20"
# Example 2:

# Input: date = "6th Jun 1933"
# Output: "1933-06-06"
# Example 3:

# Input: date = "26th May 1960"
# Output: "1960-05-26"
 

# Constraints:

# The given dates are guaranteed to be valid, so no error handling is necessary.

class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """

        day_list=["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th", "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st"]

        month_list=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        day=day_list.index(date[0:4].strip())+1

        month=month_list.index(date[4:8].strip())+1

        year=date[8:].strip()

        return year+"-"+"{:02d}".format(month)+"-"+"{:02d}".format(day)




        
        
