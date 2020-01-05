This project allows parse tex information from sites on the example of drioder.ru site.
You can make your parsing class for another sites with different text layout.
There are 3 files in the project. 1st - setting.py. This file contains all 
vk settings (login,password,api_key,group_id,group_name) and driver_path that necessary for selemium.
2nd file is functions.py.
It contains function for save text information in text file and upload file at VK group, 
it's also make VK post with text from file.
And 3rd file is mainFile.py. It's example/frame which do all project tasks on example droider.ru site.
This file parses text from droider.ru, create file with it, upload file and create post at VK group.
You only need to fill out the settings file your data and create your own parsing classes as needed.
You can check the performance right after entering your data by running mainFile.py.
Enjoyable use.
Samoylov Sergey.