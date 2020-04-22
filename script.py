# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # Script to copy and paste labeled data # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Save the folder which needs to be traversed inside another folder containing the script.
# Check if the structure of the folder is appropriate ie the target folder must contain
# different folders with every folder containing the files.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # Target Folder -> Many folders -> Files # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import os 
import shutil
# Name of the folder
path ='07.06.2019/' 
dir= os.listdir(path)

for i in range(len(dir)):
    if(dir[i]=='.DS_Store'):
        pass
    else:
        leaf = os.listdir(path + dir[i])
        for j in range(len(leaf)):
            completePath = path + dir[i] + '/' + leaf[j]
            
            if('RIGHT' in leaf[j]):
                original = completePath
                target = 'check2/RIGHT/' + leaf[j]
                shutil.copyfile(original, target)
            elif('PAIR' in leaf[j]):
                original = completePath
                target = 'check2/PAIR/' + leaf[j]
                shutil.copyfile(original, target)
            elif('SOLE' in leaf[j]):
                original = completePath
                target = 'check2/SOLE/' + leaf[j]
                shutil.copyfile(original, target)
            elif('CLOSE' in leaf[j]):
                original = completePath
                target = 'check2/CLOSE/' + leaf[j]
                shutil.copyfile(original, target)
            elif('LEFT' in leaf[j]):
                original = completePath
                target = 'check2/LEFT/' + leaf[j]
                shutil.copyfile(original, target)

            if('MAIN REVERT' in leaf[j]):
                original = completePath
                target = 'check2/MAIN-REVERT/' + leaf[j]
                shutil.copyfile(original, target)
            elif('MAIN' in leaf[j]):
                original = completePath
                target = 'check2/MAIN/' + leaf[j]
                shutil.copyfile(original, target)
            
            if('SIDE BACK' in leaf[j]):
                original = completePath
                target = 'check2/SIDE-BACK/' + leaf[j]
                shutil.copyfile(original, target)
            elif('BACK' in leaf[j]):
                original = completePath
                target = 'check2/BACK/' + leaf[j]
                shutil.copyfile(original, target)
            elif('SIDE' in leaf[j]):
                original = completePath
                target = 'check2/SIDE/' + leaf[j]
                shutil.copyfile(original, target)











    






        
    
