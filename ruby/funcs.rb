 
# Functions start with def, function name, parameters if any
# They can return, or not a value
 
def add_nums(num_1, num_2)
  return num_1.to_i + num_2.to_i
end
 
puts add_nums(3,4)
 
# Variables are passed by value so the'r value can't be changed in a function
 
x = 1
 
def change_x(x)
  x = 4
end
 
change_x(x)
 
puts "x = #{x}"
 
# --------------- EXCEPTIONS ---------------
 
# We catch exceptions with begin and rescue
 
print "Enter a number : "
 
first_num = gets.to_i
 
print "Enter Another : "
 
second_num = gets.to_i
 
begin
  answer = first_num / second_num
 
rescue # You could use rescue ZeroDivisionError
  puts "You can't divide by zero"
  exit
end
 
puts "#{first_num} / #{second_num} = #{answer}"
 
# You can throw your own exceptions with raise
 
def check_age(age)
  raise ArgumentError, "Enter Positive Number" unless age > 0
end
 
# You catch them with rescue
 
begin
  check_age(-1)
rescue ArgumentError
  puts "That is an impossible age"
end
String Methods

Ruby String MethodsRuby
# --------------- STRINGS ---------------

# Strings are a series of characters between " or '
# String interpolation doesn't work with '' and neither do backslash
# characters like newline

puts "Add Them #{4 + 5} \n\n"
puts 'Add Them #{4 + 5} \n\n'

# A here-doc is normally used when you want a multiline string

multiline_string = <<EOM
This is a very long string
that contains interpolation
like #{4 + 5} \n\n
EOM

puts multiline_string

# ---------------------------------------

# Find all string methods by typing irb in terminal and "string".methods

first_name = "Derek"

last_name = "Banas"

# You can combine or concatenate strings with +

full_name = first_name + " " + last_name

middle_name = "Justin"

# Combining strings with interpolation

full_name = "#{first_name} #{middle_name} #{last_name}"
puts full_name

# You can check if a string contains a string with include

puts full_name.include?("Justin")

# Get the length of a string

puts full_name.size

# Count the number of vowels

puts "Vowels : " + full_name.count("aeiou").to_s

# Count the consonants

puts "Consonants : " + full_name.count("^aeiou").to_s

# You can check if a string starts with another string

puts full_name.start_with?("Banas")

# Return the index for the match

puts "Index : " + full_name.index("Banas").to_s

# Check equality of strings

puts "a == a : " + ("a" == "a").to_s

# Check if they are the same object

puts "\"a\".equal?(\"a\") : " + ("a".equal?"a").to_s
puts first_name.equal?first_name

# Changing Case

puts full_name.upcase
puts full_name.downcase
puts full_name.swapcase

# Stripping white space

full_name = "       " + full_name

full_name = full_name.lstrip
full_name = full_name.rstrip
full_name = full_name.strip

puts full_name

# Formatting Strings

puts full_name.rjust(20, '.')
puts full_name.ljust(20, '.')
puts full_name.center(20, '.')

# Chop eliminates the last character

puts full_name.chop

# Chomp eliminates \n or a specific string

puts full_name.chomp
puts full_name.chomp('as')

# Delete deletes provided characters

puts full_name.delete("a")

# Split a string into an array

name_array = full_name.split(//)
puts name_array

name_array = full_name.split(/ /)
puts name_array

# String Conversions

puts "a".to_i
puts "2".to_f
puts "2".to_sym

# Escape sequences
# \\  Backslash
# \'  Single-quote
# \"  Double-quote
# \a  Bell
# \b  Backspace
# \f  Formfeed
# \n  Newline
# \r  Carriage
# \t  Tab
# \v  Vertical tab
# --------------- STRINGS ---------------
 
# Strings are a series of characters between " or '
# String interpolation doesn't work with '' and neither do backslash
# characters like newline
 
puts "Add Thm #{4 + 5} \n\n"
puts 'Add Them #{4 + 5} \n\n'
 
# A here-doc is normally used when you want a multiline string
 
multiline_string = <<EOM
This is a very long string
that contains interpolation
like #{4 + 5} \n\n
EOM
 
puts multiline_string
 
# ---------------------------------------
 
# Find all string methods by typing irb in terminal and "string".methods
 
first_name = "Derek"
 
last_name = "Banas"
 
# You can combine or concatenate strings with +
 
full_name = first_name + " " + last_name
 
middle_name = "Justin"
 
# Combining strings with interpolation
 
full_name = "#{first_name} #{middle_name} #{last_name}"
puts full_name
 
# You can check if a string contains a string with include
 
puts full_name.include?("Justin")
 
# Get the length of a string
 
puts full_name.size
 
# Count the number of vowels
 
puts "Vowels : " + full_name.count("aeiou").to_s
 
# Count the consonants
 
puts "Consonants : " + full_name.count("^aeiou").to_s
 
# You can check if a string starts with another string
 
puts full_name.start_with?("Banas")
 
# Return the index for the match
 
puts "Index : " + full_name.index("Banas").to_s
 
# Check equality of strings
 
puts "a == a : " + ("a" == "a").to_s
 
# Check if they are the same object
 
puts "\"a\".equal?(\"a\") : " + ("a".equal?"a").to_s
puts first_name.equal?first_name
 
# Changing Case
 
puts full_name.upcase
puts full_name.downcase
puts full_name.swapcase
 
# Stripping white space
 
full_name = "       " + full_name
 
full_name = full_name.lstrip
full_name = full_name.rstrip
full_name = full_name.strip
 
puts full_name
 
# Formatting Strings
 
puts full_name.rjust(20, '.')
puts full_name.ljust(20, '.')
puts full_name.center(20, '.')
 
# Chop eliminates the last character
 
puts full_name.chop
 
# Chomp eliminates \n or a specific string
 
puts full_name.chomp
puts full_name.chomp('as')
 
# Delete deletes provided characters
 
puts full_name.delete("a")
 
# Split a string into an array
 
name_array = full_name.split(//)
puts name_array
 
name_array = full_name.split(/ /)
puts name_array
 
# String Conversions
 
puts "a".to_i
puts "2".to_f
puts "2".to_sym
 
# Escape sequences
# \\  Backslash
# \'  Single-quote
# \"  Double-quote
# \a  Bell
# \b  Backspace
# \f  Formfeed
# \n  Newline
# \r  Carriage
# \t  Tab
# \v  Vertical tabe
