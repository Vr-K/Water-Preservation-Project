# 🌾 Water-Preservation-Project 🌾 
## East-Uudenmaan and Porvoo River water and air protection association Project

- [Veera](https://github.com/Vr-K) (scrum master)
- [Jakub](https://github.com/Jakub-Marciszonek) (junior dev)
- [Prashant](https://github.com/Prashant883883) (research)
- [Mamata](https://github.com/mamatanepal53) (possible new team member. Haven't asked for her github yet)

### We have decided on YOLOv8 object recognition AI for now and are looking to test and create working data sets for it using LabelImg. Looking into Svin Trnasformer to add to the process as well.

We have the theory on working AI, just need to start work on prototypes.

🌊 🌊 🌊 03.10.2025 🌊 🌊 🌊

WebODM data ended up being useless for the project. At least for now, could be useful for future data wrangling of the large files.

Prashant suggested we use RoboFlow since it can be used to train AI Vision, but it was decided it might be unusable in this situation considering the free mode having a data processing limit along with image volume limit. He found also promising dataset on Finnish plants, but it remains to be seen, need to have a more throughout look.

Veera says they figured out how to make an dataset that can be used with YOLOv8 for free. They will test out the process and maybe make a tutorial for a dataset to use in this. Since if the project continues past the projected current scope, it would be needed. However it would require manual effort on image labeling front, that we would have to do anyway since the images are very specialized.

Jakub finally says he has narrowed down the best object detection AIs for the project and it should be YOLOv8. YOLOv9 is a newer version but the image recognition seems to only be 1,5% better and that gap will be even less if we are able to add Svin Transformer on top of it. However v8 is easier to set up and requires less knowledge on the part of the user to do so. This will be more useful with less tech savvy client. He will keep on tinkering and figuring out how to work the AI in general.

We have possibly a new member in Mamata. For now she will be going through documentation we have(which is not as good as it should be, but it exists) and decide on next Friday if she wants to join the Team or not.

We met up with Kimmo for the first time with other teams. We were the only team that did not realize we should have made a presentation to explain what we are doing, but apparently it went well anyway. We got the raw images from drone flights, contact information for Kimmo and possible names of people we could contact for help. Namely in biologist sense, to help with labeling and plant recognition.

Current tasks/questions that need answers:
- Need to make a working dataset so it can be tested with AI
   - Namely Veera since they keep on being the one going "oh i know how to make a dataset".
- Find a way to transfer several GB of data between two computers without drive or github since there is so much data
   - Actually we might be able to move the data between the group in just github, it seems to all be a total of 30GB.
- Sent the summary of what we are doing to Kimmo
   - Another task for Veera, since they are the one writing this sprint review as we speak
-  Lots of data in Teams Channel that needs to be gone over and cleaned up.
-  Push the project updates to moodle as well, because I keep forgetting to do that
-  Contact people and wether they would be willing to help with the project/labeling/plant listing/that thing
  
Programs/things related to the project:

1) YOLOv8
2) YOLO (Darkside) format/ PyTorch TXT. Same thing different name
3) LabelImg
