#seek(),tell()

with open('myfile2.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(10)

  # Read the next 5 bytes
  data = f.read(5)
  print(data)

   # Save the current position
  current_position = f.tell()
  print(current_position)

f=open('myfile4.txt','w')
f.write("helloo jarvis")
# write only first argument length
f.truncate(10)