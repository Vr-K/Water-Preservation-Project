# 🌾 Water-Preservation-Project 🌾 
## East-Uudenmaan and Porvoo River water and air protection association Project

- [Veera](https://github.com/Vr-K) (struggling to survive)
- [Jakub](https://github.com/Jakub-Marciszonek) (Our AI head)
- [Prashant](https://github.com/Prashant883883) (research)
- [Mamata](https://github.com/mamatanepal53) (Our new team member)

#### 17.10.2025

Review

We had a meeting where we met with Riitta Kortisuo and Juha Salo though Teams.

Juha was the Tech head, not officially tech, but a hobbyist, seemed interested in what we had to offer. Had ideas on how to move forward if our project does end up being useful in the long term.

Riitta is a nature surveyor for the Association, does hands on work

Apparently Porvoojoki lacks in oxygenation in the summer? Professionals are looking into the why.

Our team: AI based, input images, AI with resulted data.

Our project could add a layer documentation when existing macro plant removal is done, for recreational reasons. When you remove macro plants different plants tend to take over, affects bio balance, this photogrammery might be helpful in making people in positions of power see the result of human intervention. (More data = better data)

We are to present demos at the end of course on december 12th. BEFORE. 12th.

Realization that the seasons are VERY different for plants(obvious but), this will affect datasets. Do we need to make seasonal datasets?

Change of plans with AI. Jacub said Svin Transform connection to YOLOv8 beyond his skill level, so we aare only using YOLOv8. Not really compatiable. It apparently also has the Svin Transform capabilities, will look more into this. UNET, something more precise.

Mamata and Prashant ended up staying in team. We will change up how things are done in the team though, we will start using ganban board. This will be more fair for everyone.

Until next meeting:
- Mamata will focus on GUI for the project 
- Prashant will look into research relating to Heatmap
- Jakub continues with YOLOv8 set up.
- Veera will remake the dataset. possibly get started on heatmaps as well(bring the tera brick so people can get the image data as well and start making datasets as well)

Regarding datasets, we might need to make different ones? or rather layers of Datasets. See image. We will propably make multiple smaller AIs to test things which will mean layered datasets.

Ex. Make 1st layer dataset that recognized a forest. 2nd layer AI recognizes Species of the Trees. 3rd layer can tell which time of year those trees are in the images. Etc. This is called something like Segmentation in YOLO. Jakub should have made a short explanation that propably makes more sense, might add to sprint.

#### Jakub's take on why we dropped the Svin Transform:

In ultralytics\nn\tasks.py file the f (from) value keeps me from integrating custom swin-transfomer module into YOLOv8. The value in the file is defined in the line:

    for i, (f, n, m, args) in enumerate(d["backbone"] + d["head"]):  # from, number, module, args

This line associate the configuration content by lines interpretation said lines as lists
The configuration file example looks like this:
backbone:

  - [from, repeats, module, args]
    - [-1, 1, Conv, [64, 3, 2]] # 0-P1/2

- The issue that made me stop of integrating the swin transformer into YOLOv8 is that f value in some cases is expected to be integer and in other tuple 

        if m in base_modules:
            c1, c2 = ch[f], args[0]

- This line is requiring that f is an integer so it caused error when f was tuple

        elif m is Concat:
            c2 = sum(ch[x] for x in f)
        elif m in frozenset(
            {Detect, WorldDetect, YOLOEDetect, Segment, YOLOESegment, Pose, OBB, ImagePoolingAttn, v10Detect}
        ):
            args.append([ch[x] for x in f])
            if m is Segment or m is YOLOESegment:
                args[2] = make_divisible(min(args[2], max_channels) * width, 8)
            if m in {Detect, YOLOEDetect, Segment, YOLOESegment, Pose, OBB}:
                m.legacy = legacy
        elif m is RTDETRDecoder:  # special case, channels arg must be passed in index 1
            args.insert(1, [ch[x] for x in f])

- And these few lines show where the error occurred when f was an integer. Specifically by this part of these lines:

      ch[x] for x in f

- That tries to go through every element of f as it would be an list.

  
Programs/things related to the project:

1) YOLOv8
2) Svin Transform
3) Label Studio
4) WebODM
