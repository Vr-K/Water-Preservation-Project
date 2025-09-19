# Water-Preservation-Project 🌾
## East-Uudenmaan and Porvoo river water and air protection association Project

- [Veera](https://github.com/Vr-K) (scrum master)
- [Jakub](https://github.com/Jakub-Marciszonek) (junior dev)
- [Prashant](https://github.com/Prashant883883) (research)

### Currently we are doing preliminary research on how the programs used by East Uudenmaan and Porvoo River water and air protection association work and gathering knowledge on plants and invasive species of vegetation on Finnish waterways. We plan to have an working AI, demo or a prototype that can detect invasive species.

19.09.2025

We have working webodm and are researching AI. 
Veera needs to write a WebODM installation guide.
However we do not know how to implement datasets into the workflow. How to actually use WEBODM since we do not have useable data for that. And etc.
~~Someone needs to look into TensorFlow and someone else into Keras. I can look into Wazuh and security. There is just so much we need to look into and see how to get about it all.~~
APIs we can use? There are the databases Jakub found. Do we need to look into how to train that data? Or is the data not usable to us because we do not know what data we are perceiving? Do we need to clean the data?

I've found datasets of vegetations photo that could show us in what directions we can aim, plus some possibly are going to be used for training. So far finding datasets that would fit in our expectation is quiet hard (drone photos of water areas with somehow tagged vegetation) if we would have access to the photos taken for the east-usima project and taging them with some external help would be very beneficial. 
At this moment selected two pretrained models for this project APNet-YOLOv8s and DenseNet201 first one is better suited for local AI as its more recourse efficient but the latter is more precise and have more space and potencial for other feuters and even more precision with cost of high computing power required which exteend the time of excecution significatly enough to make it not optimal for local aplicaton and centralized aproche is recommended.

Current tasks/questions that need answers:
- How to use datasets to train AI?
   - There are numerous tutorials on the topic which are linked in Teams. But the datasets seem to only contain raw data.
- How does WebODM work?
   - for this one we need Client image data to test the prgram. Currently we lack the drone data to test things out.
- Need to Train said Data
   - Again Teams has some tutorials on how to progress. Might have nothing, but we are still looking into
- Need to make WebODM installation tutorial
    - Veera knows how to install the program and needs to write a quick tutorial so other people dont end up wasting time doing the same-
- In the databases do we need to utilize Photoshop or other image editing software(Gimp)?
   - Again need to read up tutorials on how to make Image recognition AI and how to train it
