# 🌾 Water-Preservation-Project 🌾 
## East-Uudenmaan and Porvoo River water and air protection association and LAB University Project

(need to add anchors list for easier handling)

- [Veera](https://github.com/Vr-K)
- [Mamata](https://github.com/mamatanepal53)
<br>
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img width="180" height="180" alt="image" src="https://github.com/user-attachments/assets/a53c3b8d-91e3-4552-95c9-cce5f4628a6b" />
	</a>
</div>


<h3 align="center">Finnish invasive plant species object detection AI</h3>

<!-- ABOUT THE PROJECT -->
## 🦭 About The Project
<br>
This is our student group project for our second year, starting from Fall 2025, for Itä-Uudenmaan ja Porvoonjoen vesien- ja ilmansuojeluyhdistys. The aim of this project is to create a working object detection AI, learn how to make a Image detection AI and how to work one. Where once given a photogrammeric map of an area, the OB will be capable of recognizing harmful vegatation within the area, with possible heatmap detection capabilities. In this project learning to gather drone images to generate dataset and segment it. How to albumentate said dataset. And other related tasks on how to make an Computer Vision AI.

## 🌾🌾🌾 Aim of project is to help with detecting invasive species using aerial drone- images and/or video. On dry land, wetland and water. From heights 30m or 50m height off the ground.

## 🗂️ Folder structure and what contains what
#### Dataset Guide<br>
Guides on how to make 1) Dataset(and env) 2) Work WebODM 3) Work with CSC Roihu(in progress) 4) Possibly depricated guide on Puhti
#### Heatmap<br>
YOLOv8/11 Heatmap files
#### Labels<br>
Simple labeling examples for different formats in project
#### Sprints<br>
Journal of the project so far
#### TerrainSegModel<br>
First layer of the AI process, possibly depricated. Currently on hiatus.
#### UI/plant_map<br>
Planned UI. On hiatus until models are done. Should work.
#### files<br>
Contains all .py files to work out the project.
#### heatmap_demo<br>
Literally all that Prashant contributed to the project. It is broken heatmap that was copy pasted from an conversation he had with an LLM the night before final deadline in 2025. :(

## 🌿 List of invasive species we are looking to add to the model(In Finnish and Latin):

- [x] sinilevä (Cyanobacteria)<br>
- [x] komealupiini (Lupinus polyphyllus)<br>
- [x] jättiputki -ryhmä (Heracleum persicum -ryhmä)<br>
- [x] jättipalsami (Impatiens glandulifera)<br>
- [x] kurtturuusu (Rosa rugosa)<br>
- [ ] kanadanpiiskun (Solidago canadensis) + muut haitalliset vieraslajipiiskut<br>
- [x] viitapihlaja-angervo (Sorbaria sorbifolia)<br>
- [ ] valkopajuangervo (Spiraea alba)<br>
- [x] japanintatar (Reynoutria japonica) + muut haitalliset tatar-lajit<br>
- [ ] kanadanvesirutto (Elodea canadensis)<br>
- [ ] kiehkuravesirutto (Elodea nuttalii)<br>
- [x] terttuselja (Sambucus racemosa)<br>
- [ ] isotuomipihlaja (Amelanchier spicata)<br>
- [x] valkokarhunköynnös (Convolvunus sepium)<br>
- [x] isosorsimo (Glyceria maxima)<br>
<br><br>
We have not been able to find all plants even once on the above list. And some were simply forgotten to look for due to the lenght of the list.

<!-- GETTING STARTED -->
## 🔰 Getting Started

Under construction. For now see files Dataset Guide and folder on how to get started. Add progress/pipeline on how to work the project [here].

### 🛠️ Tools used

1. YOLOv8 and Ultralytics		- training + model, possibly changing over to YOLOv11 or YOLOv26 for their higher accuracy
2. Python						- for running the programs
3. Mavic Pro 2					- gathering drone images
4. Docker						- running WebODM
5. Git							- running WebODM
6. WebODM						- Combining large volume of drone images into one cohesive image. Possibly depricated for this project.
7. Albumentations				- Module for additional augmented images for larger model training
8. SAM2							- Module for helping segment bbox dataset into segmented dataset
9. Label-Studio					- Generating databases for the models to train on of
10. CSC super computers			- Physically training the model, puhti was previously used, but the CSC taken that offline. Will be using Roihu in near future.


<!-- USAGE EXAMPLES -->
## 👀 Usage

The models and datasets will be open source one project is finished. Currently there are plans for 4 distinct AI for months in the summer and easier invasive species detection, between May-Aug. In progress. Looking for a place to drop the datasets and raw images. Huggingface and Kaggle possibly could work, have not looked into what to use yet.<br>
Links to dataset to be provided once finished.

<!-- ROADMAP -->
## 🛣️ Roadmap. Or rather to do list

- [ ] CSC training AI
- [x] Heatmap prototype
- [x] Implement Albumentation into dataset creation process
- [x] Remake datasets to be in line with pretraining data
- [ ] Finish working on datasets
- [ ] Gather images for dataset.
- [x] Rework the readme
- [ ] SAM2 test files
- [ ] Implement UI. We have UI, but have not combined everything together.

<!-- CONTACT -->
## 🔎 Contact
Our contact person is<br>
Veera Korkeamäki - veera.korkeamaki@student.lab.fi
<br><br>
Project Link: Water Preservation Project](https://github.com/Vr-K/Water-Preservation-Project)


<!-- ACKNOWLEDGMENTS -->
## 🥸 Acknowledgments

* [Itä-Uudenmaan ja Porvoonjoen vesien- ja ilmansuojeluyhdistys](https://vesi-ilma.fi/) Porvoonjoen water protection association
* Klemola Pauliina, Ympäristönhoitaja, Kouvolan kaupunki. For helping locate places in Kouvola with invasive species. 
* Mirva Ketola and Anna Hakala, Vesijärvi Säätiö. For helping locate places in Lahti water area with invasive species.
* []() Mira Vorne. Tutor teacher for the project
* [Jakub](https://github.com/Jakub-Marciszonek) (The head of AI on the project in fall semester 2025)
* [Prashant](https://github.com/Prashant883883) ("Research" on the project in fall semester 2025)


