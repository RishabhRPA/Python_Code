text='Rishabh'

#reversed_Text=text[::-1]
#print(reversed_Text)
reverse_Text=""
#reverse_Text=reverse_Text.join(reversed(text))
#print(reverse_Text)
for item in text:
    reverse_Text=item+reverse_Text

print(reverse_Text)
