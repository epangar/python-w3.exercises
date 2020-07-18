from subprocess import call
import os





def create_folders(start):

  end = start + 9
  str_start = str(start)
  str_end = str(end)

  """ create a folder """
  name_of_folder = str(str_start +"-"+str_end )
  print("Created new folder: " + name_of_folder)
  call(['mkdir' , name_of_folder])

  """ get access to the new folder """
  os.chdir(name_of_folder)

  """ create 10 files """
  for n in range(start, end+1):
    name_of_file = str(n)+'.py'
    call(['touch',  name_of_file])

  """ go up a level """

  os.chdir('../')

create_folders(111)