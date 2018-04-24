#String Slicing
word = "supercalifragilisticexpialidocious"
#getting from certain string until the :end
word[word.index("docious"):]
print(word)
#Lecture Project

#Get User E-Mail Address
email = input("What is your email address?: ").strip() #strip takes away any spaces after if the user does that by accident
#slice out user name.
#Takes everything up until @ symbol
user = email[:email.index("@")]
#slice out domain name
#slice out everything AFTER @ symbol. Starts at @ symbol + 1 character after
domain = email[email.index("@") + 1 :]
#format message
output = "Your username is {} and your domain name is {}".format(user, domain)

#display output message
print(output)
