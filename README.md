# Project Overview
### This project facilitates the organization of a collection of pictures based on metadata and employs Clarifai's AI face detection model for further organization. 
### Users can select a directory in their computer where they desire to store organized pictures, choose multiple images for organization, and sort them into year and month folders.
### It also identifies images containing people and separates them into another folder within each month.

# Warning!
### Please use your pictures or pictures that you are sure contains metadata. Most pictures downloaded from the internet do not contain metadata.Therefore, the program won't work properly.

# Installation and Setup Instructions
## Packages and libraries used:
### 1. Ensure you have Python installed
### 2. Install the following libraries that are necessary to run the code:
### [Pillow]
### Description: It provides extensive file format support, image processing capabilities, and metadata extraction which were essential for this project's image manipulation tasks.
### Installation: 'pip install pillow'
### [Tkinter]
### Description: It is used in this project to create the user interface, enabling users to interact with the application.
### Installation: Tkinter should come along when installing Python. If not, use the pip command 'pip install tkinter'
### [Clarifai Python Client]
### Description: The Clarifai Python Client provides an interface to interact with Clarifai's AI models, specifically for tasks like image analysis and recognition.
### It's used in this project for detect faces in an image. 
## Installation: 'pip install clarifai'

# Usage Guide
## Using the interface:
### 1. Choose the destination directory for organized pictures
### 2. Select the images to be organized
### 3. The program will execute and return a success message 

## Folder Structure:
### - Organized pictures will be stored as following: 'Destination Directory > Year Folder > Month Folder > Images with people Folder'

## Testing Procedures
### 1. Select a directory in your computer where you would like to store the organized images.
### 2. Give it a name to the folder where all the organized folders will be.
### 3. Select the images you would like to organize (with different capture dates if possible)
### 4. Check the 'Images with People' folder within each month to ensure they are organized correctly. 
### Please take into consideration that, only landscape without any people on it will not be moved to the "images with people" folder.

## Contributors
### Contributors: 
### 1. Domenica Valencia - Developer/ Creator of the program.
### 2. Professor Gil Salu -  We worked together on implementing the Clarifai AI model for this particular project. Thanks, Professor Salu!
### 3. Knack Tutor: Alex W. - We worked together on the debugging and error handling part of the Project. Thanks, Alex!
### 4. TA: Marious P. - We worked together on the beginning stage of the program and got the Project's logic down. Thanks, Marious!