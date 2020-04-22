# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # Script to copy and paste labeled data # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Save the folder which needs to be traversed inside another folder containing the script.
# Check if the structure of the folder is appropriate ie the target folder must contain
# different folders with every folder containing the files.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # Root -> Many folders and Files -> Files # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import os 
import shutil
folderName = 'Global'
if __name__ == "__main__": 
    for (root,dirs,files) in os.walk('Global', topdown=True):
        for i in files:
            if(i=='.DS_Store'):
                pass
            else:
                completePath = os.path.join(root,i)
                if('RIGHT' in i.upper()):
                    original = completePath
                    target = 'globalCheck/RIGHT/' + i
                    shutil.copyfile(original, target)
                elif('PAIR' in i.upper()):
                    original = completePath
                    target = 'globalCheck/PAIR/' + i
                    shutil.copyfile(original, target)
                elif('SOLE' in i.upper()):
                    original = completePath
                    target = 'globalCheck/SOLE/' + i
                    shutil.copyfile(original, target)
                elif('CLOSE' in i.upper()):
                    original = completePath
                    target = 'globalCheck/CLOSE/' + i
                    shutil.copyfile(original, target)
                elif('LEFT' in i.upper()):
                    original = completePath
                    target = 'globalCheck/LEFT/' + i
                    shutil.copyfile(original, target)

                if('MAIN REVERT' in i.upper()):
                    original = completePath
                    target = 'globalCheck/MAIN-REVERT/' + i
                    shutil.copyfile(original, target)
                elif('MAIN' in i.upper()):
                    original = completePath
                    target = 'globalCheck/MAIN/' + i
                    shutil.copyfile(original, target)
                
                if('SIDE BACK' in i.upper()):
                    original = completePath
                    target = 'globalCheck/SIDE-BACK/' + i
                    shutil.copyfile(original, target)
                elif('BACK' in i.upper()):
                    original = completePath
                    target = 'globalCheck/BACK/' + i
                    shutil.copyfile(original, target)
                elif('SIDE' in i.upper()):
                    original = completePath
                    target = 'globalCheck/SIDE/' + i
                    shutil.copyfile(original, target)
                    