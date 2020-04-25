def checkPalindrome(orgstring):
    if (orgstring == ""):
        return true
    begin = 0
    end = len(orgstring) - 1

    while (orgstring[begin] == orgstring[end] and begin < end):
    	begin += 1
    	end -= 1

    if (begin >= end):
        return True

    return False

def nextPalindrome(orgnumber):
    if (checkPalindrome(orgnumber)):
        return orgnumber

    left = right = 0
    middle = int(len(orgnumber) / 2)

    if (len(orgnumber) % 2 == 0): #even length case
        left = middle - 1
        right = middle
    else :#odd length case
        left = middle - 1
        right = middle + 1

    while (left >= 0):
        if (orgnumber[left] == orgnumber[right]):
            left -= 1
            right += 1
        elif(orgnumber[left] != orgnumber[right]):

            if (int(orgnumber[left]) < int(orgnumber[right])):
                orgnumber = orgnumber[: right - 1] + str((int(orgnumber[right - 1]) + 1)%10) + '0' * (len(orgnumber) - right)
                return nextPalindrome(orgnumber)
            else :
                orgnumber = orgnumber[: right] + orgnumber[left] + '0' * (len(orgnumber) - right - 1)
                return nextPalindrome(orgnumber)

    return orgnumber

if(__name__ == "__main__"):
  testcases = int(input())
  for _ in range(testcases):
      number = input()
      if (checkPalindrome(number)):
          number = str(int(number)+1)
      print(nextPalindrome(number))
